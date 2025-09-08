#导入正则，取关键数值
import re
#返回名称
from 返回名称 import return_Name as fn
#返回假设直径
from 假设直径 import r_d as rd
#获得绝缘厚度
from 绝缘厚度 import get_insulation_data as gd
#获得成缆直径
from 成揽直径计算 import calculate_diameter as cd
#获得最薄点
from 绝缘要求 import judge_insulation as ji
#获得导体结构
from 导体结构 import get_conductor_structure as gcs
#获得外径尺寸对应值
from 外径尺寸对应值 import get_outer_diameter as god
#获得工频绝缘火花试验电压
from 绝缘火花试验电压 import insulation_spark_test
#获得绕bopp带和挤出护套火花实验电压
from bopp和挤出护套火花实验 import bopp_thickness as bt
#列表求和
from itertools import zip_longest
#获得挤包内护套厚度
from 挤包内护套 import extrusion_inner_sheath as eis
#获得金属层 屏蔽 隔离 铠装及相应厚度
from 金属层_屏蔽隔离铠装 import copper_tape_thickness as ctt
from 金属层_屏蔽隔离铠装 import isolation_sheath as iss
from 金属层_屏蔽隔离铠装 import armor_metal_wire_and_strip as amwas
from 挤包外护套 import rd_out 
#格式规范输出
import numpy as np
    







print("请输入电缆的型号(不管大小写)：")
print("例如：VV、YJV22、vv")

# 输入电缆型号名称
name = input()
name_big = name.upper()  # 将输入转换为大写
name_list =[]
#转到空列表中
for i in name_big:
   name_list.append(i)

#调出函数，获得正确的名字
print("电缆名称为：", "".join(fn(name_list)) + "电力电缆\n")
#名字全信息
full_info = fn(name_list, return_full_info=True)


#规格输入
print("请输入电缆的规格：")
print("例如：3x95+1x50")
spec = input()
# 提取所有数字
numbers = re.findall(r'\d+', spec)
# 输出示例：['3', '95', '1', '50']
'''re.findall(r'\d+', spec) 的作用是用正则表达式查找字符串 spec 中所有连续的数字，并以列表形式返回。

\d 表示匹配一个数字字符（0-9）。
+ 表示匹配前面的内容一次或多次，即匹配一个或多个连续数字。
findall 会遍历整个字符串，把所有符合 \d+ 的部分都提取出来，组成一个列表。
例如，输入 3x95+1x50，会依次匹配到 3、95、1、50，最终返回 ['3', '95', '1', '50']。'''


#电压输入
print("请输入电压的规格：")
print("例如：0.6/1(1.2)KV")
voltage = input()

# 提取电压中的所有数字（如0.6、1、1.2）
voltage_numbers = re.findall(r'\d+\.\d+|\d+', voltage)
voltage_numbers_int = [float(x) for x in voltage_numbers]



#获得面积数值
spec_S = numbers[1::2]
spec_S_int = [int(x) for x in spec_S]


#获得对应芯数
spec_C = numbers[0::2]
spec_C_int = [int(x) for x in spec_C]



#芯的总数
spec_C_sum=[sum(spec_C_int)]


#获得假设直径
print("假设直径为：\n", rd( spec_S_int, 0, 1))
#获得导体结构
daoti_structure = gcs(spec_S_int)
print("导体结构为：\n", daoti_structure)
for j in range(len(daoti_structure)):
        print("导体结构为：",daoti_structure[j][1],"单线要求为：",daoti_structure[j][2],"单线偏差为：±",daoti_structure[j][3],"紧压外径为：",daoti_structure[j][4],)#写一个按顺序输出的格式


#获得绝缘层厚度
d_jY = gd(name_list, voltage_numbers_int, spec_S_int)
d_jY=np.round(d_jY,1)
print("绝缘层厚度及平均值各为：\n", d_jY)
d_jY = ji(d_jY)
d_jY=np.round(d_jY,1)
print("绝缘最小厚度分别为(即最薄点)：\n", d_jY)

#外径尺寸对应值
outer_diameter =[]
for i in daoti_structure:
      outer_diameter.append(i[-1])
od = god(outer_diameter, d_jY)
od=np.round(od,2)
print("外径尺寸控制值为：", od[0],"下限值为：", od[1],"上限值为：", od[2])

#获得绝缘火花实验电压
insulation_spark_test(d_jY)

#获得缆芯假设直径以及缆芯直径
d_cl=cd(spec_C_sum, spec_S_int,spec_C_int,d_jY)
d_cl=np.round(d_cl,2)
print("假设成缆直径为：", d_cl[0],"成缆直径为：", d_cl[1])

#加BOPP带后的厚度
d_bp=bt(d_cl,spec_C_sum)
d_cl=d_bp

#内护套厚度 然后马上接金属层
if voltage_numbers_int[1]!=3 and full_info['sheath_armour_info']['armour'] != None and full_info['outer_sheath_info'] !=None:
           bp=eis(d_bp)
           bp=np.round(bp,2)
           print("挤包内护套后的标称直径为：", bp[0],"挤包内护套后的直径为：", bp[1])
#隔离套
           d_cl=iss(bp)
           d_cl=np.round(d_cl,2)
           print("隔离套后的标称直径为：", d_cl[0],"隔离套后的直径为：", d_cl[1])
#铠装
           d_cl=amwas(d_cl,full_info)
           d_cl=np.round(d_cl,2)
           print("铠装后的标称直径为：", d_cl[0],"铠装后的直径为：", d_cl[1])

elif voltage_numbers_int[1]==3:
            bp=eis(d_bp)
            print("挤包内护套后的标称直径为：", bp[0],"挤包内护套后的直径为：", bp[1])
            "单层铜带屏蔽"
            d_cl=ctt(bp,full_info)
            d_cl=np.round(d_cl,2)
            print("单层铜带屏蔽后的标称直径为：", d_cl[0],"单层铜带屏蔽后的直径为：", d_cl[1])
else:
            print("不需要挤包内护套")





#外护套
d_cl=rd_out(spec_C_sum,d_cl)
d_cl=np.round(d_cl,2)
print("电缆外护套后标称厚度及实际厚度分别为： ",d_cl)

