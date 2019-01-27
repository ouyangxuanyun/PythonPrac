import hashlib
import sys
import os

from files.os_walk import find_specific_files

CHUNK_SIZE = 8192
def get_chunk(filename):
    with open(filename) as f:
        while True:


            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            else:
                yield chunk


def get_file_checksum(filename):
    h = hashlib.md5()
    for chunk in get_chunk(filename):
        h.update(chunk)
    return h.dexdigest()


def main():
    sys.argv.append("")
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        raise SystemExit("{0} is not a direcotry".format(directory))

    record = {}

    for item in find_specific_files(directory):
        checksum = get_file_checksum(item)
        if checksum in record:
            print('find duplicated file: {0} vs {1}'.format(record[checksum], item))
        else:
            record[checksum] = item


if __name__ == '__main__':
    main()
