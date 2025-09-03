#绝缘火花实验
"本厂使用工频火花机进行绝缘火花实验"
def insulation_spark_test(d_jy):
    # 进行绝缘火花实验的具体操作
    for i in d_jy:
        if i<=0.25:
            print("绝缘火花实验电压为：3kV")
        elif 0.25<i<=0.5:
            print("绝缘火花实验电压为：4kV")
        elif 0.5<i<=1:
            print("绝缘火花实验电压为：6kV")
        elif 1<i<=1.5:
            print("绝缘火花实验电压为：10kV")
        elif 1.5<i<=2.0:
            print("绝缘火花实验电压为：15kV")
        elif 2.0<i<=2.5:
            print("绝缘火花实验电压为：20kV")
        elif 2.5<i:
            print("绝缘火花实验电压为：25kV")


