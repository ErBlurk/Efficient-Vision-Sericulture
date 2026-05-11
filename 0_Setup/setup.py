import os
import shutil
import pandas as pd
import zipfile
from pathlib import Path

# Paths
src_dir = "../data/images"
dst_raw = "../data/test/raw"
dst_masks = "../data/test/masks"

csv_path = os.path.join(src_dir, "0_data.csv")
zip_path = "manual_annotations.zip"
script_dir = Path(__file__).parent.resolve()

# Unzip annotations into a temp folder
tmp_dir = script_dir / "manual_annotations"
with zipfile.ZipFile(zip_path, "r") as z:
    z.extractall(script_dir)

# 2. Build list of images to move (ignore extensions)
images_to_move = {Path(f).stem for f in tmp_dir.glob("*") if f.is_file()}

# 3. Create destination folders
os.makedirs(dst_raw, exist_ok=True)
os.makedirs(dst_masks, exist_ok=True)

# 4. Load CSV and split rows
df = pd.read_csv(csv_path)
df["stem"] = df["foto"].apply(lambda x: Path(x).stem)
moved_df = df[df["stem"].isin(images_to_move)].drop(columns=["stem"])
remaining_df = df[~df["stem"].isin(images_to_move)].drop(columns=["stem"])

# 5. Move raw images from old folder
for _, row in moved_df.iterrows():
    img = row["foto"]
    src = os.path.join(src_dir, img)
    dst = os.path.join(dst_raw, img)
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Moved raw image: {img}")
    else:
        print(f"Not found: {img}")

# 6. Move masks and rename with "_mask" suffix
for mask_file in tmp_dir.glob("*"):
    if mask_file.is_file():
        dst_name = mask_file.stem + "_mask" + mask_file.suffix
        shutil.move(str(mask_file), os.path.join(dst_masks, dst_name))
        print(f"Moved mask: {dst_name}")

# 7. Save CSVs
moved_df.to_csv(os.path.join(dst_raw, "0_data.csv"), index=False)
remaining_df.to_csv(csv_path, index=False)

# 8. Cleanup: remove tmp folder if empty
if tmp_dir.exists():
    try:
        tmp_dir.rmdir()
    except OSError:
        shutil.rmtree(tmp_dir)