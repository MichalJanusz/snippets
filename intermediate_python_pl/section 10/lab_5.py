import os
import itertools as it


def scantree(path):
    for obj in os.scandir(path):
        if obj.is_dir():
            yield obj
            yield from scantree(obj.path)
        else:
            yield obj


listing = scantree('/Users/mjanusz/workspace/snippets_and_udemy/intermediate_python_pl/section 10')

for e in listing:
    print('DIR' if e.is_dir() else 'FILE', e.path)

listing = scantree('/Users/mjanusz/workspace/snippets_and_udemy/intermediate_python_pl/section 10')
listing = sorted(listing, key=lambda x: x.is_dir())

for is_dir, elements in it.groupby(listing, key=lambda x: x.is_dir()):
    print('DIR' if is_dir else 'FILE', len(list(elements)))
