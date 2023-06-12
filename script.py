import os


def rename_files(folder_path, text_file_path):
    with open(text_file_path, 'r') as file:
        lines = file.readlines()

    section = 0
    current_path = ''

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        number = line.split('- ')[0]

        if int(number) == 1:
            section += 1
            current_path = os.path.join(folder_path, f'Part{section}')
            os.mkdir(current_path)

        old_file_name = os.path.join(folder_path, f'lesson{line_number}.mp4')
        new_file_name = os.path.join(current_path, f'{line}.mp4')

        if os.path.exists(old_file_name):
            os.rename(old_file_name, new_file_name)
            print(f'Renamed "{old_file_name}" to "{new_file_name}"')
        else:
            print(f'File "{old_file_name}" does not exist')

        print(number)


# Usage example
folder_path = 'folder_path'
text_file_path = 'text_file_path'
rename_files(folder_path, text_file_path)
