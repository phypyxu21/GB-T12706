#注意1.8/3kV的电缆也应具有金属层
#金属层包含以下类型：金属屏蔽，金属铠装，同芯导体、铅套
#后两种不做
#铜带厚度  单芯 多芯
"注意扁或圆金属丝铠装暂时用不上，一般为双钢带铠装或（双）非磁性钢带铠装为主"
d_copper=[0.12,0.1]

#金属带标称厚度
d_metal_band=[[0.2,0.5],
              [0.5,0.5],
              [0.8,0.8]]
d_Round_steel_wire=[0.8,1.25,1.6,2,2.5,3.15,4]

from itertools import zip_longest
#铜带标称厚度
#一般为两层铜带重叠部分绕包
#对于1.8/3kV的电缆，铜带则为一层重叠
def copper_tape_thickness(spec_C_sum,full_info,d_cl):
    if spec_C_sum[0]==1:
        print("单芯电缆铜带标称厚度为：>= 0.12 mm ")
    else:
        print("多芯电缆铜带标称厚度为：>= 0.10 mm ")


#金属铠装
#类型如下：扁金属线铠装，圆金属丝铠装，双金属带铠装
#单芯电缆应用非磁性钢带铠装
#单芯电缆铠装层下应有内衬层

"///////////////////"

#多芯电缆若金属层和铠装材料不同时应有一层隔离套隔开

"///////////////////"
#隔离套要做火花实验

"///////////////////"
#若是采用隔离套可由其代替内衬层或附加在内衬层上




#隔离套计算、
def isolation_sheath(d_cl):
    #隔离套厚度
    d_gl=[x*0.02+0.6 for x in d_cl]
    print("隔离套标称厚度为：", d_gl[0])
    return [x+2*d_gl[0] for x in d_cl]

#铠装金属丝和金属带

def armor_metal_wire_and_strip(d_cl,full_info):
    #铠装金属丝和金属带厚度
    if full_info['sheath_armour_info']['armour']=='双钢带铠装':
        index=0
        if d_cl[0]<=30:
            print("双钢带铠装厚度为：", d_metal_band[index][0],"mm")
            return [x+d_metal_band[index][0]*4 for x in d_cl]
        if 30<d_cl[0]<=70:
            print("双钢带铠装厚度为：", d_metal_band[index][1],"mm")
            return [x+d_metal_band[index][1]*4 for x in d_cl]
        if 70<d_cl[0]:
            print("双钢带铠装厚度为：", d_metal_band[index][2],"mm")
            return [x+d_metal_band[index][2]*4 for x in d_cl]
    elif full_info['sheath_armour_info']['armour']=='(双)非磁性金属带铠装':
        index=1
        if d_cl[0]<=30:
            print("(双)非磁性金属带铠装厚度为：", d_metal_band[index][0],"mm")
            return [x+d_metal_band[index][0]*4 for x in d_cl]
        if 30<d_cl[0]<=70:
            print("(双)非磁性金属带铠装厚度为：", d_metal_band[index][1],"mm")
            return [x+d_metal_band[index][1]*4 for x in d_cl]
        if 70<d_cl[0]:
            print("(双)非磁性金属带铠装厚度为：", d_metal_band[index][2],"mm")
            return [x+d_metal_band[index][2]*4 for x in d_cl]

    elif full_info['sheath_armour_info']['armour']=='细圆钢丝铠装'or full_info['sheath_armour_info']['armour']=='粗圆钢丝铠装':
        if d_cl[0]<=10:
            print("圆钢丝铠装厚度为：", d_Round_steel_wire[0],"mm")
            return [x+d_Round_steel_wire[0]*2 for x in d_cl]
        if 10<d_cl[0]<=15:
            print("圆钢丝铠装厚度为：", d_Round_steel_wire[1],"mm")
            return [x+d_Round_steel_wire[1]*2 for x in d_cl]
        if 15<d_cl[0]<=25:
            print("圆钢丝铠装厚度为：", d_Round_steel_wire[2],"mm")
            return [x+d_Round_steel_wire[2]*2 for x in d_cl]
        if 25<d_cl[0]<=35:
            print("圆钢丝铠装厚度为：", d_Round_steel_wire[3],"mm")
            return [x+d_Round_steel_wire[3]*2 for x in d_cl]
        if 35<d_cl[0]<=60:
            print("圆钢丝铠装厚度为：", d_Round_steel_wire[4],"mm")
            return [x+d_Round_steel_wire[4]*2 for x in d_cl]
        if 60<d_cl[0]:
            if full_info['sheath_armour_info']['armour']!='粗圆钢丝铠装':
                print("圆钢丝铠装厚度为：", d_Round_steel_wire[5],"mm")
                return [x+d_Round_steel_wire[5]*2 for x in d_cl]
            else:
                print("粗圆钢丝铠装厚度为：", d_Round_steel_wire[6],"mm")
                return [x+d_Round_steel_wire[6]*2 for x in d_cl]
            