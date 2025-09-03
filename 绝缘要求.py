#12706.1绝缘要求
def judge_insulation(insulation_list: list) -> list:
    """
    对绝缘性能测量值列表进行判定，返回处理后的结果列表。
    
    参数:
        insulation_list (list): 包含绝缘性能测量值的列表
        
    返回:
        list: 处理后的绝缘性能值列表
    """
    if not isinstance(insulation_list, list):
        raise TypeError("输入必须是列表类型")
    
    # 验证所有元素
    for value in insulation_list:
        if not isinstance(value, (int, float)):
            raise TypeError("列表中的所有元素必须是数值类型")
        if value < 0:
            raise ValueError("绝缘值不能为负数")
    
    # 使用列表推导式处理
    return [0.9 * value - 0.1 for value in insulation_list]


#print("绝缘性能测量值处理结果:", judge_insulation([1.0, 2.0, 3.0, 4.0]))