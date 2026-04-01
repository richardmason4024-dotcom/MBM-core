import json
from pathlib import Path

CONFIG_PATH = Path("config/constants.json")

class MBMEngine:
    def __init__(self):
        self.constants = self.load_constants()

    def load_constants(self):
        with open(CONFIG_PATH) as f:
            return json.load(f)

    def calculate_overlean(self, player):
        weights = self.constants["weights"]["overlean"]
        
        return (
            player["star_power"] * weights["star_power"] +
            player["consistency"] * weights["consistency"] +
            (1 - player["eco_fragility"]) * weights["eco_safety"] +
            player["aggression"] * weights["aggression"]
        )

    def calculate_underlean(self, player):
        weights = self.constants["weights"]["underlean"]
        
        return (
            (1 - player["star_power"]) * weights["low_star"] +
            player["consistency"] * weights["consistency"] +
            player["eco_fragility"] * weights["eco_risk"] +
            (1 - player["aggression"]) * weights["low_aggression"]
        )
