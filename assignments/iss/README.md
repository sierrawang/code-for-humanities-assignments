# Where is the ISS?

In this assignment, your goal is to write a program that fetches the current location of the International Space Station (ISS) and displays it in a user-friendly format.

The information can be found by making a GET request to the following URL:
https://api.wheretheiss.at/v1/satellites/25544

You can open that URL in your web browser to see the data.

The JSON data that you should recieve from your request will look like this:

```json
{
    "name":"iss",
    "id":25544,
    "latitude":-0.42527425223129,
    "longitude":98.702378192363,
    "altitude":417.34181842249,
    "velocity":27582.21413734,
    "visibility":"eclipsed",
    "footprint":4493.9150262736,
    "timestamp":1749935057,
    "daynum":2460841.3779745,
    "solar_lat":23.304831848585,
    "solar_lon":224.03901224841,
    "units":"kilometers"
}
```

Print out each key in the format:

```
name: iss
id: 25544
latitude: 4.3650755752557
longitude: 102.08361234677
altitude: 416.92042277798
velocity: 27584.1957581
visibility: eclipsed
footprint: 4491.7626520252
timestamp: 1749935151
daynum: 2460841.3790625
solar_lat: 23.304878489171
solar_lon: 223.6474037804
units: kilometers
```