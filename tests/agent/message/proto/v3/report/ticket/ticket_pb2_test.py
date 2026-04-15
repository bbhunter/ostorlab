from ostorlab.agent.message.proto.v3.report.ticket import (
    ticket_pb2,
)


def testMessage_whenCreateWithValidData_shouldSerializeAndDeserializeCorrectly():
    msg = ticket_pb2.Message()
    msg.ticket_id = "TICKET-123"
    msg.title = "New Vulnerability Found"
    msg.description = "A new critical vulnerability was detected."
    msg.stack_trace = "Traceback..."
    msg.global_tags.extend(["security", "critical"])

    metadata_1 = msg.metadata.add()
    metadata_1.key = "priority"
    metadata_1.value = "high"

    metadata_2 = msg.metadata.add()
    metadata_2.key = "agent"
    metadata_2.value = "agent-01"

    serialized = msg.SerializeToString()
    deserialized_msg = ticket_pb2.Message()
    deserialized_msg.ParseFromString(serialized)

    assert deserialized_msg.ticket_id == "TICKET-123"
    assert deserialized_msg.title == "New Vulnerability Found"
    assert deserialized_msg.description == "A new critical vulnerability was detected."
    assert deserialized_msg.stack_trace == "Traceback..."
    assert list(deserialized_msg.global_tags) == ["security", "critical"]
    assert len(deserialized_msg.metadata) == 2
    assert deserialized_msg.metadata[0].key == "priority"
    assert deserialized_msg.metadata[0].value == "high"
    assert deserialized_msg.metadata[1].key == "agent"
    assert deserialized_msg.metadata[1].value == "agent-01"


def testMessage_whenCreateEmpty_shouldHaveDefaultValues():
    msg = ticket_pb2.Message()

    assert msg.ticket_id == ""
    assert msg.title == ""
    assert msg.description == ""
    assert msg.stack_trace == ""
    assert len(msg.global_tags) == 0
    assert len(msg.metadata) == 0


def testMetadata_whenCreateWithDefaults_shouldHaveCorrectDefaults():
    metadata = ticket_pb2.Metadata()
    metadata.key = "test_key"

    assert metadata.key == "test_key"
    assert metadata.value == ""
