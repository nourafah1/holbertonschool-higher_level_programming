def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(
            f"Invalid input: template must be a string, "
            f"got {type(template).__name__}."
        )
        return

    if not isinstance(attendees, list):
        print(
            f"Invalid input: attendees must be a list of dictionaries, "
            f"got {type(attendees).__name__}."
        )
        return

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = [
        "name",
        "event_title",
        "event_date",
        "event_location"
    ]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + placeholder + "}",
                str(value)
            )

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except OSError as error:
            print(f"Error writing {filename}: {error}")
