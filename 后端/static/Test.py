import InfoGetter

data = ''
with open('D:/TempSdnPlus/temp.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        data = data + line + '\n'

print(InfoGetter.getinfo(data))