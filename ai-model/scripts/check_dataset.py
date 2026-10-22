
from pathlib import Path

# Locate the AI model directory automatically
AI_MODEL_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = AI_MODEL_DIR / "dataset"

folders = [
    DATASET_DIR / "images" / "train",
    DATASET_DIR / "images" / "val",
    DATASET_DIR / "labels" / "train",
    DATASET_DIR / "labels" / "val",
]

print("PCB Smart Inspection - Dataset Check")
print("-" * 40)

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)
    files = list(folder.iterdir())

    print(f"\n{folder.relative_to(AI_MODEL_DIR)}")
    print(f"Files found: {len(files)}")

print("\nDataset folder check completed.")
print("Add the actual PCB images and annotations before training.")
