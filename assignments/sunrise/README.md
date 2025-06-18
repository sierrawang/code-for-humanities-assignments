# Sunrise
In this challenge, you will ask a user for their latitude and longitude, and then use the `sunrise-sunset` API to determine the time of sunrise and sunset for that location. You will then display the results in a user-friendly format.

The documentation for the API you will be using is available at [Sunrise-Sunset API](https://sunrise-sunset.org/api).

## Challenge
1. Prompt the user for their latitude and longitude.
2. Make a request to the `sunrise-sunset` API using the provided latitude and longitude.
3. Parse the JSON response to extract the sunrise and sunset times.

Note: 
The API can be queried at the endpoint: 
https://api.sunrise-sunset.org/json

It has several allowed parameters (you can see all of them in the documentation), but for this challenge, you will only need to use the following. 
lat (float): Latitude in decimal degrees. Required.
lng (float): Longitude in decimal degrees. Required.

These are the only two parameters that are required for the API to return a response.

You can see a sample request at the following URL:
https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400

Use this information to determine how to get the information you will need to print.
A sample output of the program could look like this:
    
``` 
Enter the latitude: 37
Enter the longitude: -122
Sunrise: 12:46:44 PM
Sunset: 3:31:51 AM
```
Note that the times are in UTC, so you may want to convert them to your local time zone if necessary.
To conver the time zone to Pacific Time, you can set the parameter "tzid" to "America/Los_Angeles".

Then your output would look like this:

```
Enter the latitude: 37
Enter the longitude: -122
Sunrise: 5:46:36 AM
Sunset: 8:31:33 PM
```

## Extension
See in the API docs, that the API can also accept a `date` parameter.
Allow the user to specify a date, and if they do not, use the current date.
Then, use that date to query the API for sunrise and sunset times on that specific date.