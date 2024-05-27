import time

import paramiko


# ssh 链接服务器， 传送p4 指令，并通过下载输出文件 获取结果信息
def connect_and_work(host, num):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_client.connect('192.168.238.132', username='p4', password='p4')

    channel1 = ssh_client.invoke_shell()
    channel2 = ssh_client.invoke_shell()
    channel3 = ssh_client.invoke_shell()
    channel4 = ssh_client.invoke_shell()

    cmd1 = 'cd tutorials/exercises/final/ \n ls \n make stop \n make \n'
    channel1.send(cmd1.encode('utf-8'))

    time.sleep(10)

    cmd2 = 'cd tutorials/exercises/final/ \n ./mycontroller.py\n'
    channel2.send(cmd2.encode('utf-8'))
    time.sleep(1)
    print('init success')

    cmd3 = 'cd tutorials/exercises/final/ \n mx h1 \n ./send.py ' + host + ' ' + num + '\n'
    channel3.send(cmd3.encode('utf-8'))

    cmd4 = 'cd tutorials/exercises/final/ \n mx h1 \n sudo ./receive.py \n'
    channel4.send(cmd4.encode('utf-8'))
    # time.sleep(int(num))
    for i in range(0, int(num)):
        time.sleep(1)
        host = '192.168.238.132'
        user = 'p4'
        password = 'p4'

        server_path = '/home/p4/tutorials/exercises/final/log.txt'
        local_path = "D:/TempSdnPlus/temp.txt"
        res = sftp_down_file(host, user, password, server_path, local_path)
        # if res is True:
        #     # 打开文件
        #     fo = open('D:/TempSdnPlus/temp.txt', "rw+")
        #     #
        #     # line = fo.read()
        #     # print(line)

    res = ''
    while channel4.recv_ready():
        res += channel4.recv(1024).decode('utf-8')

    print(res)
    ssh_client.close()
    return res

# 下载文件
def sftp_down_file(host,user,password,server_path, local_path,timeout=10):
    """
    下载文件，注意：不支持文件夹
    :param host: 主机名
    :param user: 用户名
    :param password: 密码
    :param server_path: 远程路径，比如：/home/sdn/tmp.txt
    :param local_path: 本地路径，比如：D:/text.txt
    :param timeout: 超时时间(默认)，必须是int类型
    :return: bool
    """
    try:
        t = paramiko.Transport((host,22))
        t.banner_timeout = timeout
        t.connect(username=user,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path, local_path)
        t.close()
        return True
    except Exception as e:
        print(e)
        return False

#
# print(connect_and_work('10.0.2.2', '50'))