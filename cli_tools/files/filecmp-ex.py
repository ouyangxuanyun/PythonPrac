import filecmp

print(filecmp.cmp('test.txt', 'test3.txt'))

dirres = filecmp.dircmp('./walk-mymodule/A', './walk-mymodule/B')
print(dirres.report())
