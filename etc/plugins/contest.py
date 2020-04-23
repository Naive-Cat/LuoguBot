from nonebot import on_command, CommandSession
import  requests

month=['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

name=[]
start=[]
length=[]

def get_contest():
    url = 'https://codeforc.es/contests'
    res = requests.get(url)
    string = res.text
    f=open("test.html","w")
    f.write(string)
    f.close()
    f=open("test.html","r")
    for i in range(1,495):
        f.readline()
    while True:
        string=f.readline()
        if string=='<td>\n':
            string=f.readline()
        if string=='</tr>\n':
            f.readline()
            f.readline()
            string=f.readline()
        if string=='</div>\n':
            break
        global name,start,length
        string=string[:len(string)-1]
        # print(string)
        name.append(string)
        f.readline()
        f.readline()
        while True:
            string=f.readline()
            if string=='</td>\n':
                break
        f.readline()
        f.readline()
        string=f.readline()
        string=string[43:]
        string=string[:len(string)-8]
        h=int(string[12]+string[13])+5
        d=int(string[4]+string[5])
        y=int(string[7]+string[8]+string[9]+string[10])
        mi=int(string[15]+string[16])
        mon=string[0]+string[1]+string[2]
        m=0
        for i in range(1,13):
            if mon==month[i]:
                m=i
                break
        if h>23:
            h=h-24
            d=d+1
        if y%4==0:
            days[2]=29
        if d>days[m]:
            d=d-days[m]
            m=m+1
        if m>12:
            m=m-12
            y=y+1
        string=month[m]+'/'
        if d<10:
            string=string+'0'+str(d)+'/'
        else:
            string=string+str(d)+'/'
        string=string+str(y)+' '
        if h<10:
            string=string+'0'+str(h)+':'
        else:
            string=string+str(h)+':'
        if mi<10:
            string=string+'0'+str(mi)
        else:
            string=string+str(mi)
        # print(string)
        start.append(string)
        for i in range(1,4):
            f.readline()
        string=f.readline()
        string=string[:len(string)-1]
        # print(string)
        length.append(string)
        for i in range(1,11):
            f.readline()
    return res

@on_command('CF比赛预告', aliases=('CF','CodeForces','cf','codeforces','cf比赛预告','CodeForces比赛预告','codeforces比赛预告','Codeforces比赛预告','Codeforces'))
async def daily(session: CommandSession):
    get_contest()
    await session.send('近期CodeForces比赛预告:\n')
    leng=len(name)
    for i in range(0,leng):
        await session.send('比赛名称:'+name[i]+' 比赛开始时间:'+start[i]+' 比赛时长:'+length[i]+'\n')