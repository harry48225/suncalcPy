import suncalc
import time
import re

def near(val1, val2):
    # print(f"near: {abs(val1 - val2)} < {1E-15}")
    return abs(val1 - val2) < 1E-2 # Micropython has low precision

def parseDate(date:str)->tuple:
    splitter = re.compile("\s|:|-")
    dateList = [int(x) for x in list(splitter.split(date))]
    while len(dateList) < 8:
        dateList.append(0)
    return tuple(dateList)

def dateNear(date1:str, date2:str):
    '''determines if dates are within 5 minutes of each other'''
    d1 = time.mktime(parseDate(date1))# type: ignore
    d2 = time.mktime(parseDate(date2))# type: ignore
    return abs(d1 - d2) < (60 * 5)

"""Tests for `suncalc.py`.
Designed to be run on a microcontroller running micropython
"""
class SunCalcTestCases():
  def setUp(self):
      """Setup for the test cases."""

      self.utc_dt = (2013, 3, 5, 0, 0, 0, 0, 0)
      self.utc_moon_dt = (2013, 3, 4, 0, 0, 0 , 0, 0)

      self.lat = 50.5
      self.lng = 30.5
      self.height = 2000

      self.sunTimes = {
          'solarNoon': '2013-03-05 10:10:57',
          'nadir': '2013-03-04 22:10:57',
          'sunrise': '2013-03-05 04:34:56',
          'sunset': '2013-03-05 15:46:57',
          'sunriseEnd': '2013-03-05 04:38:19',
          'sunsetStart': '2013-03-05 15:43:34',
          'dawn': '2013-03-05 04:02:17',
          'dusk': '2013-03-05 16:19:36',
          'nauticalDawn': '2013-03-05 03:24:31',
          'nauticalDusk': '2013-03-05 16:57:22',
          'nightEnd': '2013-03-05 02:46:17',
          'night': '2013-03-05 17:35:36',
          'goldenHourEnd': '2013-03-05 05:19:01',
          'goldenHour': '2013-03-05 15:02:52'
      }

      self.sunHeightTimes = {
          'solarNoon': '2013-03-05 10:10:57',
          'nadir': '2013-03-04 22:10:57',
          'sunrise': '2013-03-05 04:25:07',
          'sunset': '2013-03-05 15:56:46'
      }

  def test_getPositions(self):
      """getPosition returns azimuth and altitude for the given time and location."""
      sunPos = suncalc.getPosition(self.utc_dt, self.lat, self.lng)
      assert near(sunPos["azimuth"], -2.5003175907168385)
      assert near(sunPos["altitude"], -0.7000406838781611)

  def test_getTimes(self):
      """getTimes returns sun phases for the given date and location."""
      times = suncalc.getTimes(self.utc_dt, self.lat, self.lng)
      for time in self.sunTimes:
        assert dateNear(self.sunTimes[time],times[time])

  def test_getTimesWithHeight(self):
      """getTimes returns sun phases for the given date, location and height."""
      times = suncalc.getTimes(self.utc_dt, self.lat, self.lng, self.height)
      for time in self.sunHeightTimes:
        assert dateNear(self.sunHeightTimes[time], times[time])

if __name__ == '__main__':
  tests = SunCalcTestCases()
  tests.setUp()
  tests.test_getPositions()
  tests.test_getTimes()
  tests.test_getTimesWithHeight()
  print("ALL TESTS PASSED")
