import CoolProp.CoolProp as cp

def cop_function(T_int,f):
    T_coldroom = -15 + 273.15
    T_ambient = 35 + 273.15
    Te_low = T_coldroom - 10 #248.15K
    Tc_high = T_ambient + 15 #323.15K
    #pc_low = pe_high = p_int, which will be calculated later
    
    ''' Low temperature Cyle'''
    h_1 = cp.PropsSI('H','Q',1,'T',Te_low,f)
    #print('h_1:',h_1)
    
    s_1 = cp.PropsSI('S','Q',1,'T',Te_low,f)
    #print('s_1 = s_2:',s_1)
    s_2=s_1
    p_int = cp.PropsSI('P','Q',0,'T',T_int,f) #Q can be either 0 or 1
    #print('p_int:',p_int)
    
    h_2 = cp.PropsSI('H','S',s_2,'P',p_int,f)
    #print('h_2:',h_2)
    
    h_3 = cp.PropsSI('H','Q',0,'T',T_int,f)
    #print('h_3:',h_3)
    #h_3 can alternatively be calculated using Q=0 and p_int
    #h_3 = cp.PropsSI('H','Q',0,'P',p_int,f)
    #print('h_3:',h_3)
    
    h_4 = h_3 # Assume adiabatic expansion in throttle valve, no heat or work exchange, hence h_4 = h_3
    
    '''High temperature cycle'''
    h_5 = cp.PropsSI('H','Q',1,'P',p_int,f)
    #print('h_5:',h_5)
    
    s_5 = cp.PropsSI('S','Q',1,'P',p_int,f)
    #print('s_5 = s_6:',s_5)
    s_6=s_5
    pc_high = cp.PropsSI('P','Q',0,'T',Tc_high,f) #Q can be either 0 or 1
    #print('pc_high:',pc_high)
    
    h_6 = cp.PropsSI('H','S',s_6,'P',pc_high,f)
    #print('h_6:',h_6)
    
    h_7 = cp.PropsSI('H','Q',0,'T',Tc_high,f)
    #print('h_7:',h_7)
    #h_7 can alternatively be calculated using Q=0 and pc_high
    #h_3 = cp.PropsSI('H','Q',0,'P',pc_high,f)
    #print('h_7:',h_7)
    
    h_8 = h_7 # Assume adiabatic expansion in throttle valve, no heat or work exchange, hence h_8 = h_7   

    # cop is desired heat or cooling over the work required is desired heat or cooling over the work required 
    cop = ((h_1-h_4)*(h_5-h_8))/((h_2-h_1)*(h_5-h_8)+(h_2-h_3)*(h_6-h_5))
    #print(f,cop)
    return cop
    
T_int_list = list(range(249,323,1))#Te_low = 248.15K, Tc_high = 323.15K
fluid = ['R404A','R134a']

#Case a_cop list
cop_list_a=list()
for item in T_int_list:
    cop_a = cop_function(item,fluid[0])
    cop_list_a.append(cop_a)
#Case b_cop list
cop_list_b=list()
for item in T_int_list:
    cop_b = cop_function(item,fluid[1])
    cop_list_b.append(cop_b)

    
#Plot both fluids in one graph
import matplotlib.pyplot as plt
plt.plot(T_int_list, cop_list_a, 'bo',T_int_list, cop_list_b, 'ro')
plt.title('cop vs T_int for case a and b')
plt.xlabel('T_int(K)')
plt.ylabel('cop')
plt.show()

#Case a_max cop and corresponding temperature
max_cop_a = max(cop_list_a)
max_cop_index_a = cop_list_a.index(max_cop_a)
T_int_for_maxcop_a = T_int_list[max_cop_index_a]
#Case b_max cop and corresponding temperature
max_cop_b = max(cop_list_b)
max_cop_b_index = cop_list_b.index(max_cop_b)
T_int_for_maxcop_b = T_int_list[max_cop_b_index]

print('Max_cop_R404A(Blue)_a:',max_cop_a,'Max_Tint_R404A(Blue)_a:',T_int_for_maxcop_a)
print('Max_cop_R134a(Red)_b:',max_cop_b,'Max_Tint_R134a(Red)_b:',T_int_for_maxcop_b)






