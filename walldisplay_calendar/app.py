"""
default app creation
"""
import walldisplay_calendar
from walldisplay_calendar import environment

environment.setup_logging()

app = walldisplay_calendar.create_app()

if __name__ == "__main__":
    app.run(host="::", port="33333")
