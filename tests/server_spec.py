import unittest
from unittest.mock import patch, MagicMock
import src.server as service
import threading
import mock 
class TestUDPServer(unittest.TestCase):

    @patch('socket.socket')
    def test_server_functionality(self, mock_socket):
        # Prepare mock data to be received
        mock_received_data = b'Sensor1,2023-01-01 00:00:00,25.5'
        mock_sender_address = ('127.0.0.1', 8080)

        # Mocking the socket's recvfrom method
        mock_socket = mock.Mock()
        mock_socket.recvfrom.return_value = (mock_received_data, mock_sender_address)

        # Mocking file operations
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            # Start the server in a separate thread
            server_thread = threading.Thread(target=service.server, daemon=True)
            server_thread.start()

            # Give the server time to process
            threading.Event().wait(1)

            # Check if recvfrom was called
            mock_socket.recvfrom.assert_called_with(1024)

            # Check if the file operation was performed
            mock_file.assert_called_with('Sensor1_log.txt', 'a')

            # Cleanup: stopping the server thread
            server_thread.join(timeout=2)
            self.assertFalse(server_thread.is_alive())

if __name__ == '__main__':
    unittest.main()
