#!/usr/bin/env python
import json
import click
from src.main.mlib import predict

@click.command()
@click.option(
    "--profile",
    default="profile.json",
    prompt="Borrower Profile",
    help="Pass in the file with profile to predict defaulting probability",
)
def predictcli(profile):
    """Predicts chance of defaulting based on profile"""
    f = open(profile)
    payload = json.load(f)
    f.close

    result = predict(payload)
    pred = result["predict"]
    human_readable = str(result["human_readable_predict"])
    if pred > 0.5 :
        click.echo(click.style(human_readable, bg="red", fg="black"))
    else:
        click.echo(click.style(human_readable, bg="green", fg="black"))


if __name__ == "__main__":
    predictcli()
