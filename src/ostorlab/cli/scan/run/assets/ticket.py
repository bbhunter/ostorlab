"""Asset of type ticket for scanning."""

import logging
from typing import Optional, List, Tuple

import click

from ostorlab.assets import ticket as ticket_asset
from ostorlab.cli.scan.run import run
from ostorlab import exceptions
from ostorlab.cli import console as cli_console

console = cli_console.Console()
logger = logging.getLogger(__name__)


@run.run.command()
@click.option("--title", help="Ticket title.", required=True)
@click.option("--ticket-id", help="Ticket ID.", required=False)
@click.option("--description", help="Ticket description.", required=False)
@click.option(
    "--tag",
    "tags",
    help="Ticket tags in the format name:value.",
    required=False,
    multiple=True,
)
@click.option("--assigned-user", help="Assigned user.", required=False)
@click.pass_context
def ticket(
    ctx: click.core.Context,
    title: str,
    ticket_id: Optional[str] = None,
    description: Optional[str] = None,
    tags: Optional[List[str]] = None,
    assigned_user: Optional[str] = None,
) -> None:
    """Run scan for ticket."""
    runtime = ctx.obj["runtime"]
    parsed_tags = []
    if tags:
        for tag in tags:
            if ":" in tag:
                name, value = tag.split(":", 1)
                parsed_tags.append(ticket_asset.Tag(name=name, value=value))
            else:
                parsed_tags.append(ticket_asset.Tag(name=tag))

    asset = ticket_asset.Ticket(
        title=title,
        ticket_id=ticket_id,
        description=description,
        tags=parsed_tags,
        assigned_user=assigned_user,
    )
    logger.debug("scanning asset %s", asset)
    try:
        runtime.scan(
            title=ctx.obj["title"],
            agent_group_definition=ctx.obj["agent_group_definition"],
            assets=[asset],
        )
    except exceptions.OstorlabError as e:
        console.error(f"An error was encountered while running the scan: {e}")
