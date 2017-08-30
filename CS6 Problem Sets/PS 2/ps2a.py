

#
poly = (0.0, 0.0, 5.0, 9.3, 7.0) 
polyb = (-13.39, 0.0, 17.5, 3.0, 1.0)
x= -13


def evaluate_poly(poly,x):
    idx = 0
    finalans = 0
    for i in poly:
        ans=0
        ans= i* x**idx
        #print ans
        idx += 1
        finalans += ans
    return finalans

def compute_deriv(polyb):
    idx = 0
    deriv = []
    for i in polyb:
        ans=0
        ans= idx*i
        #print ans
        deriv.insert(idx,ans)
        idx+=1
    return tuple(deriv)



print(evaluate_poly(poly,x))

print compute_deriv(polyb)
