import os
import yaml
import random

# Set folder and output file
PICTURES_DIR = "pictures"
OUTPUT_YAML = "_data/pictures.yml"

# Ensure the output directory exists
os.makedirs(os.path.dirname(OUTPUT_YAML), exist_ok=True)

# Collect image filenames (filter for common image extensions)
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
images = [
    f for f in os.listdir(PICTURES_DIR)
    if f.lower().endswith(image_extensions) and os.path.isfile(os.path.join(PICTURES_DIR, f))
]

# Shuffle the list
random.shuffle(images)

# Write to YAML
with open(OUTPUT_YAML, 'w') as f:
    yaml.dump(images, f, default_flow_style=False)

print(f"✅ Generated `{OUTPUT_YAML}` with {len(images)} shuffled images.")