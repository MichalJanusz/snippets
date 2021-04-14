import requests
import os
import functools


def save_url_file(url, directory, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(directory, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


save_url_to_dir = functools.partial(save_url_file, directory='lab_4', msg='Please wait: {}')

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url=url, file=file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
save_url_to_dir(url=url, file=file)
