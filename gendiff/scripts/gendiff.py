import argparse
import json


def read_json(filepath):
    with open(filepath) as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()

    file1_data = read_json(args.first_file)
    file2_data = read_json(args.second_file)

    print(file1_data)
    print(file2_data)


if __name__ == "__main__":
    main()
