import json

info = {} #define dict to be dumped
with open('data.txt', 'r') as fp:
    line = fp.readline()
    while line:
        mon = line.split('|')
        toDict = {
            #mon name, followed by relevant stats
            mon[2].strip() : {
                'rank' : int(mon[1].strip()),
                'usage': float(mon[3].strip(' %')), 
            }
        }
        info.update(toDict)
        line = fp.readline()

with open('info.json', 'w') as fp:
    json.dump(info, fp)