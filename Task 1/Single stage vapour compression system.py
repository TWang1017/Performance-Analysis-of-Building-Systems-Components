import CoolProp.CoolProp as cp

T_coldroom = -15 + 273.15
T_ambient = 35 + 273.15
Te = T_coldroom - 10
Tc = T_ambient + 15

fluid = ['R12','R404A','R134a']

for f in fluid:
    h_1 = cp.PropsSI('H','Q',1,'T',Te,f)
    #print('h_1:',h_1)
    
    s_1 = cp.PropsSI('S','Q',1,'T',Te,f)
    #print('s_1 = s_2:',s_1)
    s_2=s_1
    p_c = cp.PropsSI('P','Q',0,'T',Tc,f) #Q can be either 0 or 1
    #print('p_c:',p_c)
    
    h_2 = cp.PropsSI('H','S',s_2,'P',p_c,f)
    #print('h_2:',h_2)
    
    h_3 = cp.PropsSI('H','Q',0,'T',Tc,f)
    #print('h_3:',h_3)
    #h_c can alternatively be calculated using Q=0 and p_c
    #h_3 = cp.PropsSI('H','Q',0,'P',p_c,f)
    #print('h_3:',h_3)
    
    h_4 = h_3 # Assume adiabatic expansion in throttle valve, no heat or work exchange, hence h_4 = h_3
    
    # cop is desired heat or cooling over the work required is desired heat or cooling over the work required 
    Q_41 = h_1 - h_4 #desired heat
    W_12 = h_2 - h_1 #work required 
    cop = Q_41/W_12
    print(f,cop)