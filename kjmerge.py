import argparse
import json

def merge_json_files(json_a_filename, json_b_filename):
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

    print("Kohya JSON Merging Done")

def main():
    parser = argparse.ArgumentParser(description="Merge JSON files")
    parser.add_argument("json_a", help="JSON A file path (Primary JSON file)")
    parser.add_argument("json_b", help="JSON B file path")

    args = parser.parse_args()
    merge_json_files(args.json_a, args.json_b)

if __name__ == "__main__":
    main()
