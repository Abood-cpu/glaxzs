import os
import json
import time
import requests
from pathlib import Path
import sys

# Function to retrieve HWID (Windows specific)
def get_hwid():
    # Execute the command to get the HWID
    result = os.popen('wmic csproduct get uuid').read().split('\n')[1].strip()
    return result

# Define the download folder as "Glokax"
download_folder = os.path.dirname(os.path.abspath(__file__))

# Clear the console window
os.system("cls")

print('''
 ________  ___       ________  ___  __    ________     ___    ___ 
|\   ____\|\  \     |\   __  \|\  \|\  \ |\   __  \   |\  \  /  /|
\ \  \___|\ \  \    \ \  \|\  \ \  \/  /|\ \  \|\  \  \ \  \/  / /
 \ \  \  __\ \  \    \ \  \\\  \ \   ___  \ \   __  \  \ \    / / 
  \ \  \|\  \ \  \____\ \  \\\  \ \  \\ \  \ \  \ \  \  /     \/  
   \ \_______\ \_______\ \_______\ \__\\ \__\ \__\ \__\/  /\   \  
    \|_______|\|_______|\|_______|\|__| \|__|\|__|\|__/__/ /\ __\ 
                                                      |__|/ \|__| 
''')
print('__________________________________________________________________')

# Function to validate the key
def validate_key(key):
    # Define your valid key here
    valid_key = "GLOK-y05uez"
    return key == valid_key

# Read the key from user input
user_key = input("Enter the key received from Discord: ")

# Validate the key
if validate_key(user_key):
    print("Key is valid. Proceeding with the script.")
    
    # Source URL of the executable file
    source_url = "https://github.com/Abood-cpu/glokax/raw/main/glokax.exe"
    
    # Path to the user's AppData roaming directory
    appdata_folder = Path(os.getenv('APPDATA'))
    
    # Create a folder named "glokax" in AppData
    glokax_folder = appdata_folder / "glokax"
    glokax_folder.mkdir(parents=True, exist_ok=True)
    
    # Destination path for the executable file
    destination_path = glokax_folder / 'glokax.exe'
    
    try:
        # Download the file
        with requests.get(source_url, stream=True) as file_response:
            with open(destination_path, "wb") as f:
                for chunk in file_response.iter_content(1024):
                    f.write(chunk)

        print("glokax.exe downloaded successfully to AppData/glokax folder.")

        # Define the JSON file path as "config.json"
        json_file_path = glokax_folder / "config.json"

        # Create JSON data for config.json
        json_data = {
        "Glokax": {
            "Binds": {
                "Keybind": "RButton",
                "Pause": "Esc",
                "Reload": "R"
            },
            "Color": {
                "Saturation": 10
            },
            "Bezier": {
                "LinearCurveX": 0.195,
                "LinearCurveY": 0.195
            },
            "Easing": {
                "SmoothnessX": 110,
                "SmoothnessY": 120,
                "SmoothingReplicatorX": 5,
                "SmoothingReplicatorY": 5,
                "SmoothingDividerX": 250,
                "SmoothingDividerY": 350,
                "Prediction": {
                    "Enabled": False,
                    "Mode": "Ideal",
                    "PredictionX": 5,
                    "PredictionY": 8
                }
            },
            "Misc": {
                "AimbotUpdateTick": 600,
                "AimbotUpdateMS": 1000,
                "CameraToGunFOV": 85,
                "FlickTime": 0,
                "KANKAN": False
            },
            "FOV": {
                "FOVOffsetX": 5,
                "FOVOffsetY": 5
            }
        }
    }

        # Write JSON data to config.json
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

        # Display loading message
        print("Glokax - loading")

        # Run the downloaded file directly using os.system, hiding the console window
        os.system(f'start /B {destination_path}')
        time.sleep(2)
        print("Glokax - loaded")  # Updated print statement
        time.sleep(2)

    except requests.exceptions.RequestException as e:
        print("Error downloading glokax.exe:", e)
    except Exception as e:
        print("An error occurred:", str(e))
    sys.exit()  # Exit the script after successful execution

else:
    print("Invalid key. Exiting the script.")
    sys.exit()  # Exit the script if the key is invalid
