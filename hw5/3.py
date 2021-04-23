import os


def size_of_files(directory_address):
    path = directory_address
    dirs = os.listdir(path)

    for fname in dirs:
        if os.path.isfile(fname):
            if '.' not in (str(fname))[-5:]:
                return f'size of {fname}: {os.path.getsize(fname)}'


print(size_of_files('F:/me/Maktab Sharif/جنگو/hw5'))
