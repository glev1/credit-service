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
@click.option("--tsize", default=0.1, help="Test Size")
def retrain(tsize):
    """Retrain Model
    You may want to extend this with more options, such as setting model_name
    """

    click.echo(click.style("Retraining Model", bg="green", fg="black"))
    score = mlib.retrain()
    click.echo(
        click.style(f"Retrained Model Score: {score}", bg="blue", fg="black"))

@cli.command("predict")
@click.option("--host", default="http://localhost:8080/predict", help="Host to query")
def mkrequest(host):
    """Sends prediction to ML Endpoint"""
    
    click.echo(click.style(f"Querying host {host}",bg="green", fg="black"))
    
    f = open('cli_fts.json')
    payload = json.load(f)
    f.close

    result = requests.post(url=host, json=payload)
    click.echo(click.style(f"{result}", bg="red", fg="black"))


if __name__ == "__main__":
    cli()