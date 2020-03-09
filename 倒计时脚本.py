"""
pythong3
另外需要一个倒计时发声的音频文件， 这个随便配置
"""

import time,os
from mutagen.mp3 import MP3
from pygame import mixer,time as tm
import datetime
# function to convert the seconds into readable format

def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds

def daojishi(day=0,hour=0,min=0.0,second=0):

    print(f'总时间{day}day; {hour}H; {min}min')
    seconds=int(day*24*3600+hour*3600+min*60+second)
    timess = (datetime.datetime.now() + datetime.timedelta(days=day, hours=hour, minutes=min)).strftime("%Y/%m/%d %H:%M:%S")
    print(f'目标时间:{timess}')
    for i in reversed(range(0, seconds)):
        print("\r倒计时:{}秒".format(i), end="")
        time.sleep(1)

    playMusic('BeepStop.WAV')
    time.sleep(0.2)

def playMusic(filename, loops=0, start=0.0, value=1):
    """
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    """
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play(loops=loops, start=start)
    mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。

def stopMusic():
    mixer.music.stop()

def in_some_day():
    os.system('clear')
    while 1:
        try:
            os.system('clear')
            print('请输入天--时--分')
            get_time_day = input('请输入倒计时天(单位:天)')
            get_time_hour = input('请输入倒计时(单位:小时)')
            get_time_min = input('请输入倒计时分(单位:分钟)')
            if get_time_day == 'q'or get_time_hour=='q'or get_time_min=='q':
                break
            os.system('clear')
            daojishi(day=int(get_time_day),hour=int(get_time_hour),min=int(get_time_min))
        except Exception as e:
            print('输入错误,请输入倒计时分钟')
            time.sleep(1)

def in_one_day():
    os.system('clear')
    while 1:
        try:
            os.system('clear')
            get_time = input('请输入倒计时时间(单位:分)')
            if get_time == 'q':
                break
            else:
                os.system('clear')
                daojishi(min=float(get_time))
        except Exception as e:
            print('输入错误,请输入倒计时分钟')
            time.sleep(1)

def qidong():

    while 1:
        os.system('clear')
        cut=input('1为1天内计时, 2为多天计时, q退出\n\n请选择:')
        try:
            if cut=='q':
                break
            elif int(cut)==1:
                in_one_day()
            elif int(cut)==2:
                in_some_day()
            else:
                print('you!输入错误')
                time.sleep(1)

        except Exception as e:
            os.system('clear')
            print('you!输入错误')
            time.sleep(1)



if __name__ =='__main__':
    qidong()


