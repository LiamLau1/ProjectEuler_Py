from scipy import integrate
import math


p=3;
k=1.38064852e-23;

d=20e-3;
a=2e-3;
rs=10e-6;
S1=math.pi*rs**2;
rn=10e-6;
S2=math.pi*rn**2;

m=6.6464764e-27;
Heradius=140e-12;
sigma=math.pi*(2*Heradius)**2;
kappa=5/3;

T=300;
Q=1e-1;
Ndot=Q/(k*T);
gamma=0.5;

v=math.sqrt(k*T/m);
cs=math.sqrt(kappa*k*T/m);
zc=d-rn*math.sqrt(math.sqrt(kappa)*(p+1)/2);

PF = (p+1)*Ndot*S1*d*(math.sin(gamma))**3/math.pi;
n1 = Ndot/(cs*S2);

I1 = lambda r,z: (p+1)*Ndot*S1*d*(math.sin(gamma))**3/math.pi *Ndot/(cs*S2)*(d+r*math.cos(gamma))**p/((d**2+r**2+2*d*r*math.cos(gamma))**((p+3)/2))*z*r*(z+r*math.cos(gamma))/((z**2+r**2+2*z*r*math.cos(gamma))**2);
I2 = lambda r,z: (p+1)*Ndot*S1*d*(math.sin(gamma))**3/math.pi * ((p+1)*Ndot/(2*math.pi*v))/(d-z)**2 *(d+r*math.cos(gamma))**p/((d**2+r**2+2*d*r*math.cos(gamma))**((p+3)/2))*z*r*(z+r*math.cos(gamma))/((z**2+r**2+2*z*r*math.cos(gamma))**2);

R1 = integrate.dblquad(I1, 0, a, lambda x: zc, lambda x: d);
R2 = integrate.dblquad(I2, 0, a, lambda x: 0, lambda x: zc);
answer = R1[0] + R2[0];
f = answer/Ndot
print(f);
