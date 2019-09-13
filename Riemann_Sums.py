"""
Author: Peter Watson

estimate area under a curve usng riemann sums

has function mid_rule for the midpoint rule
trap_rule for the trapezoid rule, and
left_riemann_sum for the left riemann sum

error function currently does not work
"""
import math

def mid_rule(f, a, b, n):
    tempA = a
    delta_x = ((b-a)/n)                     #range of integral divided by number of rectangles
    
    reimannSum = 0
    for i in range(0, n):
        reimannSum = reimannSum + (delta_x * ( f(tempA + (delta_x/2))))         #delta_x times f(midpoint)
        tempa = (tempA + delta_x)         #increases a by delta_x every time function runs
    return (reimannSum)

def trap_rule(f, a, b, n):
    tempA = a
    delta_x = ((b-a)/n)                  #range of integral divided by number of rectangles
    
    reimannSum = 0
    for i in range(0, n):
        reimannSum = reimannSum + (.5 * (delta_x) * (f(tempA) + f(tempA + delta_x)))        #area of each trapezoid
        tempA += delta_x     #increases starting a by delta_x every time function runs
        
    return (float(reimannSum))
    
    
def left_riemann_sum(f, a, b, n):       #define funtion left_riemann_sum, uses parameters f, a, b, and n
    delta_x = ((b-a)/n)                 #compute delta x as upper bound- lower bound over number of rectangles

    riemannSum = 0
    for i in range(0, n):        
        riemannSum = riemannSum + f(a + i * delta_x) * delta_x      #increases a by multiplying it by i
        
    return (float(riemannSum))

def f(x):
    return 3.0 * (math.exp(1/x))

#print (trap_rule(f, 1, 2, 1000000))
#mid_rule(f, 1, 2, 4)
#left_riemann_sum(f, 1, 2, 4)

#test = math.log(2)      #log base e
#print (test)
print ('trapezoid rule error')
error_trap = abs(((trap_rule(f, 1, 2, 1000000)) - (trap_rule(f, 1, 2, 4))))
print (error_trap)
print ('')
print('midpoint rule error')
error_mid = abs(((mid_rule(f, 1, 2, 1000000)) - (mid_rule(f, 1, 2, 4))))
print (error_mid)
