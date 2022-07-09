buses = sorted(buses)
passengers = sorted(passengers)
j = 0
for i in range(0,len(buses)):
    count = capacity
    while j<len(passengers) and passengers[j]<=buses[i] and count>0:
        count-=1
        j+=1

b = passengers[j-1]
p = set(passengers)

if count!=0:
    b = buses[-1]

while b in p:
    b-=1
return b
