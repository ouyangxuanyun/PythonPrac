with open('./test.txt') as inf, open('out.txt', 'w') as outf:
    for line in inf:
        print(line.strip())
        outf.write(" ".join([word.capitalize() for word in line.split()]))
        outf.write("\n")

print('*'*100)

#下面这种方式不建议使用
with open("./test.txt") as fh:
    line = fh.readline()
    while line:
        print(line.strip())
        line = fh.readline()
