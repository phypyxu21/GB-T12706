#包bopp带的后的厚度
import math 
from itertools import chain#合并列表的方法
def bopp_thickness(d_cl,spec_C_sum):
    
    
    if spec_C_sum[0] != 1:
    #加上BOPP带的厚度
        print("加上2根BOPP带的厚度为：", [x + 0.06*4 for x in d_cl])
        return [x + 0.06*4 for x in d_cl]#包bopp带的后的厚度
    else:
        return d_cl
"""
dcl=[[10.5],[11]]
spec_C_sum=[2]
print("包bopp带后的厚度为：", bopp_thickness(dcl,spec_C_sum))"""


#挤出护套火花实验
def extrusion_spark_test(d_cl):
    # 进行挤出护套火花实验
    # 这里可以添加实验的具体步骤和计算
    ht=[x*6 for x in d_cl]
    if ht[0]>15:
        print("挤出护套火花电压为: 15kV")
    else:
        print("挤出护套火花电压为：", math.ceil(ht[0]), "kV")

#d_cl=[2.0]
#extrusion_spark_test(d_cl)