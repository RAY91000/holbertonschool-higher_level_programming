import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Invalid input: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Invalid input: attendees must be a list of dictionaries.")
        return

    # Check for empty template or empty attendee list
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and generate an invitation file
    for idx, attendee in enumerate(attendees, start=1):
        # Start with the original template
        invitation = template
        # Replace placeholders with actual data or "N/A" if missing/None
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace("{" + key + "}", str(value))
        
        # Define the output filename
        output_filename = f"output_{idx}.txt"
        
        # Check if file exists; if it does, log an error and skip creation
        try:
            if os.path.exists(output_filename):
                print(f"Error: File {output_filename} already exists. Skipping creation.")
            else:
                with open(output_filename, 'w') as outfile:
                    outfile.write(invitation)
                print(f"Generated {output_filename}")
        except Exception as e:
            print(f"An error occurred while writing to {output_filename}: {e}")

# Example usage:
if __name__ == "__main__":
    # Read the template from a file named 'template.txt'
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except Exception as e:
        print(f"Error reading template file: {e}")
        template_content = ""
    
    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    
    # Generate the invitation files
    generate_invitations(template_content, attendees)
