import os

files_to_process = [
    r"lab_4/math_sin_square.py",
    r"lab_4/math_square_root.py",
]

for file in files_to_process:

    with open(file, 'r') as f:
        print(f'file {os.path.basename(file)}')

        source = f.read()
        exec(source)
