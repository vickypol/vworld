import unittest
import requests
import threading
import time

from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.server_thread = threading.Thread(target=app.run, kwargs={'port': 3000, 'host': '127.0.0.1'})
        self.server_thread.daemon = True
        self.server_thread.start()
        time.sleep(1)  # Give the server some time to start

    def tearDown(self):
        requests.get('http://127.0.0.1:3000/shutdown')  # Shutdown the Flask server

    def test_hello_with_name(self):
        response = requests.get('http://127.0.0.1:3000/?name=Itamar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello Itamar')

    def test_hello_without_name(self):
        response = requests.get('http://127.0.0.1:3000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello World')

if __name__ == '__main__':
    unittest.main()
