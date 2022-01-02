# SunCalcMicroPy

This is a fork of [suncalcpy](https://github.com/Broham/suncalcPy), adapted to run in micropython without the moon functionality.

A (Micro)Python library for calculating sun times, and positions.  Includes methods for getting:

 * sunrise
 * sunset 
 * golden hour
 * sun position 
 * and more!

 #### [Important] for any sort of meaningful calculations you will need to use a micropython port with double-precision floats.


### Usage examples:

##### Get sunrise, sunset, golden hour and other times for San Francisco:

```
>>> import suncalc
>>> suncalc.getTimes(datetime.now().timetuple(), 37.7749, -122.4194)
{
   'sunriseEnd': '2017-09-06 06:48:24', 
   'goldenHourEnd': '2017-09-06 07:20:27', 
   'dusk': '2017-09-06 19:59:44', 
   'nightEnd': '2017-09-06 05:15:09', 
   'night': '2017-09-06 21:03:39', 
   'goldenHour': '2017-09-06 18:58:21', 
   'sunset': '2017-09-06 19:33:08', 
   'nauticalDawn': '2017-09-06 05:47:35', 
   'sunsetStart': '2017-09-06 19:30:24', 
   'dawn': '2017-09-06 06:19:04', 
   'nauticalDusk': '2017-09-06 20:31:13', 
   'sunrise': '2017-09-06 06:45:40'
}
```