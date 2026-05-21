'''This code was written to support adding tags to audio book metadata based on their genre'''

#Imports
import argparse
import json
from pathlib import Path

#Function
def MetaTagUpdater(rootFolder, targetGenre, targetTag):
    folderData = scanFolder(rootFolder)
    for metaFile in folderData.rglob("metadata.json"):
        try:
            with metaFile.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Skipping {metaFile}: {e}")
            return False
        
        genres = normalizeList(data.get("genre") or data.get("genres"))
        tags = normalizeList(data.get("tags"))

        #check for target Genre
        if any(targetGenre.lower() in genre.lower() for genre in genres):
            #check for target tag
            if not any(targetTag.lower() in tag.lower() for tag in tags):
                #update tags
                tags.append(targetTag)
                data["tags"] = tags

                print(f"Adding tag to: {metaFile}")

                with metaFile.open("w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
          
 
def scanFolder(rootFolder):
    return Path(rootFolder)

def normalizeList(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

#cmd line run
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