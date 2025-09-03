from itertools import zip_longest

def get_outer_diameter(daoti_structure, d_jY):
    # 计算外径尺寸对应值
    d_jY_contrue = [x * 2.1 for x in d_jY]
    daoti_structure_contrue = [x + y for x, y in zip_longest(daoti_structure, d_jY_contrue, fillvalue=0)]
    
    d_jY_min=[x * 2 for x in d_jY]#得到相应倍数
    d_jY_max=[x * 2.2 for x in d_jY]
    daoti_structure_min = [x + y for x, y in zip_longest(daoti_structure, d_jY_min, fillvalue=0)]#列表求和
    daoti_structure_max = [x + y for x, y in zip_longest(daoti_structure, d_jY_max, fillvalue=0)]
    daoti_structure = []
    
    
    daoti_structure.append(daoti_structure_contrue)#计算得到的外径尺寸控制值
    
    daoti_structure.append(daoti_structure_min)#计算得到的外径尺寸下限值
    daoti_structure.append(daoti_structure_max)#计算得到的外径尺寸上限值

    return daoti_structure

"""
d_S=[8.3,11.6]
d_jy=[1,1.1]
od=get_outer_diameter(d_S, d_jy)
print("外径尺寸控制值为：\n", od[0])
print("外径尺寸下限值为：\n", od[1])
print("外径尺寸上限值为：\n", od[2])
"""