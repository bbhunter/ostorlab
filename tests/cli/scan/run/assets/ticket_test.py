"""Tests for scan run ticket command."""

from click.testing import CliRunner
from pytest_mock import plugin

from ostorlab.cli import rootcli
from ostorlab.agent import definitions as agent_definitions
from ostorlab.assets import ticket


def testScanRunTicket_whenValidArgumentsAreProvided_callScanWithValidSettings(
    mocker: plugin.MockerFixture,
    nmap_agent_definition: agent_definitions.AgentDefinition,
) -> None:
    """Test oxo scan run ticket command with valid arguments."""
    runner = CliRunner()
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.__init__", return_value=None)
    mocker.patch("ostorlab.runtimes.local.LocalRuntime.can_run", return_value=True)
    mocker.patch(
        "ostorlab.cli.agent_fetcher.get_definition",
        return_value=nmap_agent_definition,
    )
    scan_mocked = mocker.patch(
        "ostorlab.runtimes.local.LocalRuntime.scan", return_value=True
    )

    runner.invoke(
        rootcli.rootcli,
        [
            "scan",
            "run",
            "--agent=agent1",
            "ticket",
            "--title=Sample Ticket",
            "--ticket-id=TCK-123",
            "--description=A sample ticket description",
            "--tag=priority:high",
            "--tag=type:bug",
            "--assigned-user=user@example.com",
        ],
    )

    assert scan_mocked.call_count == 1
    assets = scan_mocked.call_args[1].get("assets")
    assert len(assets) == 1
    asset = assets[0]
    assert isinstance(asset, ticket.Ticket)
    assert asset.title == "Sample Ticket"
    assert asset.ticket_id == "TCK-123"
    assert asset.description == "A sample ticket description"
    assert len(asset.tags) == 2
    assert asset.tags[0].name == "priority"
    assert asset.tags[0].value == "high"
    assert asset.tags[1].name == "type"
    assert asset.tags[1].value == "bug"
    assert asset.assigned_user == "user@example.com"
