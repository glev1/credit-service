#!/usr/bin/env python
import click
import src.main.mlib as mlib
import requests
import json

@click.group()
@click.version_option("1.0")
def cli():
    """Machine Learning Utility Belt"""


@cli.command("retrain")
def retrain():
    """Retrain Model
    """

    click.echo(click.style("Retraining Model", bg="green", fg="black"))
    score = mlib.retrain()
    click.echo(
        click.style(f"Retrained Model Score: {score}", bg="blue", fg="black"))

@cli.command("predict")
@click.option("--profile", default="profile.json", help="File with profile")
@click.option("--host", default="http://localhost:8080/predict", help="Host to query")
def mkrequest(profile, host):
    """Sends prediction to ML Endpoint"""
    
    click.echo(click.style(f"Querying host {host}",bg="green", fg="black"))
    
    f = open(profile)
    payload = json.load(f)
    f.close

    result = requests.post(url=host, json=payload)

    click.echo(click.style(result.text,
         bg="green", fg="black"))
  
if __name__ == "__main__":
    cli()