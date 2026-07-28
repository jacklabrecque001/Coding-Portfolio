import rsa
import stdio
import sys

# Entry point.
def main():

    lo=int(sys.argv[1])
    hi=int(sys.argv[2])
    n_e_d=rsa.keygen(lo, hi)
    stdio.writeln(n_e_d)

if __name__ == "__main__":
    main()
