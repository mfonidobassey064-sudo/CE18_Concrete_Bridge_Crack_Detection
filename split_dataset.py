import os
import splitfolders

# CE18 - CONCRETE BRIDGE DECK DATASET
# Dataset Separation Script


# Original dataset
INPUT_FOLDER = "dataset/D"

# Location where the separated dataset will be created
OUTPUT_FOLDER = "dataset"


# Check that the original dataset exists
if not os.path.exists(INPUT_FOLDER):
    raise FileNotFoundError(
        f"Dataset not found: {INPUT_FOLDER}"
    )


# Check that the two classes exist
cracked_folder = os.path.join(INPUT_FOLDER, "CD")
uncracked_folder = os.path.join(INPUT_FOLDER, "UD")

if not os.path.exists(cracked_folder):
    raise FileNotFoundError(
        f"Cracked Deck folder not found: {cracked_folder}"
    )

if not os.path.exists(uncracked_folder):
    raise FileNotFoundError(
        f"Uncracked Deck folder not found: {uncracked_folder}"
    )


# Split the dataset
# 70% = Training
# 15% = Validation
# 15% = Testing

splitfolders.ratio(
    INPUT_FOLDER,
    output=OUTPUT_FOLDER,
    seed=42,
    ratio=(0.70, 0.15, 0.15),
    group_prefix=None
)


print("==========================================")
print("CE18 DATASET SPLITTING COMPLETED")
print("==========================================")
print("Training set:   70%")
print("Validation set: 15%")
print("Testing set:    15%")
print("==========================================")
