#Python Program for simple interest formula = (P x T x R)/100

#created funcrion
def simple_interest(p,t,r):
    print("ThePrinciple is", p)
    print("The Time Period is", t)
    print("The rate is", r)
    
    #formula of Simple Interest
    si = (p*r*t)/100
    
    print("TheSimple interest is = ", si)
    return si


#call the function
simple_interest(3000,7,1)
     
#output
'''
ThePrinciple is 3000
The Time Period is 7
The rate is 1
TheSimple interest is =  210.0
'''


