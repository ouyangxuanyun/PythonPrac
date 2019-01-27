import subprocess


def execute_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


# subprocess.call(['ls','-l'])
# subprocess.call("exit 1", shell=True)
# subprocess.check_call(["ls","-l"])
# output = subprocess.check_output(["df","-h"])

a = (('a',888),('b',999))
res = (row[1] for row in a)

print(res,sum(res))