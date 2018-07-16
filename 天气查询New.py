import urllib.request
import json
import pickle
import easygui as g
import sys


pickle_file=open('city_data.pkl','rb')
city=pickle.load(pickle_file)
while 1:
    password=g.enterbox(msg='请输入城市',title='天气查询系统')
    if password==None:
        sys.exit(0)

    else:
        try:
            name1=city[password]
            name2=city[password]
        except:
            g.exceptionbox('输入错误，请重新输入！(输入中文城市名)')
            continue     
          #添加第一个天气源
        File1 =urllib.request.urlopen('http://www.weather.com.cn/data/cityinfo/'+name1+'.html')#打开url
        weatherHTML1= File1.read().decode('utf-8')#读入打开的url
        weatherJSON1= json.JSONDecoder().decode(weatherHTML1)#创建json
        weatherInfo1 = weatherJSON1['weatherinfo']
          #添加第二个天气源
        File2 =urllib.request.urlopen('http://www.weather.com.cn/data/sk/'+name1+'.html')#打开url
        weatherHTML2 = File2.read().decode('utf-8')#读入打开的url
        weatherJSON2 = json.JSONDecoder().decode(weatherHTML2)#创建json
        weatherInfo2 = weatherJSON2['weatherinfo']

        pri=['城市：'+weatherInfo1['city']+'\n发布时间：  当天'+weatherInfo1['ptime']+'\n24小时天气：'+
        '\n温度：'+weatherInfo1['temp2']+'~'+weatherInfo1['temp1']+'\n天气：'+weatherInfo1['weather']
        +'\n\n当前温度： '+weatherInfo2['temp']+'℃'+'\n风向:  '+weatherInfo2['WD']+'\n风速：  '
        +weatherInfo2['WS']+'\n相对湿度：  '+weatherInfo2['SD']+'\n风力： '+weatherInfo2['WSE']
        +'\n更新时间： '+weatherInfo2['time']]

        g.textbox(msg='天气信息：', title='天气', text=pri)
        choice = g.ccbox('还要查询其它城市吗？',choices=('是','否'))
        if choice:
            pass
        else:
            sys.exit(0)

