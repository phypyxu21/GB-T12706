
import math as m
import numpy as np

"中压电缆铜带屏蔽"

def Medium_Voltage_Cable_Copper_Tape_Shielding(copper_binder_od,copper_binder_thickness,Number_of_Insulated_Cores,Stranding_Lay_Factor_of_Cable_Formation,Copper_Tape_Overlap_Rate):
    Rated_Consumption_of_Metal_Shielding =np.round(((copper_binder_od+copper_binder_thickness)*copper_binder_thickness*3.1416*copper_density/(1-Copper_Tape_Overlap_Rate)*Number_of_Insulated_Cores*Stranding_Lay_Factor_of_Cable_Formation),1)
    return Rated_Consumption_of_Metal_Shielding


"低压电缆统包铜带屏蔽"
def Low_Voltage_Cable_Copper_Tape_Shielding(copper_binder_od,copper_binder_thickness,Number_of_Copper_Tape_Wrapping_Layers,Copper_Tape_Overlap_Rate):
    Rated_Consumption_of_Metal_Shielding=np.round(((copper_binder_od+copper_binder_thickness*Number_of_Copper_Tape_Wrapping_Layers)*Number_of_Copper_Tape_Wrapping_Layers*copper_binder_thickness*3.1416*copper_density*(1-Copper_Tape_Overlap_Rate)),1)
    return Rated_Consumption_of_Metal_Shielding

"铜丝编织屏蔽（覆盖率计算）"
def Copper_wire_braided_shielding_coverage_calculation(copper_binder_od,Nominal_Outer_Diameter_of_Copper_Wire,copper_density,):
    