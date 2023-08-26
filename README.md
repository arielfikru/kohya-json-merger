# JSON File Merger for Kohya SD Script

This Python script is designed to facilitate the merging of JSON files specifically for the [Kohya SD Script](https://github.com/kohya-ss/sd-scripts).

## Overview

This script enables you to merge two JSON files, namely JSON A and JSON B, into a single merged JSON file. The primary purpose of this functionality is to integrate the contents of JSON B into JSON A, resulting in a comprehensive JSON file.

Please note that this script operates independently of the Kohya SD Script repository and does not require cloning the repository to function.

## Usage

1. Ensure you have Python installed on your system.

2. Modify the paths to the JSON files you wish to merge within the script. Locate the lines:
   
   ```python
   parser.add_argument("json_a", help="JSON A file path (Primary JSON file)")
   parser.add_argument("json_b", help="JSON B file path")
   ```

   Replace `"json_a_path"` and `"json_b_path"` with the actual file paths of your JSON A and JSON B files.

3. Open a terminal or command prompt.

4. Navigate to the directory containing the script.

5. Run the script using the following command:

   ```bash
   python script_name.py json_a_path json_b_path
   ```

   Replace `script_name.py` with the actual name of your script file, and `json_a_path` and `json_b_path` with the paths to your JSON A and JSON B files, respectively.

6. After successful execution, the merged content will be saved to the JSON A file, and a confirmation message will be displayed: "Kohya JSON Merging Done."

## Example

Suppose you have two JSON files: `data_a.json` and `data_b.json`. You can merge the contents of `data_b.json` into `data_a.json` using the following command:

```bash
python merge_json_files.py data_a.json data_b.json
```

## License

This script is provided under the [MIT License](LICENSE).

---

Feel free to customize this README as needed and ensure to include any relevant information specific to your project or use case.
