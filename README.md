```  _______  _______   ______    __        ______     ______     ___   .___________. __    ______   .__   __.     __    __  .___________. __   __       __  .___________.____    ____ 
 /  _____||   ____| /  __  \  |  |      /  __  \   /      |   /   \  |           ||  |  /  __  \  |  \ |  |    |  |  |  | |           ||  | |  |     |  | |           |\   \  /   / 
|  |  __  |  |__   |  |  |  | |  |     |  |  |  | |  ,----'  /  ^  \ `---|  |----`|  | |  |  |  | |   \|  |    |  |  |  | `---|  |----`|  | |  |     |  | `---|  |----` \   \/   /  
|  | |_ | |   __|  |  |  |  | |  |     |  |  |  | |  |      /  /_\  \    |  |     |  | |  |  |  | |  . `  |    |  |  |  |     |  |     |  | |  |     |  |     |  |       \_    _/   
|  |__| | |  |____ |  `--'  | |  `----.|  `--'  | |  `----./  _____  \   |  |     |  | |  `--'  | |  |\   |    |  `--'  |     |  |     |  | |  `----.|  |     |  |         |  |     
 \______| |_______| \______/  |_______| \______/   \______/__/     \__\  |__|     |__|  \______/  |__| \__|     \______/      |__|     |__| |_______||__|     |__|         |__|     
   ```                                                                                                                                                                                 

This utility fetches geolocation (latitude, longitude) data using the OpenWeather Geocoding API based on 
city, state, or zip code inputs.

## Setup
Requirements 
Python3 is set up and configured
(https://www.python.org/downloads/)

Run the manual step below:
1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt 


## Example of command running within the virtual .venv
```
$ python geoloc_util.py --locations "Madison, WI" "12345"
Location: Madison, WI, Latitude: 43.0731, Longitude: -89.4012
Location: Schenectady (12345), US, Latitude: 42.8142, Longitude: -73.9396
```
