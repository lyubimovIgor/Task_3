import os

texts_folder = 'texts'
sorted_files_dict = {}


def get_lines():
    files_dict = {}
    for file_name in os.listdir('texts'):
        with open(os.path.join(texts_folder, file_name), encoding='utf-8') as f:
            files_dict[file_name] = len(f.readlines())
    for i in sorted(files_dict, key=files_dict.get):
        sorted_files_dict[i] = files_dict[i]
    return sorted_files_dict


def get_res():
    get_lines()
    with open('res.txt', 'w', encoding='utf-8') as res:
        for k, v in sorted_files_dict.items():
            with open(os.path.join(texts_folder, k), encoding='utf-8') as f:
                res.write(f'{k}\n{v}\n{"".join(f.readlines())}\n')


get_res()