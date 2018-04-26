import os, re


def find(pattern, path):
    for root, dirs, files in os.walk(path):
        r = re.compile(pattern, re.IGNORECASE)
        return list(filter(r.search, files))

        # for name in files:
        #     if fnmatch.fnmatch(name, pattern):
        #         return os.path.join(root, name)


print(find('Mortal kombat-.*', 'c:/temp/box'))
