import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = 'lab_1/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print(f'Removing {tmpfile_path}')
        os.remove(tmpfile_path)

    print(f'Downloading url {url}')
    save_url_to_file(url, tmpfile_path)

    print(f'Copying file {tmpfile_path} {file_path}')

    shutil.copy(tmpfile_path, file_path)
except requests.exceptions.ConnectionError:
    print(f'Error downloading the file. The URL {url} is incorrect')
except FileNotFoundError:
    print(f'File cannot be found: {tmpfile_path}')
except PermissionError:
    print(f'Problem accessing the file: {file_path}')
except Exception as e:
    print(f'An error occured')
    print(f'Error details: {e}')
else:
    print(f'URL Downloaded successfully {file}')

finally:
    if os.path.exists(tmpfile_path):
        print(f'Final removal of the file {tmpfile_path}')

        os.remove(tmpfile_path)
    print('Done')
