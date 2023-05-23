import subprocess
import os
import datetime

def pack_directory(directory_name):
    root_dir = os.path.join(os.getcwd(), directory_name)
    
    if not os.path.isdir(root_dir):
        print(f"Directory '{root_dir}' does not exist.")
        return

    # vpk command to pack a directory
    # The command is usually in the format: vpk a output.vpk root
    command = ["C:\\Program Files (x86)\\Steam\\steamapps\\common\\insurgency2\\bin\\vpk.exe", root_dir]

    try:
        subprocess.check_call(command)
        
        # Get the current date and time
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d-%H%M%S")

        # Original and new file names
        original_file_name = f"{directory_name}.vpk"
        new_file_name = f"{directory_name}-{timestamp}.vpk"

        # Rename the output file
        os.rename(original_file_name, new_file_name)

        print(f"VPK packing completed successfully. Output file: {new_file_name}")
    except subprocess.CalledProcessError as e:
        print(f"VPK packing failed with error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    pack_directory("therestaurant-custom-theaters")