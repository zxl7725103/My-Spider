from wordcloud import WordCloud,STOPWORDS
import pandas as pd
import jieba
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import Geo

def read():
    f = open('西红柿首富new.txt', encoding='UTF-8')
    data = pd.read_csv(f, sep=',', header=None, encoding='UTF-8',
                       names=['date', 'nickname', 'city', 'rates', 'comments'])
    return data

def ditu(data):

    #print(data.values)
    #读取数据，以','分隔为5列
    city=data.groupby(['city']) #抓取'city'列的值
    #print(city.count().index)
    #rate_group=data['rates'].groupby(data['city'])
    rate_group = city['rates']  #抓取以'city'为字段的'rates'组
    #print(rate_group.count())
    #city_com=data.groupby(['city']).agg(['count'])
    city_com = city['city'].agg(['count'])  # 统计每个城市的总数
    #print(city_com.count())
    city_com.reset_index(inplace=True)
    data_map = [(city_com['city'][i],city_com['count'][i]) for i in range(0,city_com.shape[0])]
    geo = Geo("西红柿首富",title_color="#fff",title_pos="center",width=1200,
              height=600,background_color="#404a59")
    while True:
        try:
            attr, val = geo.cast(data_map)
            geo.add("", attr, val, visual_range=[0, 5], visual_text_color="#fff", is_geo_effect_show=False,
                    is_piecewise=True, visual_split_number=6, symbol_size=15, is_visualmap=True)

        except ValueError as e:
            e = str(e)
            e = e.split("No coordinate is specified for ")[1]  # 获取不支持的城市名称
            for i in range(0,len(data_map)):
                if e in data_map[i]:
                    data_map.pop(i)
                    break
        else:
            break
    geo.render('西红柿首富.html')
def rates_bar(data):
    rate=data['rates'].value_counts()   #以评分进行统计
    #print(rate)
    sns.set_style('darkgrid')
    bar_plot=sns.barplot(x=rate.index,y=(rate.values/sum(rate)),palette='muted')   #每个分值的占比
    plt.xticks(rotation=90)
    plt.show()

def ciyun(data):
    comment=jieba.cut(str(data['comments']),cut_all=False) #分词
    wl_space_split= " ".join(comment)
    backgroud_Image=plt.imread('shenteng.jpg')  #添加背景
    stopwords = STOPWORDS.copy()
    print(" STOPWORDS.copy()", help(STOPWORDS.copy()))
    # 可以自行加多个屏蔽词，也可直接下载停用词表格
    stopwords.add("电影")
    stopwords.add("一部")
    stopwords.add("一个")
    stopwords.add("没有")
    stopwords.add("什么")
    stopwords.add("有点")
    stopwords.add("这部")
    stopwords.add("这个")
    stopwords.add("不是")
    stopwords.add("真的")
    stopwords.add("感觉")
    stopwords.add("觉得")
    stopwords.add("还是")
    stopwords.add("特别")
    stopwords.add("非常")
    stopwords.add("可以")
    stopwords.add("因为")
    stopwords.add("为了")
    stopwords.add("比较")
    #print(stopwords)
    # 设置词云参数
    # 参数分别是指定字体/背景颜色/最大的词的大小,使用给定图作为背景形状
    wc=WordCloud(width=1024,height=768,background_color='white',mask=backgroud_Image,
                 font_path='‪C:\Windows\Fonts\simhei.ttf',stopwords=stopwords,max_font_size=400,random_state=50)
    print(wl_space_split)
    wc.generate_from_text(str(wl_space_split))
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    wc.to_file(r'shenteng_wordcloud.jpg')





if __name__=='__main__':
    data=read()
    #ditu(data)  #生成热力图
    #rates_bar(data)   #生产评分柱状图
    ciyun(data)  #生成词云图

