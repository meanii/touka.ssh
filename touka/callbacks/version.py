import typer
from touka import __app_name__, __about__, __source__, __author__, __version__


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(
            (
                f"{__app_name__} v{__version__} - {__about__}\n"
                f"Author - {__author__}\n\n"
                f"feel free to contribute - {__source__}\n"
            )
        )
        raise typer.Exit()
