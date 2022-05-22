#Python Program for compound interest
'''
Formula to calculate compound interest annually is given by: 
A = P(1 + R/100) t 
Compound Interest = A – P 
Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span
'''

def compound_interest(p,r,t):
    
    print("ThePrinciple is", p)
    print("The Time Period is", t)
    print("The rate is", r)
    
    
    #formula for Compound Interest
    
    a = p*(pow((1 + r / 100), t))

    
    ci = a - p
    print("The Compound Interest is", ci )
    
    return ci


#calling Function
compound_interest(10000, 10.25, 5)
     
'''
Output

ThePrinciple is 10000
The Time Period is 5
The rate is 10.25
The Compound Interest is 6288.946267774416

'''

