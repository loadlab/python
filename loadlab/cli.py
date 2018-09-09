# -*- coding: utf-8 -*-

"""Console script for loadlab."""
import sys
import click
from loadlab import LoadLab


@click.group()
def main():
    return 0


@click.command()
def jobs():
    click.echo(LoadLab().jobs.get())


@click.command()
def plans():
    click.echo(LoadLab().plans.get())


@click.command()
def sites():
    click.echo(LoadLab().sites.get())


main.add_command(jobs)
main.add_command(plans)
main.add_command(sites)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
