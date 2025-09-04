#挤包内护套
from itertools import chain#合并列表的方法
def extrusion_inner_sheath(bp):
        if bp[0]<=25:
            eis=1.0
            print("挤包内护套标称厚度为：1.0 mm")
            print("最薄点为：",eis*0.8-0.2,"mm")
            print("考核值为：", eis*1.05, "mm")
            bp=[x+2.1*eis for x in bp]
            return bp
        elif 25<bp[0]<=35:
            eis=1.2
            print("挤包内护套标称厚度为：1.2 mm")
            print("最薄点为：",eis*0.8-0.2,"mm")
            print("考核值为：", eis*1.05, "mm")
            bp=[x+2.1*eis for x in bp]
            return bp

        elif 35<bp[0]<=45:
            eis=1.4
            print("挤包内护套标称厚度为：1.4 mm")
            print("最薄点为：",eis*0.8-0.2,"mm")
            print("考核值为：", eis*1.05, "mm")
            bp=[x+2.1*eis for x in bp]
            return bp

        elif 45<bp[0]<=60:
            eis=1.6
            print("挤包内护套标称厚度为：1.6 mm")
            print("最薄点为：",eis*0.8-0.2,"mm")
            print("考核值为：", eis*1.05, "mm")
            bp=[x+2.1*eis for x in bp]
            return bp

        elif 60<bp[0]<=80:
            eis=1.8
            print("挤包内护套标称厚度为：1.8 mm")
            print("最薄点为：",eis*0.8-0.2,"mm")
            print("考核值为：", eis*1.05, "mm")
            bp=[x+2.1*eis for x in bp]
            return bp

        elif 80<bp[0]:
            eis=2.0
            print("挤包内护套标称厚度为：2.0 mm")
            print("最薄点为：",eis*0.8-0.2,"mm")
            print("考核值为：", eis*1.05, "mm")
            bp=[x+2.1*eis for x in bp]
            return bp


"""            
bp=[10.5,11]
print("挤包内护套后的厚度为：", extrusion_inner_sheath(bp))"""