'''This code was written to support adding tags to audio book metadata based on their genre'''

#Imports
import argparse
import json
from pathlib import Path

#Function
def MetaTagUpdater(rootFolder, targetGenre, targetTag):
    print("your args were - " + rootFolder + ", "+ targetGenre + ", "+ targetTag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scan metadata.json files and add a tag when a genre matches."
    )

    parser.add_argument("folder", help="Root folder to scan")
    parser.add_argument("--genre", required=True, help="Genre to search for")
    parser.add_argument("--tag", required=True, help="Tag to add if missing")

    args = parser.parse_args()

    MetaTagUpdater(
        args.folder,
        args.genre,
        args.tag)