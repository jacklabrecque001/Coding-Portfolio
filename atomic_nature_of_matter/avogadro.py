import math
import stdio


# Entry point.
def main():
    #Nsm^-2
    eta=9.135*10**(-4)
    #JK^-1mol^-1
    rho=0.5*10**(-6)
    #kelvin
    t=float(297)
    r=8.31457
    var=0
    #take all stadnard input
    n=stdio.readAllFloats()
    #formulas formulas formulas....
    for i in n:
        meters=i*0.175*10**(-6)
        var += meters**2/(2*len(n))
    d=var
    k=d*6*math.pi*eta*rho/t
    n_a=r/k
    stdio.writef('%e',n_a)

if __name__ == "__main__":
    main()
