import unittest

from fastapi.testclient import TestClient
from mongoengine import connect, disconnect
from src.api import app

client = TestClient(app)
client.headers["Content-Type"] = "application/json"


class ConnectionTestClass:

    class ConnectionTest(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            connect('mongoenginetest', host='mongomock://localhost')

        @classmethod
        def tearDownClass(cls):
            disconnect()
