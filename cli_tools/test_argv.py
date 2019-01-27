import sys
import os


# print(sys.argv)

def main():
    sys.argv.append("")
    print(sys.argv)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exists ')
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + ' is not accessble ')
    else:
        print(filename + ' is accessble')


if __name__ == '__main__':
    main()
