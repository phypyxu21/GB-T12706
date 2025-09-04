"本厂暂未使用绕包内衬层，因此不作判别，若有需要，再根据情况作出相关计算"
def wrap_inner_liner(d_cl,none):
    if d_cl<=40:
        print("绕包内衬层厚度为：0.4mm")
        d_cl=[x+0.4*2 for x in d_cl]
        return d_cl
    else:
        print("绕包内衬层厚度为：0.6mm")
        d_cl=[x+0.6 *2 for x in d_cl]
        return d_cl
    