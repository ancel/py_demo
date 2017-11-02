import json
import csv
import sys

from util import file_util

# json转csv
if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    keys = None
    writer = None
    with open(input_file, mode='r', encoding='utf-8') as f:
        with open(output_file, 'w', encoding='utf-8') as csvfile:
            for line in f.readlines():
                try:
                    line_json = json.loads(line)
                except Exception as e:
                    raise e
                if None==keys:
                    keys = line_json.keys()
                    # writer = csv.DictWriter(csvfile, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
                    writer = csv.DictWriter(csvfile, fieldnames=keys)
                    writer.writeheader()
                writer.writerow(line_json)

