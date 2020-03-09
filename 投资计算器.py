# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 定投计算公式,如果用需要输入参数
def dingtou(a,x,n):
    """定投收益的计算公式为：M=a(1+x)[-1+(1+x)^n]/x;
    其中
    M代表预期收益,
    a代表每期定投金额,
    x代表收益率,
    n代表定投期数。
    假设用户每月定投金额为300元,一年也就是3600元,年收益率为15%,定投期限为35年,则可以计算出收益为3600(1+15%)[-1+(1+15%)^35]/15%=3648044元
    """

    a=float(a)
    x = float(x) / 100
    n = int(n)
    M = a*(1 + x)*(-1 + (1 + x) ** n) / x
    return  round(M,2)

# 定投启动
def show_DT():
    a = input('输入定投金额(元):')
    x = input('输入收益率(如10%则输入10):')
    n = input('输入投资期数')
    # DT_M=dingtou(a,x,n)
    print(f'定投金额:{a},每期收益率:{x},定投期数:{n}')
    pd_col = pd.DataFrame(columns=('期数', '定投金额', '收益率','本期末成本合计', '本期末收益合计','总倍数'))
    for i in range(1,int(n)+1):
        # 定投计算
        DT_M = dingtou(a, x, i)
        # 本金计算
        benjin=round(float(a)*i,2)
        beishu=round((DT_M/benjin),2)
        # 加入数据
        b = pd.Series({'期数': i, '定投金额': a, '收益率': str(x)+'%', '本期末成本合计':benjin,'本期末收益合计': DT_M,'总倍数':beishu})
        pd_col = pd_col.append(b, ignore_index=True)
    fin=pd_col.set_index('期数')
    # 画图
    plt.figure(figsize=(15, 8))
    plt.rcParams['font.family'] = 'Arial Unicode MS'
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 12
    font1 = {
        'weight': 'normal',
        'size': 23,
    }

    x = pd_col['期数']
    y1 = pd_col['本期末成本合计']
    y2 = pd_col['本期末收益合计']
    plt.legend(["本期末成本合计", "本期末收益合计"])

    plt.ylabel('金额',size=22)
    plt.xlabel('期数',size=22)
    plt.plot(x, y1, color='blue', linewidth=1.0, linestyle='--')
    plt.plot(x, y2, color='red', linewidth=1.0, linestyle='-.')
    plt.xlim(1, int(n))
    plt.legend(('本金曲线','期末收益合计曲线'),prop=font1)
    # plt.bar (x, y3,color='blue',)
    plt.show()

    print(fin)

# 单利计算器,按期计算
def danli_income(m,n,t):
    """
        m 本金
        n 收益率如5%收益率,则输入5
        t 投资年限 如1年则输入1
        """
    m = float(m)
    n = float(n) / 100
    t = int(t)
    return round(m +m*n*t, 2)




# 复利计算收益 按期计算
def fuli_income(m,n,t):
    """
    m 本金
    n 收益率如5%收益率,则输入5
    t 投资年限 如1年则输入1
    """
    m=float(m)
    n=float(n)/100
    t=int(t)
    return round(m*(1+n)**t,2)

# 单利复利启动
def danli_VS_fuli():
    pd_col = pd.DataFrame(columns=('年限','复利收益','单利收益','差额'))
    m = input("请输入本金(单位元):")
    n = input('请输入收益率(收益率如5%收益率,则输入5):')
    t = input('请输入周期:')
    print(f'\n本金:{m}, 收益率:{n}%, 投资周期{t}\n')
    for i in range(1,int(t)+1):
        fuli = fuli_income(m, n, i)
        danli = danli_income(m, n, i)
        chae = round(fuli - danli, 2)
        # 加入数据
        b = pd.Series({'年限':i,'复利收益':fuli,'单利收益':danli,'差额':chae})
        pd_col = pd_col.append(b,ignore_index=True)
        # 修改索引列
        fin=pd_col.set_index('年限')

    # 画图
    plt.figure(figsize=(15, 8))
    plt.rcParams['font.family'] = 'Arial Unicode MS'
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 12

    font1 = {
             'weight': 'normal',
             'size': 23,
             }
    x = pd_col['年限']
    y1 = pd_col['复利收益']
    y2 = pd_col['单利收益']
    y3 = pd_col['差额']
    plt.ylabel('金额',size=22)
    plt.xlabel('期数',size=22)
    plt.plot(x, y1,color='red', linewidth=1.0, linestyle='--')
    plt.plot(x, y2,color='green', linewidth=1.0, linestyle='-.')
    plt.legend(('复利收益曲线', '单利收益曲线'),prop=font1)
    plt.show()

    print(fin)
# danli_VS_fuli()
show_DT()
