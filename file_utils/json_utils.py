import os
import json


FILE_PATH = os.path.join('{folder}', '{file_name}.json')


def is_file_exists(folder: str, file_name: str) -> bool:
    file_path = FILE_PATH.format(folder=folder, file_name=file_name)
    return os.path.isfile(file_path)


def save_file_data(key: str, data: str, folder: str, file_name: str) -> None:
    file_path = FILE_PATH.format(folder=folder, file_name=file_name)
    data_object = {key: data}
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump(data_object, file, ensure_ascii=False, indent=4)
        else:
            with open(file_path, 'w') as file:
                json.dump(data_object, file, ensure_ascii=False, indent=4)

    except OSError as e:
        print(f"Error: {e}")


def get_file_data(folder: str, file_name: str) -> dict:
    file_path = FILE_PATH.format(folder=folder, file_name=file_name)
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        # Handle the case where the file does not exist
        return None
    except json.JSONDecodeError:
        # Handle the case where the file is empty or not in valid JSON format
        return None
