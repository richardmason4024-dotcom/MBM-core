from core_engine.engine import MBMEngine

def main():
    engine = MBMEngine()

    sample_player = {
        "star_power": 0.72,
        "consistency": 0.81,
        "eco_fragility": 0.28,
        "aggression": 0.64
    }

    overlean = engine.calculate_overlean(sample_player)
    underlean = engine.calculate_underlean(sample_player)

    print("MBM Engine Test")
    print(f"OverLean: {overlean:.4f}")
    print(f"UnderLean: {underlean:.4f}")

if __name__ == "__main__":
    main()
