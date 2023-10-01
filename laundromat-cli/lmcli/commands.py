import typer
from datetime import datetime
import tzlocal

def hello_cmd(name: str):
  typer.echo(f"Hello {name}!")

def time_cmd():
  tz = tzlocal.get_localzone()
  tz_name = tz.tzname(datetime.now(tz))
  typer.echo(f"Current time in {tz_name}: {datetime.now(tz).strftime('%H:%M:%S')}")