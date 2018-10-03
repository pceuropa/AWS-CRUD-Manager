from datetime import datetime

pixel_array_left = [18.25, 18.5, 24, 30.5, 29, 24.75, 26.25, 21, 26.25, 10.75, 16, 29, 34.75, 33, 41.75, 25.25, 13.75, 10, 17.5, 29.5, 18, 24.5, 21.5, 21.75, 10.75, 11.25, 25.75, 47.75, 39.5, 44.25, 46.25, 28.25, 11.75, 11, 16.25, 37.5, 41.25, 42.25, 42.5, 21, 11, 12, 20.25, 14.5, 15.75, 16.75, 15.5, 13.25, 11.75, 11, 16.5, 16.5, 13.75, 13.5, 13.75, 13.75, 11.75, 11, 11, 20.5, 15, 13.75, 13.75, 12.5]

pixel_array_right = [17.25, 20.5, 20.25, 17.75, 20.25, 22.75, 21.75, 24.25, 25.5, 30.5, 25.25, 26.5, 22.5, 24.75, 31.25, 22.5, 28.5, 21.5, 42.5, 47, 36.25, 22, 31.75, 25.25, 24, 30.25, 43, 37.5, 43.25, 15.5, 11.5, 10, 12.5, 30.5, 38.25, 34.5, 40.25, 35, 12.75, 11.75, 14, 42.25, 48, 42.75, 49.25, 51.25, 15.75, 11.25, 12.25, 33.25, 39.25, 34,
        36.75, 31.75, 13.75, 11, 11.75, 13.75, 19.75, 21, 20.5, 12.5, 11.715, 11]


class MockData(object):
    """Docstring for MockGateway. """
    id = 1
    rssi = -96
    datetime = '2018-07-24T12:00:51+01:00'
    status = 63
    internaltemp = 23
    thermal_sensors = [
        {' sensorId': 'TH1', 'internalTemp': 23.25, 'pixelArray': pixel_array_left},
        {'sensorId': 'TH2', 'internalTemp': 23.25, 'pixelArray': pixel_array_right}
    ]
    snapshots = []

    def __init__(self, params):

        self.deviceId = f'{self.id:0>1}'
        self.datetime = datetime.now()
        self.lat = 53.073803
        self.lon = 23.164168
        self.status = self.set_status(params['charge'], params['status_w'], params['tv'])

        self.snapshots = {
            "deviceId": f'{self.id:0>15}',
            "datetime": datetime.now(),
            "lat": 53.073803,
            "lon": 23.164168,
            "status": self.status,
            "snapshots": [{
                'datetime': datetime.now(),
                'thermalSensors': self.thermal_sensors,
                'wristBands': [
                    self.wristband(params['wristband']),
                    self.wristband(params['wristband'])
                ],
            }]
        }

    def set_status(self, charge: int=0, wristbands=[5, 4, 3, 2, 1], tv: int=0) -> int:
        """TODO: Set status gateway
        :returns: int """

        status = ''.join((str(x) for x in [charge] + wristbands + [tv]))
        return int(status, 2)

    def wristband(self, data) -> dict:
        """Set dict data of wristband
        :returns: dict """

        wristband_data={'wristBandId': 'BB:BB:BB:BB:01', 'rssi': -38, 'voltage': 4.23, 'status': 3}

        if data['status'] is not None:
            wristband_data['status']= int(''.join((str(x) for x in data['status'])), 2)

        if data['id'] is not None:
            wristband_data['wristBandId'] = f'BB:BB:BB:{self.id:0>2}:{data["id"]:0>2}'
        return wristband_data

    def get(self):
        return self.snapshots

    def get_wristband(self, config={}):
        params = {
            'wristband_id': f'BB:BB:BB:{self.id:0>2}:{self.id:0>2}',
            'status': 0,
            'charge': 0,
            'battery': 1
        }
        params.update(config)
        return params
