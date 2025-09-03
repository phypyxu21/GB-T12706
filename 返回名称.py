
#导体代号：
#第一种或第二种铜导体
Dao_Ti = [["T","铜芯"],["R","第五种铜导体"],["L","铝芯"]]

def get_conductor(name_list):
    if "L" in name_list:
        return "铝芯"
    elif "R" in name_list:
        return "第五种铜导体"
    else:
        return "铜芯"  # 默认铜芯
'''绝缘代号：'''
jue_Yuan = [[
    "V"  ,  "聚氯乙烯绝缘"],
    ["YJ" ,  "交联聚乙烯绝缘"],
    ["E",  "乙丙橡胶绝缘"],
    ["EY" ,  "硬乙丙橡胶绝缘"]]
def get_insulation(name_list):
    # 判断绝缘代号在前一位或前两位
    if len(name_list) >= 2 and name_list[0] + name_list[1] == "YJ":
        return "交联聚乙烯绝缘"
    elif name_list[0] == "V":
        return "聚氯乙烯绝缘"
    elif name_list[0] == "E" and len(name_list) > 1 and name_list[1] == "Y":
        return "硬乙丙橡胶绝缘"
    elif name_list[0] == "E":
        return "乙丙橡胶绝缘"
    



'''护层代号：'''
hu_Ceng = [[
     "V" , "聚氯乙烯护套"],
    ["Y" , "聚乙烯或聚烯烃护套"],
    ["F" , "弹性体护套"],
    ["Q" , "铅套"]]

'''铠装代号：'''
kai_Zhuang = [[
    "2" , "双钢带铠装"],
    ["3" , "细圆钢丝铠装"],
    ["4" , "粗圆钢丝铠装"],
    ["6" , "(双)非磁性金属带铠装"],
    ["7" ,"非磁性金属丝铠装"]]

'''注意！！！
非磁性金属带包括非磁性不锈钢带、铝、铝合金带等，若合同未注明，则由制造方确定
'''

'''外护套代号:'''
wai_Hu_Tao = [
    ["2" , "聚氯乙烯护套"],
    ["3" , "聚乙烯或聚烯烃护套"],
    ["4" , "弹性体护套"]]
def get_conductor(name_list):
    if "L" in name_list:
        return "铝芯"
    elif "R" in name_list:
        return "第五种铜导体"
    else:
        return "铜芯"  # 默认铜芯

def get_sheath(name_list, conductor_type, insulation_type):
    """
    根据导体类型和绝缘类型获取护层名称
    :param name_list: 名称列表
    :param conductor_type: 导体类型（铝芯、第五种铜导体或铜芯）
    :param insulation_type: 绝缘类型
    :return: 护层名称
    """
    if conductor_type in ["铝芯", "第五种铜导体"]:
        # 护层在导体右侧
        idx = name_list.index("L") if "L" in name_list else name_list.index("R")
        if idx + 1 < len(name_list):
            hu_code = name_list[idx + 1]
            for h in hu_Ceng:
                if hu_code == h[0]:
                    return h[1]
    else:
        # 铜芯，护层在绝缘右侧
        idx = 1 if insulation_type == "聚氯乙烯绝缘" else 2
        if idx < len(name_list):
            hu_code = name_list[idx]
            for h in hu_Ceng:
                if hu_code == h[0]:
                    return h[1]
    return None
def get_armour(name_list, sheath_index):
    """
    获取铠装名称及其位置
    :param name_list: 名称列表
    :param sheath_index: 护层在列表中的位置索引
    :return: 铠装名称及其位置索引
    """
    # 铠装通常在护层右边的第一个数字位置，或者倒数第二个位置
    if sheath_index >= 0 and sheath_index + 1 < len(name_list):
        # 首先尝试护层右边的第一个数字
        for k in kai_Zhuang:
            if name_list[sheath_index + 1] == k[0]:
                return k[1], sheath_index + 1
    
    # 如果没找到，尝试倒数第二个位置
    if len(name_list) >= 2:
        for k in kai_Zhuang:
            if name_list[-2] == k[0]:
                return k[1], len(name_list) - 2
    
    return None, -1

