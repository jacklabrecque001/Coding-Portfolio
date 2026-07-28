import rsa
import stdio
import sys

# Entry point.
def main():
    n=sys.argv[1]
    d=sys.argv[2]
    binary_string=stdio.readAllInts()
    
    
    n_list=[]
    for i in n:
        if i.isdigit():
            n_list.append(i)
    n=int("".join(n_list))

    d_list=[]
    for j in d:
        if j.isdigit():
            d_list.append(j)
    d=int("".join(d_list))
            
    length=len(str(binary_string))
    
    width=rsa.bitLength(n)
    
    
    #decription=rsa.decrypt(binary_string[0],n,d)
    #new_string=chr(decription)
    #stdio.writeln(new_string)
    for i in range(0, length - 1, width):
        s = binary_string[i*width]
        y = rsa.bin2dec(s)
        x = rsa.decrypt(y, n, d)
        stdio.write(chr(x))
   
if __name__ == "__main__":
    main()