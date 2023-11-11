import unittest
import socket
# Test case for socket client
class TestSocketClient(unittest.TestCase):
    def test_connection_to_server(self):
        # Attempt to connect to the test server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("localhost", 12345))
            # If no exception is raised, the connection is successful
            self.assertTrue(True)

# Running the test
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
