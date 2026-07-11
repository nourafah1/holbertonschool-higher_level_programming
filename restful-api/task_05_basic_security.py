#!/usr/bin/env python3
"""API demonstrating Basic and JWT authentication."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-jwt-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify Basic Authentication credentials."""
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        return username

    return None


@auth.error_handler
def basic_auth_error(status):
    """Return a response for invalid Basic Authentication."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message for valid Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT access token."""
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if user is None or not check_password_hash(
            user["password"], password or ""):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message when a valid JWT is supplied."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return a message only when the user has the admin role."""
    username = get_jwt_identity()
    user = users.get(username)

    if user is None or user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(error):
    """Handle missing JWT tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(error):
    """Handle invalid JWT tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired JWT tokens."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked JWT tokens."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle JWT tokens that are not fresh."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
