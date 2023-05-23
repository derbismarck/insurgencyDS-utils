# Insurgency Map Cycle Update and Server Starter

This project contains two Python scripts: `update_map_cycle.py` and `!start.py`. 

`update_map_cycle.py` is a script that fetches the list of maps in a Steam Workshop collection, finds the BSP files for these maps, combines them with the vanilla maps and writes them all to a map cycle file.

`!start.py` is a script that first calls `update_map_cycle.py` to update the map cycle file, then selects a random map from this file and launches a dedicated Insurgency server with this map.

## Prerequisites

- Python 3.6 or above
- Steam API key
- Directory path to the Insurgency dedicated server (`srcds`)
- Directory path to the Steam workshop content
- Directory path to the vanilla maps

## Setup

0. Set up an Insurgency Server, then clone this repository into the Insurgency dedicated server directory

1. Get your Steam API key and save it in the file named `steam_api_key.txt`. The API key should be the only content in this file.

2. Replace the `collection_id` in `update_map_cycle.py` with your workshop collection ID, which should exclusively contain maps from the Insurgency workshop.

3. Replace `workshop_directory` in `update_map_cycle.py` with the directory containing your workshop content.

4. Replace `mapcycle_file` in `update_map_cycle.py` with your desired output file path. The default value will probably work fine for you.

5. Replace `vanilla_maps_directory` in `update_map_cycle.py` with the directory containing the vanilla maps. The default will probably work fine for you.

## Usage

To update the map cycle file and start the server, simply run the `!start.py` script.

This will fetch the list of custom maps from the workshop collection and the list of vanilla maps, write them to the map cycle file, select a random map from this file, and launch the server with this map.

## Contributing

oh god pls no, this is just for me to do things, if you don't know me then I will probably ignore you <3