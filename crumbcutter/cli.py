import logging

import click

import crumbcutter


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("username_gistname_pair", metavar="<username>/<gist_description>")
@click.option(
    "-o",
    "--output-dir",
    default=".",
    type=click.Path(),
    show_default=True,
    help="Directory where the rendered file will be saved.",
)
@click.option("--no-input", is_flag=True, help="Do not prompt for user input, use default values.")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Provide more verbose output for debugging purposes.",
)
@click.version_option(version="1.0.0", prog_name="crumbcutter")
def cli(username_gistname_pair: str, output_dir: str, no_input: bool, verbose: bool):
    """
    crumbcutter: template a single-file GitHub gist

    This tool is intended for single-file Gist templates.
    If you need to template more than one file, cookiecutter
    should be used instead.

    Given a GitHub username and gist description (functioning as
    the "name" of the gist), crumbcutter fetches the gist,
    prompts for required inputs, and renders the template.
    The rendered file is then saved to a specified directory
    or current working directory if no directory is specified.

    Example Usage:

        crumbcutter <username>/<gist_description>
        crumbcutter octocat/index-html
    """
    if verbose:
        click.echo("Running in verbose mode...")
        logging.basicConfig(level=logging.DEBUG)
    try:
        crumbcutter.main(username_gistname_pair, output_dir, no_input)
    except ValueError:
        click.echo("Invalid format for <username>/<gist_description>.")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if verbose:
            logging.exception("Detailed error:")


if __name__ == "__main__":
    cli()
