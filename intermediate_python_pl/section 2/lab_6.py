import os
import urllib.request

data_dir = r'lab_6'

pages = [
    {'name': 'pandaramen', 'url': 'http://pandaramen.pl'},
    {'name': 'romaxwynajem', 'url': 'http://romaxwynajem.pl'},
    {'name': 'akwariascienne', 'url': 'http://akwariascienne.pl'},
]

for page in pages:

    try:
        file_name = f'{page["name"]}.html'
        path = os.path.join(data_dir, file_name)
        urllib.request.urlretrieve(page['url'], path)

    except:
        print('an error occurred')
        break
else:
    print('all pages downloaded properly')
