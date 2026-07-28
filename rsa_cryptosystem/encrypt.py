import rsa
import stdio
import sys

# Entry point.
def main():
    e=sys.argv[1]
    
    e_list=[]
    for i in e:
       
        if i.isdigit():
            e_list.append(i)
            

    n=sys.argv[2]
    n_list=[]
    for j in n:
        if j.isdigit():
            n_list.append(j)
    e=int("".join(e_list))
    
    n=int("".join(n_list))
        
    
    width=rsa.bitLength(n)
    string=stdio.readAll()
    #stdio.writeln(string)
    string_array=[]
    #for i in string:
   #     string_array=string_array+[i]
   # stdio.writeln(string_array)
    
    
   # for c in string_array:
    for c in string:
        #if c==string_array[-1]:
          #  break
        x=ord(c)
        encription=rsa.encrypt(x,n,e)
        binary_string=rsa.dec2bin(encription,width)
        stdio.write(str(binary_string))
    


    

if __name__ == "__main__":
    main()
