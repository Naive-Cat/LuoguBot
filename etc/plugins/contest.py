from nonebot import on_command, CommandSession
import  requests
import re

month=['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

name=[]
start=[]
length=[]

def get_contest():
    global name,start,length
    url = 'https://codeforc.es/contests'
    res = requests.get(url)
    string = res.text
    name=re.findall('<tr data-contestId="[0-9][0-9][0-9][0-9]">\n<td>\n(.*?)\n</td>',string)
    pattern=re.findall('<span class="format-time" data-locale="en">(.*?)</span>\n</a>\n</td>\n<td>\n(.*?)\n</td>',string)
    for k in pattern:
        string=k[0]
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
        start.append(string)
        string=k[1]
        length.append(string)
    return res

@on_command('CF', aliases=('CodeForces','cf','codeforces','Codeforces'))
async def CodeForces_Report(session: CommandSession):
    get_contest()
    string='近期 CodeForces 比赛预告:\n------------------\n'
    leng=len(name)
    for i in range(0,leng):
        string=string+'比赛名称: '+name[i]+'\n比赛开始时间: '+start[i]+'\n比赛时长: '+length[i]+'\n------------------\n'
    await session.send(string)