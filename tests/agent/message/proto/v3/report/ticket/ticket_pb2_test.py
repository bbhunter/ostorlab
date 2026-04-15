import unittest
from src.ostorlab.agent.message.proto.v3.report.ticket import ticket_pb2


class TestTicketPB2(unittest.TestCase):
    def testTicketMessage_whenSerialized_shouldDeserializeCorrectly(self):
        """Test that ticket message serializes and deserializes correctly."""
        ticket_message = ticket_pb2.Message()
        ticket_message.ticket_id = "TICKET-123"
        ticket_message.title = "New Vulnerability Found"
        ticket_message.description = "A new critical vulnerability was detected."
        ticket_message.stack_trace = "Traceback..."
        ticket_message.global_tags.extend(["security", "critical"])

        metadata_1 = ticket_message.metadata.add()
        metadata_1.key = "priority"
        metadata_1.value = "high"

        metadata_2 = ticket_message.metadata.add()
        metadata_2.key = "agent"
        metadata_2.value = "agent-01"

        serialized = ticket_message.SerializeToString()
        deserialized = ticket_pb2.Message()
        deserialized.ParseFromString(serialized)

        self.assertEqual(deserialized.ticket_id, "TICKET-123")
        self.assertEqual(deserialized.title, "New Vulnerability Found")
        self.assertEqual(
            deserialized.description, "A new critical vulnerability was detected."
        )
        self.assertEqual(deserialized.stack_trace, "Traceback...")
        self.assertEqual(list(deserialized.global_tags), ["security", "critical"])
        self.assertEqual(len(deserialized.metadata), 2)
        self.assertEqual(deserialized.metadata[0].key, "priority")
        self.assertEqual(deserialized.metadata[0].value, "high")
        self.assertEqual(deserialized.metadata[1].key, "agent")
        self.assertEqual(deserialized.metadata[1].value, "agent-01")
