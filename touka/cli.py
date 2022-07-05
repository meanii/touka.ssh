"""This module provides the touke.ssh cli"""
# touka/cli.py

import os
import typer

from pathlib import Path
from typing import List, Optional
from prettytable import PrettyTable


from touka.callbacks.version import _version_callback
from touka.callbacks.add import _add_callback
from touka.callbacks.connect import _connect_callback

from touka import __app_name__, __version__, __about__
from touka.database.touka import ToukaDatabase

from touka.utils.validations import check_ip
from touka.utils.ping import ping

from touka import DEFAULT_ROOT_DIR_PATH

app = typer.Typer(
    name=f"{__app_name__} - (v{__version__})",
    help=__about__,
)

db = ToukaDatabase()


@app.command()
def init() -> None:
    """assign pub key to your IP machine"""
    os.system(f"ssh-keygen -t rsa -q")


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
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="If the ssh key has been withdrawn from the server, force a reconnect!",
    ),
    id: str = typer.Option(
        None,
        "--id",
        help="You may get the server's ID that Touka saved by going to: touka list.",
    ),
    name: str = typer.Option(
        None,
        "--name",
        "-n",
        help="The server's nickname, which you saved!",
    ),
) -> None:
    """connect to server via name"""
    if not name and not id:
        typer.secho(
            "To connect, please provide the server's nickname or ID!",
            fg=typer.colors.RED,
        )
        raise typer.Exit()

    if name:
        address = db.get_address(name=name)
    if id:
        address = db.get_address(id=id)
    if not address:
        typer.secho(
            "You don't have this server in your collection!", fg=typer.colors.RED
        )
        raise typer.Exit()
    if force:
        typer.secho(f"reforcing to connect to the f{address}...", fg=typer.colors.GREEN)
    typer.secho(f"connecting to the {address}...", fg=typer.colors.GREEN)
    _connect_callback(address, force)


@app.command()
def list(
    status: bool = typer.Option(
        False,
        "--status",
        "-s",
        help="Ping all servers and display the results in a list.",
    )
) -> None:
    """list of all saved servers."""
    table = PrettyTable()
    servers = db.get_all()
    if len(servers) == 0:
        typer.secho("There are currently no servers saved!", fg=typer.colors.RED)
        raise typer.Exit()
    if status:
        table.field_names = ["ID", "Name", "Address", "Port", "Description", "Status"]
        typer.secho("pinging...")
    else:
        table.field_names = ["ID", "Name", "Address", "Port", "Description"]
    for id, server in enumerate(servers, 1):
        port, address, description, name = server.values()
        if status:
            status_result = "✅" if ping(address) else "❌"
            table.add_row([id, name, address, port, description, status_result])
        else:
            table.add_row([id, name, address, port, description])
    typer.secho("\nServers you have saved:\n", fg=typer.colors.BLUE, bold=True)
    typer.secho(table, fg=typer.colors.BLUE)


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
            typer.secho("aborted!", fg=typer.colors.GREEN)
            raise typer.Exit()
        db.purge_all()
        typer.secho(
            "deleted all of your saved servers successfully!", fg=typer.colors.GREEN
        )
        raise typer.Exit()
    if not name:
        typer.secho(
            "To delete it, kindly specify the server name!", fg=typer.colors.RED
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