def get_outer_sheath(name_list, armour_index):
    """
    获取外护套名称及其位置
    :param name_list: 名称列表
    :param armour_index: 铠装在列表中的位置索引
    :return: 外护套名称及其位置索引
    """
    # 外护套通常在最后一个位置，或者在铠装右边的位置
    if armour_index >= 0 and armour_index + 1 < len(name_list):
        # 首先尝试铠装右边的位置
        for w in wai_Hu_Tao:
            if name_list[armour_index + 1] == w[0]:
                return w[1], armour_index + 1
    
    # 如果没找到，尝试最后一个位置
    if len(name_list) >= 1:
        for w in wai_Hu_Tao:
            if name_list[-1] == w[0]:
                return w[1], len(name_list) - 1
    
    return None, -1
def process_sheath_armour_info(sheath_info, armour_info):
    """
    处理护层和铠装信息，可用于其他函数
    :param sheath_info: 护层信息 (名称, 位置索引)
    :param armour_info: 铠装信息 (名称, 位置索引)
    :return: 处理后的信息
    """
    # 这里可以根据需要添加处理逻辑
    result = {
        "sheath": sheath_info[0] if sheath_info else None,
        "sheath_index": sheath_info[1] if sheath_info else -1,
        "armour": armour_info[0] if armour_info else None,
        "armour_index": armour_info[1] if armour_info else -1
    }
    return result

def return_Name(name_list, return_full_info=False):
    """
    返回电缆名称组件
    :param name_list: 名称列表
    :param return_full_info: 是否返回完整信息（包括位置索引）
    :return: 电缆名称组件列表或完整信息字典
    """
    name_CN = []
    # 导体判断
    conductor = get_conductor(name_list)
    name_CN.append(conductor)
    # 绝缘判断
    insulation = get_insulation(name_list)
    name_CN.append(insulation)
    
    # 护层判断
    sheath = get_sheath(name_list, conductor, insulation)
    sheath_index = -1
    sheath_info = None
    if sheath:
        name_CN.append(sheath)
        # 获取护层在列表中的位置
        if conductor in ["铝芯", "第五种铜导体"]:
            idx = name_list.index("L") if "L" in name_list else name_list.index("R")
            sheath_index = idx + 1
        else:
            sheath_index = 1 if insulation == "聚氯乙烯绝缘" else 2
        sheath_info = (sheath, sheath_index)
    
    # 铠装判断
    armour, armour_index = get_armour(name_list, sheath_index)
    armour_info = None
    if armour:
        name_CN.append(armour)
        armour_info = (armour, armour_index)
    
    # 外护套判断
    outer_sheath, outer_sheath_index = get_outer_sheath(name_list, armour_index)
    outer_sheath_info = None
    if outer_sheath:
        name_CN.append(outer_sheath)
        outer_sheath_info = (outer_sheath, outer_sheath_index)
    
    # 如果有铠装或外护套，则删除护层名称（只保留外护套）
    if armour or outer_sheath:
        if sheath in name_CN:
            name_CN.remove(sheath)
    
    # 处理护层和铠装信息
    sheath_armour_info = process_sheath_armour_info(sheath_info, armour_info)
    
    if return_full_info:
        return {
            "name_components": name_CN,
            "sheath_armour_info": sheath_armour_info,
            "outer_sheath_info": outer_sheath_info
        }
    else:
        return name_CN

# 示例
# 示例

name = "yjv22"
name_big = name.upper()
name_list = [i for i in name_big]

# 获取完整信息
full_info = return_Name(name_list, return_full_info=True)
#print("完整信息:", full_info)
print(str(full_info))
# 获取名称组件
"""name_components = return_Name(name_list)
print("名称组件:", name_components)
print("电缆名称为：", "".join(name_components) + "电力电缆")"""
