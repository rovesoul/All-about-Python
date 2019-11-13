import itchat
import requests
import csv
import datetime
'''
在2的基础上添加回复，增加时间标签
'''
group_names = ['MONBOX']
rootpath = '/Users/donghuibiao/网课学习/自己想做的项目/wxchat/ItChat/itchat/chat-str'
nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
    data = {
        'key': '94c05374b371480fb4bd0c53338ccb41',  # Tuling Key
        'info': msg,  # 这是我们发出去的消息
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(apiUrl, data=data).json()
    
    # return r.get('text') # 开启自动回复

#用于接收来自朋友间的对话消息  #如果不用这个，朋友发的消息便不会自动回复
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])

@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
#用于接收群里面的对话消息

# '''
# 群聊名字FromUserName,
# ToUserName,MsgType,
# 人名ActualNickName,IsAt,人的编号ActualUserName,
# User,Type,文档内容Text
# '''

def print_content(msg):
    i=1
    # try:
    #     # print(type(msg))
    #     # with open(rootpath + '/' + 'msg' + '.txt', 'a+', newline='', encoding='utf-8') as recordword:
    #     #     recordword.write(str(msg)+'\n\n\n')
    # except:
    #     pass
    group_name = msg['FromUserName']
    a = msg['FromUserName']
    b = msg['ActualNickName']
    c = msg['ActualUserName']
    d = msg['Content']
    t = msg['CreateTime']
    at = msg['IsAt']
    print('----------------------------')
    e = str(b).replace(' ', '')
    f = str(d).replace(' ', '')
    tt = str(t).replace(' ', '')
    g = (str(nowtime)+':  '+e+':  '+f)
    print(g)
    g = (str(nowtime)+':  '+e+':  '+f+'\n')
    with open(rootpath + '/' + e + '.txt', 'a', newline='', encoding='utf-8') as recordword:
        recordword.write(g)
    # if group_name  in  group_names:
    # msg = (msg['Text']).replace(' ','')
    # print(type(msg),msg)
    # with open(rootpath +'/'+ group_name + '.csv', 'a', newline='', encoding='utf-8') as recordword :
    #     writer = csv.writer(recordword)
    #     writer.writerow(msg)
    # with open(rootpath + '/' + group_name + '.txt', 'a', newline='', encoding='utf-8') as recordword:
    #     recordword.write(msg+'\n')
    if at==True:
        return get_response(msg['Text'])
itchat.auto_login(True)
itchat.run()
