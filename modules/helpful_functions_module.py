import json


def get_file_number(cycles):
    with open("inproject_data.json", "r") as f:
        data = json.load(f)

        file_number = data["file_number"]

        updated_file_number = file_number + cycles

        data["file_number"] = updated_file_number

    with open("inproject_data.json", "w") as f:
        json.dump(data, f)

    return updated_file_number


def save_html(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    print("helpful_functions_module.py running in main.")

    # cycles = 1
    # f_number = get_file_number(cycles)
    # print(f_number)
    with open("inproject_data.json", "r") as f:
        data = json.load(f)

        file_number = data["file_number"]
        print(file_number)
