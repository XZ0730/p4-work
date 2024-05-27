import re


def getinfo(info_str):
    temp = info_str.split('\n')
    s = []

    temp_s = '&'
    for i in range(6, len(temp)):
        if temp[i] == '':
            continue

        # print(temp[i])
        temp_s += '&' + temp[i]
        if i + 1 < len(temp) and temp[i + 1] == '':
            s.append(temp_s)
            temp_s = ''

    info1 = []
    info2 = []
    info3 = []

    # 提取元组和数字
    match = re.search(r"\((.*?)\)(.*?):\s*(\d+)", s[0])
    if match:
        # 解析元组
        arr = match.group(1).split(", ")
        arr = [x.strip("'") for x in arr]

        temp_info = {}
        temp_info['s1'] = arr[0]
        temp_info['s2'] = arr[1]
        temp_info['s3'] = arr[2]
        info1.append(temp_info)

    for i in s:
        pattern = r"Received from \('.*?', '.*?', \d+, \d+, \d+\) total: \d+"
        result = re.findall(pattern, i)
        if result:
            info2.append({'s1': result[0]})

    for i in s:
        pattern = r"(Switch \d+ - Port \d+): (\d+\.\d+) Mbps"
        result = re.findall(pattern, i)
        if result:
            temp_info3 = []
            for j in result:
                temp_info3.append({j[0]: j[1]})
            info3.append(temp_info3)

    # info = [info1, info2, info3]
    info = {
        'info1': info1,
        'info2': info2,
        'info3': info3
    }
    return info


