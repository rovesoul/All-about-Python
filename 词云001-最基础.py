import wordcloud  # 导入词云库
import jieba  # 导入第三方分词库
f = open("txt1.txt", "rb")  # 导入本地文本文档
t = f.read()  # 读取文本内容
f.close()  # 关闭文件
ls = jieba.lcut(t)  # 将文本内容返回为列表类型的分词
txt = " ".join(ls)  # 用空格分割返回的分词
print(type(txt))
w = wordcloud.WordCloud(font_path="/Users/donghuibiao/网课学习/DeepLearning-self/字体下载/WenYue-XinQingNianTi-W8-J.otf", width=1000,
                        height=700, background_color="white")
print('ok')
w.generate(txt)  # 向WordCloud对象w中加载文本txt
w.to_file("first.png")  # 输出词云
