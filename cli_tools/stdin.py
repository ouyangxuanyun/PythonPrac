import sys
import fileinput


def get_content():
    return sys.stdin.readlines()


# for line in sys.stdin:
#     print(line)


for line in fileinput.input():
    meta = {fileinput.filename(), fileinput.filelineno(), fileinput.fileno(), fileinput.isfirstline(),
            fileinput.isstdin()}
    print(*meta, end="") # *解包
    print(meta, end="")
    print(line, end="")
