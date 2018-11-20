# TODO -- Fix OSError bug.
# TODO -- Check the image quality. 

import requests
import pprint
import warnings

pp = pprint.PrettyPrinter(indent=2)
TOKEN = "uclapi-bb037067b0bc025-5930d586dd754c5-97f267b79d66d0b-a3d128d4d45b62c"

params = {
    "token": TOKEN
}

individual_room_data_url = {
    "sensor_data": "https://uclapi.com/workspaces/sensors",
    "map_live_image": "https://uclapi.com/workspaces/images/map/live"
}

r = requests.get("https://uclapi.com/workspaces/surveys", params=params)
all_library_data = r.json()

def get_room_data(survey_id, map_id, type_data="map_live_image"):
    """
    Getting the room data given the survey_id and the map_id

    Args:
        survey_id(int): The id of library surveys.
        map_id(int): The id of the map image. (the documentation is wrong)
        type_data(string/choice): the type of data we want to fetch

    Return:
        r(requests.Response): the response object, in which we can read from it.

    """
    map_param = {
        "token": TOKEN,
        "survey_id": survey_id,
        "map_id": map_id
    }

    r = requests.get(individual_room_data_url[type_data], params=map_param)
    return r

def save_svg_image(response, save_path='test_map_image.svg'):
    """
    Given the response, save the image in the given path

    Args:
        response(requests.Response): the response from the API
        save_path(str): the path we want to save the image

    Return:
        save_path(str): the path we want to save the image
    """
    warnings.warn("The save path doesn't work, since there is an Error called OSError")

    with open('test_map_image.svg', "wb") as f:
        raw_byte = get_room_data(survey_id, map_id).content
        f.write(raw_byte)

    return save_path


# Trying out the example
for room in all_library_data['surveys']:
    print(f"Room name: {room['name']} -- Start Time: {room['start_time']} - End time: {room['end_time']} -- Is Active: {room['active']}")
    map_data = room['maps']
    survey_id = room['id']

# Getting the last map for test only
last_map = map_data[-1]
map_id = last_map['id']

save_svg_image(survey_id, map_id)
