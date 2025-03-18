import os
import datetime
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Yet to install google-auth
# Load credentials from the JSON file
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CREDS = service_account.Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

# Initialize Google Calendar API
service = build("calendar", "v3", credentials=CREDS)

def list_events():
    """Lists upcoming events from Google Calendar."""
    now = datetime.datetime.utcnow().isoformat() + "Z"
    events_result = service.events().list(
        calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy="startTime"
    ).execute()
    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
    else:
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(f"{start}: {event['summary']}")

def create_event(Mentorship_Session, start_time, end_time):
    #Creates a new event in Google Calendar
    event = {
        "summary": Mentorship_Session,
        "start": {"dateTime": start_time, "timeZone": "UTC"},
        "end": {"dateTime": end_time, "timeZone": "UTC"},
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(f"Event created: {event.get('htmlLink')}")

if __name__ == "__main__":
    list_events()
    # Example: create_event("Mentorship Session", "2025-03-15T10:00:00", "2025-03-15T11:00:00")