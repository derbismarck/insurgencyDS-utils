import requests
import os
import json
import random
import sys

def get_workshop_collection_details(api_key, collection_id):
    url = "https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/"
    data = {
        "key": api_key,
        "collectioncount": 1,
        "publishedfileids[0]": collection_id
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=data, headers=headers)
    response_json = response.json()

    if response.status_code == 200 and "response" in response_json:
        if "resultcount" in response_json["response"] and response_json["response"]["resultcount"] > 0:
            # Extract the list of children from the first collection in the response
            children = response_json["response"]["collectiondetails"][0]["children"]
            # Return a list of the child workshop item IDs
            return [child["publishedfileid"] for child in children]
    
    return None


def find_bsp_files(directory, input_ids):
    bsp_files = []

    for id in input_ids:
        id_directory = os.path.join(directory, id, "maps")
        if os.path.isdir(id_directory):
            for file in os.listdir(id_directory):
                if file.endswith(".bsp"):
                    bsp_files.append(os.path.join(id_directory, file))

    return bsp_files


def find_vanilla_bsp_files(directory):
    bsp_files = []

    if os.path.isdir(directory):
        for file in os.listdir(directory):
            if file.endswith("_coop.bsp"):
                bsp_files.append(os.path.join(directory, file))

    return bsp_files


def generate_mapcycle_text(bsp_files):
    mapcycle_text = ""

    for bsp_file in bsp_files:
        mapname = os.path.basename(bsp_file)[:-4]  # Remove the .bsp extension
        mapcycle_text += f"{mapname} checkpoint\n"
	
    return mapcycle_text.strip()


def write_mapcycle_file(mapcycle_text, output_file):
    with open(output_file, "w") as file:
        file.write(mapcycle_text)


def get_random_map(mapcycle_file):
    with open(mapcycle_file, 'r') as file:
        lines = file.readlines()
        maps = [line.split()[0] for line in lines]  # Assumes each line starts with map name
        return random.choice(maps)


def load_api_key(filename):
    try:
        with open(filename, 'r') as f:
            api_key = f.read().strip()
            if not api_key:
                print("Error: API key file is empty. Please enter your Steam Dev API key in the file.")
                sys.exit(1) # Stop the program
            return api_key
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please create this file and enter your Steam Dev API key in it.")
        sys.exit(1) # Stop the program


def do_update_map_cycle():
	api_key = load_api_key("steam_api_key.txt") # Replace with your Steam Dev API key
	collection_id = "2977646886"  # Replace with your workshop collection ID
	workshop_directory = "C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\222880" # Replace with the directory you want to search for workshop content
	mapcycle_file = "insurgency\\mapcycle__custom_checkpoint.txt" # Replace with the desired output file path
	vanilla_maps_directory = "insurgency\\maps"
	
	input_ids = get_workshop_collection_details(api_key,collection_id)
	bsp_files = find_bsp_files(workshop_directory, input_ids)
	vanilla_bsp_files = find_vanilla_bsp_files(vanilla_maps_directory)
	all_bsp_files = bsp_files + vanilla_bsp_files  # concatenate the two lists
	mapcycle_text = generate_mapcycle_text(all_bsp_files)
	write_mapcycle_file(mapcycle_text, mapcycle_file)
	
	print(f"Found {len(bsp_files)} custom maps and {len(vanilla_bsp_files)} vanilla maps, for a total of {len(all_bsp_files)} maps.")