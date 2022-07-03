import os
import typer
from touka import DEFAULT_ROOT_DIR_PATH, database


def _add_callback(port: int, address: str, description: str, name: str) -> None:
    try:
        os.system(f"ssh-keygen -R {address} -q")
        os.system(
            f'ssh-copy-id -f root@{address}'
        )
        db = database.DatabaseHandler()
        db.save(
            {"port": port, "address": address, "description": description, "name": name}
        )
        typer.secho(
            f'There is a new server now! Access is available via ( touka connect --name {name} )',
            fg=typer.colors.GREEN
        )
    except KeyboardInterrupt:
        typer.secho("coudn't save the server!", pg=typer.colors.RED)