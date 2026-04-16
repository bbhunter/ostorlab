from ostorlab.agent.message.proto.v3.report.ticket import (
    ticket_pb2,
)


def testMessage_whenCreateWithValidData_shouldSerializeAndDeserializeCorrectly():
    msg = ticket_pb2.Message()
    msg.ticket_id = "TICKET-123"
    msg.title = "New Vulnerability Found"
    msg.description = "A new critical vulnerability was detected."
    msg.assigned_user = "user-01"

    tag1 = msg.tags.add()
    tag1.name = "priority"
    tag1.value = "high"

    tag2 = msg.tags.add()
    tag2.name = "source"
    tag2.value = "agent-01"

    serialized = msg.SerializeToString()
    deserialized_msg = ticket_pb2.Message()
    deserialized_msg.ParseFromString(serialized)

    assert deserialized_msg.ticket_id == "TICKET-123"
    assert deserialized_msg.title == "New Vulnerability Found"
    assert deserialized_msg.description == "A new critical vulnerability was detected."
    assert deserialized_msg.assigned_user == "user-01"
    assert len(deserialized_msg.tags) == 2
    assert deserialized_msg.tags[0].name == "priority"
    assert deserialized_msg.tags[0].value == "high"
    assert deserialized_msg.tags[1].name == "source"
    assert deserialized_msg.tags[1].value == "agent-01"


def testMessage_whenCreateEmpty_shouldHaveDefaultValues():
    msg = ticket_pb2.Message()

    assert msg.ticket_id == ""
    assert msg.title == ""
    assert msg.description == ""
    assert len(msg.tags) == 0
    assert msg.assigned_user == ""


def testTag_whenCreateWithDefaults_shouldHaveCorrectDefaults():
    tag = ticket_pb2.Tag()
    tag.name = "test_name"

    assert tag.name == "test_name"
    assert tag.value == ""
