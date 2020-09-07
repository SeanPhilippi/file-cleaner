from path import Path
from tqdm import tqdm
import os
import sys
import argparse

PATH = os.environ["FILE_CLEANER_DIR_PATH"]

default_dir = Path(PATH)

default_patterns = [
    "*.db",
    "*.pdf",
    "*.png",
    "*.jpg",
    "*.jpeg",
    "*.m3u",
    "*.nfo",
    "*.txt",
    "*.sfv",
]


parser = argparse.ArgumentParser(description="Clean directory of certain file types.")

parser.add_argument(
    "-p",
    "--path",
    help=f"Path to directory for cleaning. Default is {default_dir}.",
    default=default_dir,
)
parser.add_argument(
    "-e",
    "--extensions",
    nargs="+",
    help="Space separated list of extentions to match for deletion. ex). python3 file-cleaner.py -e .db .pdf .txt Default is "
    + " ".join(default_patterns),
    default=default_patterns,
)

args = parser.parse_args()
dir_path = args.path
extensions = args.extensions


def file_cleaner(dir, patterns):
    for i in patterns:
        files = dir.walkfiles(i)
        for file in tqdm(files):
            print(file + " removed")
            file.remove()


patterns = []
for item in extensions:
    print("item", item)
    item = item.strip(" .,")
    item = "*." + item
    patterns.append(item)

print("path:", dir_path)
print("patterns:", patterns)

file_cleaner(dir_path, patterns)