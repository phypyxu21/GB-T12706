from 成揽 import get_K as gk
from 假设直径 import r_d as rd
from 导体结构 import get_conductor_structure as gcs
from itertools import zip_longest
from 外径尺寸对应值 import get_outer_diameter as god
import numpy as np
#计算
def calculate_diameter(spec_C_sum, spec_S_int,spec_C_int,d_jY):
    k = gk(spec_C_sum)#得到成缆系数
    d = rd(spec_S_int, 0, 1)#获得相应的假设直径
    d_s=spec_S_int#获得相应的截面积
    d=god(d, d_jY)#加上相应的绝缘层厚度
    d=d[0]#控制值

    d_True_0 = gcs(spec_S_int)#获得相应的导体结构
    "通过位置加上紧压外径到空列表中"
    d_True_1 = []
    for i in d_True_0:
        d_True_1.append(i[-1])
    d_True=god(d_True_1, d_jY)
    d_True=d_True[0]#控制值
    "假设成缆直径计算"
    if len(spec_C_int) == 1:#单芯同截面
        d_l=[x*k for x in d] #缆芯直径计算
    else:
        if spec_C_sum[0] == 3:#三芯小截面判定
            if 2/3*d_s[0]>d_s[1]:
                d_l = 2*d[0]
            else:
                d_l = 2.16/3*(d[1]+2*d[0])
        elif spec_C_sum[0] == 4:#四芯小截面
            d_l=2.42/4*(d[1]+3*d[0])
        else:
            if spec_C_int[0] == 4:#五芯中有一根小截面
                d_l = 2.70/5*(d[1]+4*d[0])
            else:
                d_l = 2.70/5*(d_l[2]+d[1]+3*d[0])#五芯中有两根根小截面
    "真实成缆直径计算"
    if len(spec_C_int) == 1:#只有一根芯
        d_l_r = [x * k for x in d_True]#缆芯直径计算
    else:
        if spec_C_sum[0] == 3:#三芯小截面判定
            if 2/3*d_s[0]>d_s[1]:
                d_l_r = 2*d_True[0]
            else:
                d_l_r = 2.16/3*(d_True[1]+2*d_True[0])
        elif spec_C_sum[0] == 4:#四芯小截面
            d_l_r = 2.42/4*(d_True[1]+3*d_True[0])
        else:
            if spec_C_int[0] == 4:#五芯中有一根小截面
                d_l_r = 2.70/5*(d_True[1]+4*d_True[0])
            else:
                d_l_r = 2.70/5*(d_l_r[2]+d_True[1]+3*d_True[0])#五芯中有两根根小截面
    D=[]
    D.append(d_l)
    D.append(d_l_r)
    D=np.around(D,2)
    return D

"""
#样例示范消除注释即可使用
spec_C_sum = 3                # 芯数总和
spec_S_int = [95, 50]         # 截面积列表
spec_C_int = [2, 1]           # 各芯数列表
d_jY = [1.4, 1.2]             # 绝缘厚度补偿列表

# 调用函数
result = calculate_diameter(spec_C_sum, spec_S_int, spec_C_int, d_jY)
print("计算得到的成揽直径为：", result)"""