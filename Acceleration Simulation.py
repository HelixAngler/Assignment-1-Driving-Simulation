# This Function is used for calculating the distance,S=V0T+(A*T^2)/2. V0=0m/s^2, so it become S=(A*T^2)/2)
def g(a, t):
    s=(a*(t**2))/2
    return s
#This Function is used for calculating final velocity and, for optional, velocity during process
def l(a, t):
    v=a*t
    return v
#This function is used for generating * that represents 10 m (every 10 m, it will add * to represents it)
def process():
    j=int(s/10)
    print("Duration: ",i,"Distance: ","*"*(j))
#This is the input and the constants for limit
y=int(input("duration"))
x=int(input("acceleration"))
z=int(input("distance"))
max=60
for i in range(y+1):
    s=g(x,i)
    process()
    v=l(x,i)
    f=chr(0x00B2)
#Comparison of speed limit
if v<=max:
    print("The person did not go over the speed limit. (Max speed was ",max,"m/s",f,")")
else:
    print("The person went over the speed limit. (Max speed was ",max,"m/s",f,")")
#Comparison whether the entity reached the destination or not
if s<=z:
    print("The person did not reach the destination. (Reached",s,"m)")
else:
    print("The person reached the destination. (Reached",s,"m)")