from nonebot import on_command, CommandSession
import  requests
from urllib import request
import urllib
import re

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

daycnt=[]
name=[]

def get_countdown():
    global name,daycnt
    name.clear()
    daycnt.clear()
    url = 'https://www.luogu.com.cn/'
    res = request.Request(url,headers=headers)
    response = request.urlopen(res)
    html = response.read().decode('utf-8')
    string = html
    pattern=re.findall('距 <strong>(.*?)</strong> 还剩 <strong>(.*?) 天</strong>',string)
    daycnt.append(pattern[0][1])
    name.append(pattern[0][0])
    daycnt.append(pattern[1][1])
    name.append(pattern[1][0])

@on_command('CountDown', aliases=('Countdown','countdown'))
async def CountDown_Report(session: CommandSession):
	get_countdown()
	string='距 '+name[0]+' 还剩 '+daycnt[0]+' 天\n'+'距 '+name[1]+' 还剩 '+daycnt[1]+' 天\n'
	await session.send(string)