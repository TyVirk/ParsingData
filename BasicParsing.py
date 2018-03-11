#Parsing

f = open('weblog.txt','r')

#print f.read()[0:200]

lines = f.read().split("\n")
data = []
#print lines
for line in lines:
    tmp = line.split(' - - ')
    ip = tmp[0]
    td = []
    td.append(ip)
    date1 = tmp[1].split(']')
    #print date1[0].split('[')[1]
    dt = date1[0].replace('[','')
    tmh = dt.split(':')[1] 
    tmm = dt.split(':')[2] 
    tms = dt.split(':')[3].split(' ')[0]
    tm = tmh +':'+tmm +':'+tms
    td.append(tmh)
    td.append(tmm)
    td.append(tms)
    data.append(td)
    #if int(tmm) > 13:
    #    print line
    
    print tm
