import click
from authentication import get_auth,get_db

#
@cli.command()
def book_session():
    email = click.prompt("Enter your email", type=str)
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

    # Save to Firestore
    booking_data = {
        "mentee_email": email,
        "mentor_email": mentor_email,
        "session_time": session_time,
        "status": "pending"
    }
    db.collection("bookings").add(booking_data)
    
    click.echo(f"Session booked with {mentor_email} at {session_time}")
