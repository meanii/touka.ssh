"""This module provides the touke.ssh cli"""
# touka/cli.py

import os
from pathlib import Path
from typing import List, Optional

import typer

from touka.callbacks.version import _version_callback
from touka.callbacks.add import _add_callback
from touka.callbacks.connect import _connect_callback

from touka import __app_name__, __version__, database
from touka.utils.validations import check_ip
from touka import DEFAULT_ROOT_DIR_PATH

app = typer.Typer(
    name=f"{__app_name__} - (v{__version__})",
    help="Awesome ssh manager, especially made for anii ☂️",
)

db = database.DatabaseHandler()


@app.command()
def init() -> None:
    """assign pub key to your IP machine"""
    os.system(f'ssh-keygen -t rsa -q')


@app.command()
def add(
    name: str = typer.Option(
        None,
        "--name",
        "-n",
        help="The server's nickname, which you may use to connect to it directly.",
    ),
    port: int = typer.Option(22, "--port", "-p", help="The server's ssh port."),
    address: str = typer.Option(
        None, "--address", "-a", help="This is the correct IP address of the server."
    ),
    description: str = typer.Option(
        None,
        "--description",
        "-d",
        help="You may give a description when adding a server, which will help you remember which server it is.",
    ),
) -> None:

    """Add a new ssh connection with a description."""

    if not (name):
        typer.secho("Give the ssh server nick name, please!", fg=typer.colors.RED)
        raise typer.Exit()
    if not (address):
        typer.secho("Please provide ssh address!", fg=typer.colors.RED)
        raise typer.Exit()
    if not (check_ip(address)):
        typer.secho(
            "The IP address that you provided is incorrect.", fg=typer.colors.RED
        )
        raise typer.Exit()
    if db.get_address(name):
        typer.secho(
            "This nickname is already in your collection; the new name should be unique.",
            fg=typer.colors.RED,
        )
        raise typer.Exit()
    if db.get_name(address):
        typer.secho(
            "This address is already in your database; the new address should be distinct.",
            fg=typer.colors.RED,
        )
        raise typer.Exit()

    _add_callback(port, address, description, name)


@app.command()
def connect(
    name: str = typer.Option(
        None,
        "--name",
        "-n",
        help="The server's nickname, which you saved!",
    )
) -> None:
    """connect to server via name"""
    if not name:
        typer.secho(
            "To connect, please provide the server's nickname!", fg=typer.colors.RED
        )
        raise typer.Exit()

    address = db.get_address(name)
    if not address:
        typer.secho(
            "You don't have this server in your collection!", fg=typer.colors.RED
        )
        raise typer.Exit()
    typer.secho(f"connecting to the {address}...", fg=typer.colors.GREEN)
    _connect_callback(address)


@app.command()
def list() -> None:
    """list of all saved servers."""
    servers = db.get_all()
    if len(servers) == 0:
        typer.secho("There are currently no servers saved!", fg=typer.colors.RED)
        raise typer.Exit()
    typer.secho("\nServers you have saved:\n", fg=typer.colors.BLUE, bold=True)
    columns = ("ID.  ", "| Name  ", "| Address  ", "| Port  ", "| Description  ")
    headers = "".join(columns)
    typer.secho(headers, fg=typer.colors.BLUE, bold=True)
    typer.secho("-" * len(headers), fg=typer.colors.BLUE)
    for id, server in enumerate(servers, 1):
        port, address, description, name = server.values()
        typer.secho(
            f"{id}{(len(columns[0]) - len(str(id))) * ' '}"
            f"| {name}{(len(columns[1]) - len(str(name)) - 4) * ' '} "
            f"| {address}{(len(columns[2]) - len(str(address)) - 2) * ' '} "
            f"| {port} "
            f"| {description} ",
            fg=typer.colors.BLUE,
        )
    typer.secho("-" * len(headers) + "\n", fg=typer.colors.BLUE)


@app.command()
def purge(
    name: str = typer.Option(
        None,
        "--name",
        "-n",
        help="name of the saved server, you can get via touka.shh list",
    ),
    all: bool = typer.Option(
        False,
        "--all",
        "-a",
        help="purge every stored server.",
    ),
) -> None:
    """purge your stored servers."""

    if all:
        can_delete = typer.confirm(
            "Do you really want to remove ALL of your saved servers?", abort=True
        )
        if not can_delete:
            typer.secho(
                "aborted!", fg=typer.colors.GREEN
            )
            raise typer.Exit()
        db.purge_all()
        typer.secho(
            "deleted all of your saved servers successfully!", fg=typer.colors.GREEN
        )
        raise typer.Exit()

    db.purge(name)
    typer.secho(f"{name} deleted!", fg=typer.colors.GREEN)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
