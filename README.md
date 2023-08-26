# JSON File Merger for Kohya SD Script

This Python script is designed to facilitate the merging of JSON files specifically for the [Kohya SD Script](https://github.com/kohya-ss/sd-scripts).

## Overview

This script enables you to merge two JSON files, namely JSON A and JSON B, into a single merged JSON file. The primary purpose of this functionality is to integrate the contents of JSON B into JSON A, resulting in a comprehensive JSON file.

Please note that this script operates independently of the Kohya SD Script repository and does not require cloning the repository to function.

## Usage

1. Ensure you have Python installed on your system.

2. Open a terminal or command prompt.

3. Navigate to the directory containing the script.

4. Run the script using the following command:

   ```bash
   python kjmerge.py json_a_path json_b_path
   ```

   Replace `json_a_path` and `json_b_path` with the paths to your JSON A and JSON B files, respectively.

5. After successful execution, the merged content will be saved to the JSON A file, and a confirmation message will be displayed: "Kohya JSON Merging Done."

## Example

Suppose you have two JSON files: `data_a.json` and `data_b.json`. You can merge the contents of `data_b.json` into `data_a.json` using the following command:

```bash
python kjmerge.py data_a.json data_b.json
```

## License

This script is provided under the [MIT License](LICENSE).
