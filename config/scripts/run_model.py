import json
from pathlib import Path

CONFIG_PATH = Path("config/constants.json")

def load_constants():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def main():
    constants = load_constants()
    print("MBM Loaded Successfully")
    print(constants["sigmoids"])

if __name__ == "__main__":
    main()
