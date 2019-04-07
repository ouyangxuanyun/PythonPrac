import os
import paramiko
import time
import sys
import threading

workspace_dir = os.path.abspath('..')  # 获取工作目录
workspace_tmp_dir = workspace_dir + "/tmp"  # 临时工作目录
workspace_config_dir = workspace_dir + "/config"  # config文件夹存储路径
make_install_dir = ""  # 定义安装目录
threads = []
shows = [{
    'name':'',
    'process_bar':'',
    'percent':'',
    'accepts_bytes':'',
    'total_bytes':'',
}]

def progress1(curr, total, width=50):
    percent = curr / total * 100;
    print(curr, total, percent)
    if percent >= 100:
        percent = 100
    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    # print('[%-20s]' % '^^^^^^^^') # %-*s 代表输入一个字符串，-号代表左对齐、后补空白，*号代表对齐宽度由输入时确定
    sys.stdout.write('%s %d%%' % (show_str, percent), end='')


def progress(curr, total, file_name, width=30):
    percent = curr / total * 100;
    if percent >= 100:
        percent = 100


    # sys.stdout.write('\r')
    # sys.stdout.flush()

    show_str = ('[%%-%ds]' % width) % (int(width * percent / 100) * "#")  # 字符串拼接的嵌套使用
    sys.stdout.write('\r')
    sys.stdout.write('%s ' % file_name)
    sys.stdout.write('%s %d%%  ' % (show_str, percent))
    sys.stdout.write('accepts:%s total:%s' % (curr,total))
    sys.stdout.flush()
    time.sleep(1)

def remote_scp(host_ip, host_port, host_username, host_passwd, remote_file, local_file):
    file_name=os.path.split(remote_file)[1]
    def set_show(curr,total):
        progress(curr,total,file_name)

    scp = paramiko.Transport(host_ip, host_port)
    scp.connect(username=host_username, password=host_passwd)
    sftp = paramiko.SFTPClient.from_transport(scp)
    sftp.get(remote_file, local_file, set_show)
    scp.close()
    return ("success")



# for i in range(4):
#     print(i)
#     t = threading.Thread(target=remote_scp, args=('47.92.207.20', 22, 'root', 'yunliYL@851','/storage/deploy/projects/river-chief-app/river-chief-app-1.0-SNAPSHOT.jar','river-chief-app-1.0-SNAPSHOT' + str(i) + '.jar'))
#     threads.append(t)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.start()
        # t.join()

remote_scp('47.92.207.20', 22, 'root', 'yunliYL@851','/storage/deploy/projects/river-chief-app/river-chief-app-1.0-SNAPSHOT.jar','river-chief-app-1.0-SNAPSHOT.jar')


