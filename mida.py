import math

# get the input for n
n=input('Please input n:')
# convert string to float then to nearest integer
n=round(float(n))

# use loop to accumulate Sn
Sn=0
for i in range(n+1):
  Sn = Sn + 1/math.factorial(i)
# Sn+=1/math.factorial(i)

# print results on screeen
print(Sn)
print(math.exp(1))
