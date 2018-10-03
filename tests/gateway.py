from telemetry.workers.gateway import Gateway
from telemetry.tests.mocking import MockData
import unittest


mock = MockData({"id": 1, "tv": 1, "status_w": [0, 0, 0, 0, 1], 'charge': 1, 'wristband': {"status": [1, 1, 1], 'id': 1}})
snapshot = mock.get()


class TestGateway(unittest.TestCase):
    gateway = Gateway(snapshot)
    gateway.run()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_tv(self):
        self.assertTrue(self.gateway.tv)

    def test_status(self):
        self.assertEqual(self.gateway.status, [1, 1, 0, 0, 0, 0, 1])
        self.assertEqual(self.gateway.get_status(0, -1), 0)
        self.assertEqual(self.gateway.get_status(1, -1), 1)
        self.assertEqual(self.gateway.get_status(2, -2), 1)
        self.assertEqual(self.gateway.get_status(3, -2), 1)
        self.assertEqual(self.gateway.get_status(4, -2), 0)
        self.assertEqual(self.gateway.get_status(4, -2), 0)

    def test_active(self):
        self.assertTrue(self.gateway.isBandActive(mock.get_wristband({'status': 1, 'charge': 0, })))
        self.assertFalse(self.gateway.isBandActive(mock.get_wristband({'status': 1, 'charge': 1, })))
        self.assertFalse(self.gateway.isBandActive(mock.get_wristband({'status': 0, 'charge': 1, })))
        self.assertFalse(self.gateway.isBandActive(mock.get_wristband({'status': 0, 'charge': 0, })))

    def test_tv_off(self):
        mock = MockData({"id": 2, "tv": 0, "status_w": [1, 1, 1, 1, 1], 'charge': 0, 'wristband': {"status": [0, 0, 1], 'id': 2}})
        snapshot = mock.get()
        gateway = Gateway(snapshot)
        gateway.run()

        self.assertEqual(gateway.status, [0, 1, 1, 1, 1, 1, 0])
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 1, 'charge': 0, })))
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 1, 'charge': 1, })))
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 0, 'charge': 1, })))
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 0, 'charge': 0, })))

    def test_nothing_in_area(self):
        mock = MockData({"id": 2, "tv": 1, "status_w": [0, 0, 0, 0, 0], 'charge': 0, 'wristband': {"status": [0, 0, 1], 'id': 2}})
        snapshot = mock.get()
        gateway = Gateway(snapshot)
        gateway.run()

        self.assertEqual(gateway.status, [1, 0, 0, 0, 0, 0, 0])
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 1, 'charge': 0, })))
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 1, 'charge': 1, })))
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 0, 'charge': 1, })))
        self.assertFalse(gateway.isBandActive(mock.get_wristband({'status': 0, 'charge': 0, })))
