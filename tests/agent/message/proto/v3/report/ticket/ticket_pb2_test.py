from ostorlab.agent.message.proto.v3.report.ticket import (
    ticket_pb2,
)


def testMessage_whenCreateWithValidData_shouldSerializeAndDeserializeCorrectly():
    msg = ticket_pb2.Message()
    msg.ticket_id = "TICKET-123"
    msg.title = "New Vulnerability Found"
    msg.description = "A new critical vulnerability was detected."
    msg.global_tags.extend(["security", "critical"])
    msg.assigned_user = "user-01"

    serialized = msg.SerializeToString()
    deserialized_msg = ticket_pb2.Message()
    deserialized_msg.ParseFromString(serialized)

    assert deserialized_msg.ticket_id == "TICKET-123"
    assert deserialized_msg.title == "New Vulnerability Found"
    assert deserialized_msg.description == "A new critical vulnerability was detected."
    assert list(deserialized_msg.global_tags) == ["security", "critical"]
    assert deserialized_msg.assigned_user == "user-01"


def testMessage_whenCreateEmpty_shouldHaveDefaultValues():
    msg = ticket_pb2.Message()

    assert msg.ticket_id == ""
    assert msg.title == ""
    assert msg.description == ""
    assert len(msg.global_tags) == 0
    assert msg.assigned_user == ""
