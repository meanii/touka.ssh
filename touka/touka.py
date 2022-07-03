"""touka.ssh entry point script."""
# touka/__main__.py

from touka import __app_name__, cli

def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()