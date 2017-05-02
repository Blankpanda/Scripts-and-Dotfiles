import time, sys
def main():
    iterations =  10000000
    start = time.time()
    atan = gen_atan(iterations,1)
    end = time.time()

    print("\n"+str(4.0*atan))
    print("Total time in seconds: "  + str(end - start))

def gen_atan(iter,num_at):
    sum = 1
    expon = 3
    isPos = False

    for k in range(1,iter):        
        if isPos:
            sum = sum + (exp(num_at,expon)/expon)
            isPos = False
        else:
            sum = sum - (exp(num_at,expon)/expon)
            isPos = True
            
        expon = expon + 2            
    return sum
    
def exp(base,exponent):
    root = base
    for i in range(1,exponent):
        base = root * base
    return base
    
if __name__ == '__main__':
    main()
