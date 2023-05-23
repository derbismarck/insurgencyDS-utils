import subprocess
import sys
from update_map_cycle import *

# Update the map cycle file to contain all custom maps from The Restaurant collection, as well as all vanilla maps
do_update_map_cycle()
# Get a random map from the map cycle file to start with
random_map = get_random_map("insurgency\\mapcycle__custom_checkpoint.txt")

# Launch the dedicated server
subprocess.call(["srcds.exe", "-game", "insurgency", "-console", "-port", "27015", "+map", random_map, "checkpoint", "+maxplayers", "64", "+sv_pure", "0", "+exec", "creds.cfg", "-workshop", "-insecure"])