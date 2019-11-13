# from scipy.misc import imread
from imageio import imread
import numpy as np
from PIL import Image
import wordcloud  # 导入词云库
from wordcloud import WordCloud, ImageColorGenerator
import jieba  # 导入第三方分词库
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# mask = imread("p2.jpg")
mask = np.array(Image.open("bai.jpg"))
f = open("txt1.txt", "rb")  # 导入本地文本文档
t = f.read()  # 读取文本内容
f.close()  # 关闭文件
ls = jieba.lcut(t)  # 将文本内容返回为列表类型的分词
txt = " ".join(ls)  # 用空格分割返回的分词
print(type(txt))
w = wordcloud.WordCloud(
    font_path="/Users/donghuibiao/网课学习/DeepLearning-self/字体下载/WenYue-XinQingNianTi-W8-J.otf",
    width=2000,
    height=2000, 
    max_words=2000,
    max_font_size=1900,
    random_state=2000,
    background_color="#FFDD55",
    mask=mask)
w.generate(txt)  # 向WordCloud对象w中加载文本txt

my_font = fm.FontProperties(
    fname='/Users/donghuibiao/网课学习/DeepLearning-self/字体下载/WenYue-XinQingNianTi-W8-J.otf')
#产生背景图片，基于彩色图像的颜色生成器
image_colors = ImageColorGenerator(mask)
print('ok')

plt.imshow(w.recolor(color_func=image_colors))   #这句是决定了图片字体颜色跟原图关系
#为云图去掉坐标轴
plt.axis("off")
#画云图，显示
plt.figure()
#为背景图去掉坐标轴
plt.axis("off")
plt.imshow(mask, cmap=plt.cm.gray)

w.to_file("first2.png")  # 输出词云
