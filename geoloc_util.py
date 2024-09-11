import string

import requests
import argparse
import sys

from abbreviation_to_name import find_full_name

API_KEY = 'f897a99d971b5eef57be6fafa0d83239'
BASE_URL = 'http://api.openweathermap.org/geo/1.0/direct'
BASE_URL_ZIPCODE = "http://api.openweathermap.org/geo/1.0/zip"

def get_location_by_name(city: string, state: string) -> dict | str:
    """
    Gets location by Name(City & State)
    :return: Dict or String
    """
    # Update abbreviation with full name
    state_full_name = find_full_name(state)
    try:
        response = requests.get(f"{BASE_URL}?q={city},{state_full_name}&limit=1&appid={API_KEY}")
        data = response.json()
        if data:
            # Break data down to be returned
            return {'latitude': data[0]['lat'],
                    'longitude': data[0]['lon'],
                    'name': f"{data[0]['name']}, {data[0]['state']}, {data[0]['country']}"
                    }
    # Handle Exception
    except Exception as e:
        return f"Error fetching location for {city}, {state}: {str(e)}"


def get_location_by_zip(zip_code: string) -> dict | str:
    """
    Gets the location by zip
    :return: dict or string
    """
    try:
        response = requests.get(f"{BASE_URL_ZIPCODE}?zip={zip_code},US&appid={API_KEY}")
        data = response.json()
        if 'lat' in data and 'lon' in data:
            return {
                'latitude': data['lat'],
                'longitude': data['lon'],
                'name': f"{data['name']} ({zip_code}), {data['country']}"
            }
    except Exception as e:
        return f"Error fetching location for {zip_code}: {str(e)}"

def main(locations):
    """
    Breaks down the multiple string and depicts if it's a Zip or City, State
    :param locations: Args passed in
    :return: Printed to console
    """
    results = []

    for loc in locations:
        if ',' in loc:
            city = loc.split(',')[0]
            state = loc.split(',')[1]
            result = get_location_by_name(city=city, state=state)
            if result is None:
                result = f"Location {loc}, could not be found."
            results.append(result)
        elif loc.isnumeric():
            result = get_location_by_zip(loc)
            if result is None:
                result = f"Location {loc}, could not be found."
            results.append(result)

    # Print results
    for result in results:
        # Check to see if it's a string not a dict
        if isinstance(result, str):
            print(result)
        else:
            print(f"Location: {result['name']}, Latitude: {result['latitude']}, Longitude: {result['longitude']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get geolocation data from city/state or zip code.')
    parser.add_argument('--locations', nargs='+', required=True, help='List of cities/states or zip codes.')
    args = parser.parse_args()

    if not args.locations:
        print("No locations provided!")
        sys.exit(1)

    main(args.locations)
