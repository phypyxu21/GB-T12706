#12706.1外护套厚度
#挤包外护套
#单芯电缆外护套标称厚度小于1.4的取1.4，多芯电缆外护套标称厚度小于1.8的取1.8

def rd(spec_C_sum,d_cl):
    d_os=[x*0.035+1 for x in d_cl]
    
    if spec_C_sum[0]==1:
        if d_os[0]<1.4:
            print("单芯电缆外护套标称厚度为：1.4 mm ")
            return [x+1.4*2 for x in d_cl]
        else:
            print("单芯电缆外护套标称厚度为：", round(d_os[0],3),"mm")
            return [x+round([x*2 for x in d_os],2) for x in d_cl]
    else:
        if d_os[0]<1.8:
            print("多芯电缆外护套标称厚度为：1.8 mm ")
            return [x+1.8*2 for x in d_cl]
        else:
            print("多芯电缆外护套标称厚度为：", round(d_os[0],3),"mm")
            return [x+round([x*2 for x in d_os],2) for x in d_cl]

"""
#样例： 
spec_C_sum=[3]
d_cl=[10.5, 12.3]
rd(spec_C_sum,d_cl)
#输出：
print("电缆外护套后标称厚度及实际厚度分别为： ",rd(spec_C_sum,d_cl))"""
