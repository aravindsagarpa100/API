with open('temp.txt','r') as f:
    content = f.read()
data = content.split('"')
for i in data:
    if 'http://' in i:
        print i
        break     