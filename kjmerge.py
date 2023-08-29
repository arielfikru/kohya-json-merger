import argparse
import json
import shutil
import os

def merge_json_files(json_a_filename, json_b_filename, backup):
    if backup:
        backup_filename = f"{json_a_filename.split('.')[0]}_backup.json"
        shutil.copy(json_a_filename, backup_filename)
        print(f"Backup created: {backup_filename}")

    with open(json_a_filename, "r") as json_a_file:
        json_a_content = json_a_file.read()

    with open(json_b_filename, "r") as json_b_file:
        json_b_content = json_b_file.read()

    json_b_content = json_b_content.lstrip("{\n")

    json_a_content = json_a_content.rstrip("}\n")
    json_a_content += "},\n"

    merged_content = json_a_content + json_b_content

    with open(json_a_filename, "w") as merged_file:
        merged_file.write(merged_content)

    print("Kohya JSON Merge Finish!")

def main():
    parser = argparse.ArgumentParser(description="Merge JSON files")
    parser.add_argument("json_a", help="JSON A file path (Primary JSON file)")
    parser.add_argument("json_b", help="JSON B file path")
    parser.add_argument("--backup", action="store_true", help="Create a backup of JSON A")

    args = parser.parse_args()
    merge_json_files(args.json_a, args.json_b, args.backup)

if __name__ == "__main__":
    main()
