# Imports
import json
import sys

print("Welcome! Please wait...") # Quick loading text

def loadfromloc(): # Loads a json file from a location
    loc = input("Please input your config location: ") # Asks for location
    try: # Try to load the file as a dict
        with open(loc) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError: # File doesn't exist
        print(f"Error: File not found at {loc}")
    except json.JSONDecodeError: # File is bad json
        print(f"Error: The file is not a valid JSON.")
    except Exception as e: # Error.
        print(f"An unexpected error occurred: {e}")

try: # File loaded from dragging onto script (Usally non-Linux)
    if len(sys.argv) < 2: # Check
        raise FileNotFoundError("No file was dragged onto the script.") # No file

    filename = sys.argv[1] # Found
    
    with open(filename) as json_file: # Set to data
        data = json.load(json_file)

except FileNotFoundError as e: # Fall back to loading from location due to file not existing
    data = loadfromloc()
except json.JSONDecodeError: # File is bad json
    print("Error: The file is not a valid JSON.")
except Exception as e: # Error.
    print("An unexpected error occurred: {e}")

if data is None: # Secondary check just in case something bad happened
    print("Failed to load JSON data.")
else:

    profileprog = len(data.values()) # Load profile(s)
    print(profileprog, "profile(s) found.")

    for value in data.values(): # For each profile
        for properties in value: # For each property of the profile
            name = properties.get("name", "Profile")
            outputloc = properties.get("output_dir", "/")
            ver = properties.get("game_version", "1.21.1")
            loader = properties.get("mod_loader", "Fabric")
            mods = properties.get("mods", [])
            print("Profile:", name)
            print("Output:", outputloc)
            print("Version:", ver)
            print("Loader:", loader)
            print("Loading mods...")
            for i in mods: # For each mod
                print(i.get("name", ""))
                


