import click
from authentication import get_auth,get_db
from calendar import create_event


@cli.command()
def book_session(mentor_email,mentee_email,date,time):
    mentee_email = click.prompt("Enter your email", type=str)
    user_ref = db.collection("users").where("email", "==", email).get()

    if not user_ref:
        click.echo("User not found.")
        return

    user = user_ref[0].to_dict()
    if user["role"] != "mentee":
        click.echo("Only mentees can book sessions.")
        return

    mentor_email = click.prompt("Enter mentor's email", type=str)
    session_time = click.prompt("Enter session time (YYYY-MM-DD HH:MM)", type=str)

    session_data = {
        "mentee" : mentee_email,
        "mentor" : mentor_email,
        "date"   : date,
        "time"   : time,
        "status" : "booked"/"completed"/"cancelled" # Yet to figure this out
            }
    db.child("booked sessions").push(session_data) # For real time database 
    click.echo("Session booked successfully")
    
    booking_data = {
        "mentee_email": mentee_email,
        "mentor_email": mentor_email,
        "session_time": session_time,
        "status": "pending" 
    }
    db.collection("bookings").add(booking_data)

    # Not quite sure about this feature
    mentor_email = "mentor@email.com"
    start_time = "2025-03-15T14:00:00" # Yet to modify this based on the project requirements
    end_time = "2025-03-15T15:00:00"

    create_event(f"Session with {mentor_email}", start_time, end_time)
    
    click.echo(f"Session booked with {mentor_email} at {session_time}")
