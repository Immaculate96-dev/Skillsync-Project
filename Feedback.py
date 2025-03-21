from firebase_config import db
import click

@click.command()
@click.option("--meeting_id", "-m", type=str, required=True, help="ID of the meeting")
@click.option("--mentor_id", "-t", type=str, required=True, help="ID of the mentor being reviewed")
@click.option("--mentee_id", "-e", type=str, required=True, help="ID of the mentee leaving feedback")
@click.option("--rating", "-r", type=int, required=True, help="Rating from 1 to 5")
@click.option("--comment", "-c", type=str, help="Optional comment")
def submit_feedback(meeting_id, mentor_id, mentee_id, rating, comment):
    #Submit feedback for a mentor after a session

    if rating < 1 or rating > 5:
        click.echo("Invalid rating! Please provide a score between 1 and 5.")
        return

    feedback_data = {
        "mentor_id": mentor_id,
        "mentee_id": mentee_id,
        "rating": rating,
        "comment": comment or ""
    }

    db.child("feedback").child(meeting_id).set(feedback_data)
    
    click.echo("Feedback submitted successfully!")

if __name__ == "__main__":
    submit_feedback()
