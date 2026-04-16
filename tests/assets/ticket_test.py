"""Unit tests for Ticket asset."""

from ostorlab.agent.message import serializer
from ostorlab.assets import ticket


def testTicketToProto_whenValidData_generatesProto():
    asset = ticket.Ticket(
        title="Sample Ticket",
        ticket_id="TCK-123",
        description="A sample ticket description",
        tags=[
            ticket.Tag(name="priority", value="high"),
            ticket.Tag(name="type", value="bug"),
        ],
        assigned_user="user@example.com",
    )
    raw = asset.to_proto()

    assert isinstance(raw, bytes)
    unraw = serializer.deserialize("v3.report.ticket", raw)
    assert unraw.title == "Sample Ticket"
    assert unraw.ticket_id == "TCK-123"
    assert unraw.description == "A sample ticket description"
    assert unraw.tags[0].name == "priority"
    assert unraw.tags[0].value == "high"
    assert unraw.tags[1].name == "type"
    assert unraw.tags[1].value == "bug"
    assert unraw.assigned_user == "user@example.com"
