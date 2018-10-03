from iso8601 import parse_date
from dateutil import tz

"""
File: timezone.py
Author: Rafal Marguzewicz
Email: rafal.marguzewicz@incepton.com
Github: https://github.com/incepton/
Description: Timezone date for IOT global network
"""


def localtime(date, zone='Europe/Warsaw'):
    if isinstance(date, str):
        iso_date = parse_date(date)
        return iso_date.astimezone(tz.gettz(zone))
    return date


if __name__ == "__main__":
    str_date = '2018-07-16T06:25:36.472Z'
    print(localtime(str_date))

    str_date = '2018-07-16T06:25:36.472-02:00'
    print(localtime(str_date))
