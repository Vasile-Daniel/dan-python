"""
Author: Vasile - Daniel DAN
This program will calculate the Resistance and Inductance for diffrents Power Factor 
we consider: frequency 60Hz and input voltage V = 230V 
"""
from math import pi, inf 
P1 = [0.25, 0.5*0.5, 1, 0.4, 0.5, 0.6] # power 
pf = [0.99, 0.80, 0.85, 0.9, 0.9, 0.9] # power factor 
b = (10e3)/3
f = 60 # frequency 
V = 230 # voltage 
w = 2*pi*f # omega =  angular velocity 

P = []; R=[]; L = []; C = []

for i in range(len(P1)):
    P.append(b*P1[i])
    
for j in range(len(P1)):
    r = ((V**2)*(pf[j]**2))/P[j] 
    R.append(r)
    if r > 0:
        L.append(((r/w)/pf[j])*((1-(pf[j])**2))**0.5)
        C.append(inf)
    else:
        L.append(0)
        C.append((1/r/w)*abs(pf[j])/(1-(pf[j])**2)**0.5)


print("Resistance R [Omega]:")
print("R = " + str(R))
print("Inductance L [H]")
print("L = " + str(L))
#print("C = " + str(C))
