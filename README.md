```
  _______  _______   ______    __        ______     ______     ___   .___________. __    ______   .__   __. 
 /  _____||   ____| /  __  \  |  |      /  __  \   /      |   /   \  |           ||  |  /  __  \  |  \ |  | 
|  |  __  |  |__   |  |  |  | |  |     |  |  |  | |  ,----'  /  ^  \ `---|  |----`|  | |  |  |  | |   \|  | 
|  | |_ | |   __|  |  |  |  | |  |     |  |  |  | |  |      /  /_\  \    |  |     |  | |  |  |  | |  . `  | 
|  |__| | |  |____ |  `--'  | |  `----.|  `--'  | |  `----./  _____  \   |  |     |  | |  `--'  | |  |\   | 
 \______| |_______| \______/  |_______| \______/   \______/__/     \__\  |__|     |__|  \______/  |__| \__|                                                                                                         
 __    __  .___________. __   __       __  .___________.____    ____ 
|  |  |  | |           ||  | |  |     |  | |           |\   \  /   / 
|  |  |  | `---|  |----`|  | |  |     |  | `---|  |----` \   \/   /  
|  |  |  |     |  |     |  | |  |     |  |     |  |       \_    _/   
|  `--'  |     |  |     |  | |  `----.|  |     |  |         |  |     
 \______/      |__|     |__| |_______||__|     |__|         |__|                                                                      
```

This utility fetches geolocation (latitude, longitude) data using the OpenWeather Geocoding API based on 
city, state, or zip code inputs.

`(Github Action setup on push to validate suite still is 100% green)`

## Setup
Requirements:

Python3 is set up and configured
(https://www.python.org/downloads/)

Run the steps below in the root of the project:
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt

   (If any issues arise, please reach out to ian.allheim@gmail.com and include a funny dad joke.)

## Example of command running within the virtual .venv
```
$ python3 geoloc_util.py --locations "Madison, WI" "12345"
Location: Madison, WI, Latitude: 43.0731, Longitude: -89.4012
Location: Schenectady (12345), US, Latitude: 42.8142, Longitude: -73.9396
```
