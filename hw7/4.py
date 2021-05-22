# import os
#
# for (root, dirs, files) in os.walk('F:\me\Maktab Sharif\جنگو', topdown=True):
#     print(root)
#     print(dirs)
#     print(files)
#     print('--------------------------------')

from os import walk


def get_files_of_one_dir(path):
    # f = []
    for (dirpath, dirnames, filenames) in walk(path):
        # f.extend(filenames)
        # print(f)
        if dirpath == path:
            yield filenames


for i in get_files_of_one_dir('F:\me\Maktab Sharif\جنگو'):
    print(i)
