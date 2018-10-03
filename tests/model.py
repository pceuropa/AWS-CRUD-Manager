from telemetry.workers.gateway import Gateway
from telemetry.tests.mocking import MockData
from telemetry.models.snapshot import Snapshots
import unittest


class TestModel(unittest.TestCase):
    """Tests models/shema"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_snapshots(self):
        count = Snapshots().count()
        self.assertEqual(count, 2)
