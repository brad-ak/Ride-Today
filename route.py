import httplib2
import json

def read_directions_key():
    with open("directions_api_key", "r") as f:
        directions_key = str(f.readline()).strip()
        return directions_key

## Grab starting coordinates from user
##TO-DO Add function later to make a default location file
##TO-DO Add function later to request location of device
##TO-DO use place id instead of coordinates
def enter_starting():
    user_coords = input("Enter your coordinates").strip(' ')
    return user_coords

## Grab destination coordinates from user
def enter_target():
    target_coords = input("Enter your destination coordinates").strip(' ')
    return target_coords

## Make request
target_coords = enter_target()
user_coords = enter_starting()
directions_key = read_directions_key()
api_url = 'https://maps.googleapis.com/maps/api/directions/json?destination={}&origin={}&key={}'.format(target_coords,
                                                                                                       user_coords,
                                                                                                       directions_key)

def web_request(api_url):
    http = httplib2.Http()
    response = http.request(api_url)
    json_response = json.loads(response[1])
    dict = json_response['routes'][0]['legs'][0]['steps']
    for x in range(len(dict)):
        print(dict[x]['end_location'])
    return

web_request(api_url)