test_info='''
p4@p4:~$ cd tutorials/exercises/final/ 
p4@p4:~/tutorials/exercises/final$  mx h1 
root@p4:/home/p4/tutorials/exercises/final#  ./receive.py
sniffing on eth0
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 1

Switch 1 - Port 1: 0.001627000885872667 Mbps
Switch 4 - Port 2: 0.0010994437730711404 Mbps
Switch 2 - Port 3: 0.0009675353411524116 Mbps
Switch 3 - Port 2: 0.0008358261481611824 Mbps
Switch 1 - Port 3: 0.0007039974773423728 Mbps
Switch 3 - Port 1: 0.0005720876247545249 Mbps
Switch 2 - Port 4: 0.0004402437849959415 Mbps
Switch 4 - Port 1: 0.00030826395100805066 Mbps
Switch 1 - Port 4: 0.0001761716793014793 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 2

Switch 1 - Port 1: 0.0016385033526583241 Mbps
Switch 4 - Port 2: 0.0011073921192439834 Mbps
Switch 2 - Port 3: 0.0009750602487511657 Mbps
Switch 3 - Port 2: 0.0008423160366074982 Mbps
Switch 1 - Port 3: 0.0007095684567255633 Mbps
Switch 3 - Port 1: 0.0005770954158832566 Mbps
Switch 2 - Port 4: 0.0004439700542198429 Mbps
Switch 4 - Port 1: 0.00031110189327723624 Mbps
Switch 1 - Port 4: 0.00017824070850681631 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 3

Switch 1 - Port 1: 0.0016224275023386343 Mbps
Switch 4 - Port 2: 0.001096616481231866 Mbps
Switch 2 - Port 3: 0.0009645623800576728 Mbps
Switch 3 - Port 2: 0.0008329679964927663 Mbps
Switch 1 - Port 3: 0.0007013461645588231 Mbps
Switch 3 - Port 1: 0.0005698755041206382 Mbps
Switch 2 - Port 4: 0.00043820889417985553 Mbps
Switch 4 - Port 1: 0.0003063881938415973 Mbps
Switch 1 - Port 4: 0.00017468091165239954 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 4

Switch 1 - Port 1: 0.001673357899785083 Mbps
Switch 4 - Port 2: 0.0011298254137279437 Mbps
Switch 2 - Port 3: 0.0009942201538593349 Mbps
Switch 3 - Port 2: 0.0008582850861673054 Mbps
Switch 1 - Port 3: 0.0007225589878152845 Mbps
Switch 3 - Port 1: 0.0005864110515928954 Mbps
Switch 2 - Port 4: 0.0004510506661454526 Mbps
Switch 4 - Port 1: 0.0003157244890384404 Mbps
Switch 1 - Port 4: 0.0001803960256500599 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 5

Switch 1 - Port 1: 0.0016370866494477597 Mbps
Switch 4 - Port 2: 0.001105981609369139 Mbps
Switch 2 - Port 3: 0.0009731140386444227 Mbps
Switch 3 - Port 2: 0.000840152664582867 Mbps
Switch 1 - Port 3: 0.0007072656814062799 Mbps
Switch 3 - Port 1: 0.0005744920026846453 Mbps
Switch 2 - Port 4: 0.0004418132013784572 Mbps
Switch 4 - Port 1: 0.00030917419205238295 Mbps
Switch 1 - Port 4: 0.00017658013933276618 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 6

Switch 1 - Port 1: 0.0015922853059680217 Mbps
Switch 4 - Port 2: 0.0010757855027145654 Mbps
Switch 2 - Port 3: 0.0009465978948953633 Mbps
Switch 3 - Port 2: 0.0008176226366716304 Mbps
Switch 1 - Port 3: 0.0006885095113823711 Mbps
Switch 3 - Port 1: 0.0005594235069040391 Mbps
Switch 2 - Port 4: 0.00043041684077625676 Mbps
Switch 4 - Port 1: 0.00030136313001487085 Mbps
Switch 1 - Port 4: 0.00017225493371325116 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 7

Switch 1 - Port 1: 0.0015976366492090079 Mbps
Switch 4 - Port 2: 0.0010795638562020944 Mbps
Switch 2 - Port 3: 0.0009499973911056494 Mbps
Switch 3 - Port 2: 0.0008203393794384453 Mbps
Switch 1 - Port 3: 0.00069082577967515 Mbps
Switch 3 - Port 1: 0.0005612994802582697 Mbps
Switch 2 - Port 4: 0.000431681850476199 Mbps
Switch 4 - Port 1: 0.0003021395255150535 Mbps
Switch 1 - Port 4: 0.0001726100254060381 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 8

Switch 1 - Port 1: 0.001640522380752682 Mbps
Switch 4 - Port 2: 0.0011085911192613089 Mbps
Switch 2 - Port 3: 0.0009754529482511126 Mbps
Switch 3 - Port 2: 0.0008427090879522169 Mbps
Switch 1 - Port 3: 0.0007096950067226968 Mbps
Switch 3 - Port 1: 0.0005766058797166869 Mbps
Switch 2 - Port 4: 0.0004435274104559739 Mbps
Switch 4 - Port 1: 0.0003104760725516051 Mbps
Switch 1 - Port 4: 0.00017743408139049175 Mbps
Received from ('10.0.2.2', '10.0.1.1', 6, 57938, 20) total: 9

Switch 1 - Port 1: 0.0016527741199396588 Mbps
Switch 4 - Port 2: 0.0011168255350990344 Mbps
Switch 2 - Port 3: 0.0009827150107856696 Mbps
Switch 3 - Port 2: 0.0008483555204968089 Mbps
Switch 1 - Port 3: 0.0007143747453644706 Mbps
Switch 3 - Port 1: 0.0005804257013244682 Mbps
Switch 2 - Port 4: 0.0004464921068567235 Mbps
Switch 4 - Port 1: 0.0003125142421855163 Mbps
Switch 1 - Port 4: 0.00017854768199541913 Mbps

Switch 1 - Port 1: 0.0012040248831809192 Mbps
Switch 4 - Port 2: 0.0010753054315469524 Mbps
Switch 2 - Port 3: 0.0009467184014803233 Mbps
Switch 3 - Port 2: 0.0008203814413886035 Mbps
Switch 1 - Port 3: 0.0006912585495991511 Mbps
Switch 3 - Port 1: 0.0005618478310782886 Mbps
Switch 2 - Port 4: 0.0004323362278844257 Mbps
Switch 4 - Port 1: 0.0003028369331271158 Mbps
Switch 1 - Port 4: 0.00017309710386908088 Mbps

'''

# print(getinfo(test_info))