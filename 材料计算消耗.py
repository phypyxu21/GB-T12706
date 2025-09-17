
import math as m
import numpy as np
copper_density = 8.89#铜密度
Woven_Cross_Coefficient=1.02#编织交叉系数
Density_of_Steel_Tape=7.85#钢带密度
Number_of_Steel_Tape_Wrapping_Layers=2#钢带铠装层数
Steel_Tape_Overlap_Rate=0.5#钢带铠装重叠率
density_of_insulating_material=1.5#绝缘材料密度
cabling_lay_ratio=1.02#成缆绞入系数
densityOfSheathingMaterial=1.5#护套材料密度
#非紧压铜的成缆绞入系数
non_cabling_lay_ratio=1.004
#绕包材料的密度g/cm3
densityOfWrappingMaterial=1.5
#层数
Number_of_Layers=2
#绕包材料的重叠率
WrappingMaterialOverlapRate=0.3
#云母带的密度g/cm3
Density_of_mica_bands=1.42
#云母带绕包带的搭盖率
micaOverlapRate=0.4
#层数
micaNumberofLayers=2
"中压电缆铜带屏蔽"

def Medium_Voltage_Cable_Copper_Tape_Shielding(copper_binder_od,copper_binder_thickness,Number_of_Insulated_Cores,Stranding_Lay_Factor_of_Cable_Formation,Copper_Tape_Overlap_Rate):
    Rated_Consumption_of_Metal_Shielding =np.round(((copper_binder_od+copper_binder_thickness)*copper_binder_thickness*3.1416*copper_density/(1-Copper_Tape_Overlap_Rate)*Number_of_Insulated_Cores*Stranding_Lay_Factor_of_Cable_Formation),3)
    return Rated_Consumption_of_Metal_Shielding


"低压电缆统包铜带屏蔽"
def Low_Voltage_Cable_Copper_Tape_Shielding(copper_binder_od,copper_binder_thickness,Number_of_Copper_Tape_Wrapping_Layers,Copper_Tape_Overlap_Rate):
    Rated_Consumption_of_Metal_Shielding=np.round(((copper_binder_od+copper_binder_thickness*Number_of_Copper_Tape_Wrapping_Layers)*Number_of_Copper_Tape_Wrapping_Layers*copper_binder_thickness*3.1416*copper_density*(1-Copper_Tape_Overlap_Rate)),3)
    return Rated_Consumption_of_Metal_Shielding

"铜丝编织屏蔽（覆盖率计算）"
#铜丝编织这部分有疑问
#单项覆盖率p值得查表
#这里空缺了一个表
def Copper_wire_braided_shielding_coverage_calculation(copper_binder_od,Nominal_Outer_Diameter_of_Copper_Wire,copper_density,Oneway_Coverage_p_value,numbers):
    Copper_wire_braided_shielding_coverage_calculation=np.round(3.14156*3.14156/2*Nominal_Outer_Diameter_of_Copper_Wire*(Nominal_Outer_Diameter_of_Copper_Wire*2+copper_binder_od)*copper_density*Oneway_Coverage_p_value*Woven_Cross_Coefficient*numbers,3)
    return Copper_wire_braided_shielding_coverage_calculation


#铜丝编织屏蔽（编织角计算）
def Copper_Wire_Braided_Shield_Braiding_Angle_Calculation(Wire_Diameter,Half_of_the_total_number_of_braiding_spindles,Number_of_wires_per_spindle):
    sine_of_alpha=0.789
    Copper_Wire_Braided_Shield_Braiding_Angle_Calculation=3.1416/2*Wire_Diameter*Wire_Diameter*Half_of_the_total_number_of_braiding_spindles*Number_of_wires_per_spindle/sine_of_alpha*copper_density*Woven_Cross_Coefficient
    return Copper_Wire_Braided_Shield_Braiding_Angle_Calculation

#钢带铠装	
def Steel_Tape_Armoring(Outer_Diameter_Before_Armoring,Nominal_Thickness_of_Steel_Tape):
    Steel_Tape_Armoring=np.round((Outer_Diameter_Before_Armoring+Number_of_Steel_Tape_Wrapping_Layers*Nominal_Thickness_of_Steel_Tape)*Number_of_Steel_Tape_Wrapping_Layers*Nominal_Thickness_of_Steel_Tape*3.1416*(Density_of_Steel_Tape/(1+Steel_Tape_Overlap_Rate)),3)
    return Steel_Tape_Armoring

#绝缘	
def insulation(conductor_outer_diameter_before_extrusion_insulation,nominal_thickness_of_insulation_layer,number_of_insulated_cores):
    insulation=np.round((conductor_outer_diameter_before_extrusion_insulation+nominal_thickness_of_insulation_layer)*nominal_thickness_of_insulation_layer*3.1416*density_of_insulating_material*number_of_insulated_cores*cabling_lay_ratio,3)
    return insulation
#内护套
def innerSheath(conductorOuterDiameterBeforeSheathingExtrusion,nominalThicknessOfSheathLayer):
    innerSheath=np.round((conductorOuterDiameterBeforeSheathingExtrusion+nominalThicknessOfSheathLayer)*nominalThicknessOfSheathLayer*3.1416*densityOfSheathingMaterial,3)
    return innerSheath

#护套
def sheath(conductorOuterDiameterBeforeSheathingExtrusion,nominalThicknessOfSheathLayer):
    sheath=np.round((conductorOuterDiameterBeforeSheathingExtrusion+nominalThicknessOfSheathLayer)*nominalThicknessOfSheathLayer*3.1416*densityOfSheathingMaterial,3)
    return sheath

#非紧压导体铜芯用量	
#有个支数没写进去
def copperCoreConsumptionOfNonCompactedConductor(nominalCrossSectionOfConductor,conductorCoreCount):
    copperCoreConsumptionOfNonCompactedConductor=np.round(nominalCrossSectionOfConductor*conductorCoreCount*non_cabling_lay_ratio*copper_density,3)
    return copperCoreConsumptionOfNonCompactedConductor

#绕包带
#加判断判断重叠还是间隙绕包
def wrappingTape(outerDiameterBeforeWrapping,wrappingTapeThickness):
    wrappingTape=np.round((outerDiameterBeforeWrapping+wrappingTapeThickness)*Number_of_Layers*wrappingTapeThickness*3.1416*densityOfWrappingMaterial/(1+WrappingMaterialOverlapRate))
    return wrappingTape


#云母带	
def micaTape(diameter_the_wrap,micaTapeThickness,S,numberofinsaluation):
    if S<6:
        Density_of_mica_bands=0.14
        micaTape=np.round((diameter_the_wrap+micaTapeThickness*micaNumberofLayers)*micaTapeThickness*micaNumberofLayers*3.1416*Density_of_mica_bands*(1+micaOverlapRate)*numberofinsaluation*cabling_lay_ratio,3)
    else:
        Density_of_mica_bands=0.17
        micaTape=np.round((diameter_the_wrap+micaTapeThickness*micaNumberofLayers)*micaTapeThickness*micaNumberofLayers*3.1416*Density_of_mica_bands*(1+micaOverlapRate)*numberofinsaluation*cabling_lay_ratio,3)
    return micaTape

