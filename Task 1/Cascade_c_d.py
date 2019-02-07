import CoolProp.CoolProp as cp

def cop_function(T_int,f1,f2):
    T_coldroom = -15 + 273.15
    T_ambient = 35 + 273.15
    Te_low = T_coldroom - 10 #248.15K
    Tc_high = T_ambient + 15 #323.15K
    #pc_low is different from pe_high since we will use two refrigerants

    ''' Low temperature Cyle'''
    h_1 = cp.PropsSI('H','Q',1,'T',Te_low,f1)
    #print('h_1:',h_1)
    
    s_1 = cp.PropsSI('S','Q',1,'T',Te_low,f1)
    #print('s_1 = s_2:',s_1)
    s_2=s_1
    pc_low = cp.PropsSI('P','Q',0,'T',T_int,f1) #Q can be either 0 or 1
    #print('pc_low:',pc_low)
    
    h_2 = cp.PropsSI('H','S',s_2,'P',pc_low,f1)
    #print('h_2:',h_2)
    
    h_3 = cp.PropsSI('H','Q',0,'T',T_int,f1)
    #print('h_3:',h_3)
    #h_3 can alternatively be calculated using Q=0 and pc_low
    #h_3 = cp.PropsSI('H','Q',0,'P',pc_low,f)
    #print('h_3:',h_3)
    
    h_4 = h_3 # Assume adiabatic expansion in throttle valve, no heat or work exchange, hence h_4 = h_3
    
    '''High temperature cycle'''
    pe_high = cp.PropsSI('P','Q',0,'T',T_int,f2) #Q can be either 0 or 1
    #print('pe_high:',pe_high)
    h_5 = cp.PropsSI('H','Q',1,'P',pe_high,f2)
    #print('h_5:',h_5)
    
    s_5 = cp.PropsSI('S','Q',1,'P',pe_high,f2)
    #print('s_5 = s_6:',s_5)
    s_6=s_5
    pc_high = cp.PropsSI('P','Q',0,'T',Tc_high,f2) #Q can be either 0 or 1
    #print('pc_high:',pc_high)
    
    h_6 = cp.PropsSI('H','S',s_6,'P',pc_high,f2)
    #print('h_6:',h_6)
    
    h_7 = cp.PropsSI('H','Q',0,'T',Tc_high,f2)
    #print('h_7:',h_7)
    #h_7 can alternatively be calculated using Q=0 and pc_high
    #h_7 = cp.PropsSI('H','Q',0,'P',pc_high,f)
    #print('h_7:',h_7)
    
    h_8 = h_7 # Assume adiabatic expansion in throttle valve, no heat or work exchange, hence h_8 = h_7  

    # cop is desired heat or cooling over the work required is desired heat or cooling over the work required 
    cop = ((h_1-h_4)*(h_5-h_8))/((h_2-h_1)*(h_5-h_8)+(h_2-h_3)*(h_6-h_5))
    return cop
    
T_int_list = list(range(249,323,1))#Te_low = 248.15K, Tc_high = 323.15K
fluid = ['R404A','R134a']

#Case c_cop list
cop_list_c = list()
for item in T_int_list:
    cop_c = cop_function(item,fluid[0],fluid[1])
    cop_list_c.append(cop_c)
#Case d_cop list
cop_list_d = list()
for item in T_int_list:
    cop_d = cop_function(item,fluid[1],fluid[0])
    cop_list_d.append(cop_d)

#Plot both cases in one graph
import matplotlib.pyplot as plt
plt.plot(T_int_list, cop_list_c, 'bo',T_int_list, cop_list_d, 'ro')
plt.title('cop vs T_int for case c and d')
plt.xlabel('T_int(K)')
plt.ylabel('cop')
plt.show()

#Print max cop and corresponding intermediate temperature for case c
max_cop_c = max(cop_list_c)
max_cop_index_c = cop_list_c.index(max_cop_c)
T_int_for_maxcop_c = T_int_list[max_cop_index_c]
#Print max cop and corresponding intermediate temperature for case d
max_cop_d = max(cop_list_d)
max_cop_index_d = cop_list_d.index(max_cop_d)
T_int_for_maxcop_d = T_int_list[max_cop_index_d]

print('Max_cop_R404A_R134a(Blue)_c:',max_cop_c,'Max_Tint_R404A_R134a(Blue)_c:',T_int_for_maxcop_c)
print('Max_cop_R134a_R404a(Red)_d:',max_cop_d,'Max_Tint_R134a_R404a(Red)_d:',T_int_for_maxcop_d)





