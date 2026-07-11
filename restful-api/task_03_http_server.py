#!/usr/bin/env python3
"""Module that implements a simple API using http.server."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for a simple API."""

    def send_text_response(self, status_code, text):
        """Send a plain text response."""
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def send_json_response(self, status_code, data):
        """Send a JSON response."""
        response = json.dumps(data)

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self.send_text_response(
                200,
                "Hello, this is a simple API!"
            )

        elif self.path == "/data":
            self.send_json_response(
                200,
                {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
            )

        elif self.path == "/status":
            self.send_text_response(200, "OK")

        elif self.path == "/info":
            self.send_json_response(
                200,
                {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
            )

        else:
            self.send_text_response(404, "Endpoint not found")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)

    print("Server running on http://localhost:8000")
    httpd.serve_forever()
