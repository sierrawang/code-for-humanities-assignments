# Astrononmy Picture of the Day (APOD) Assignment
In this assignment you will fetch the Astronomy Picture of the Day (APOD) from NASA's API and display.

There are three steps to complete this assignment:
1. **Sign up for a free API key** at [NASA's API portal](https://api.nasa.gov/). The api key is free!
2. **Fetch the APOD data** using the API key you received. The URL to fetch the APOD data is:
   ```
    https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
    ```

    Replace `DEMO_KEY` with your actual API key.

3. **Use the APOD data to fetch the image** and display it in a user-friendly format. The APOD data will be in JSON format and will look like this:

   ```json
   {
        "copyright": "John Doe",
       "date": "2023-10-01",
       "explanation": "A beautiful view of the Milky Way...",
       "hdurl": "https://apod.nasa.gov/apod/image/2310/milkyway.jpg",
       "media_type": "image",
       "service_version": "v1",
       "title": "Milky Way over the Desert",
       "url": "https://apod.nasa.gov/apod/image/2310/milkyway.jpg"
   }
   ```
    The `url` field contains the URL of the image, and the `title` field contains the title of the image. Make a GET request to the `url` field to fetch the image, then save it to a file.
