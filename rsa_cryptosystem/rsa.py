import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    p_list=_primes(lo, hi)
    q_list=_primes(lo, hi)
    p=_choice(p_list)
    q=_choice(q_list)
    
    n=p*q
    m=(p-1)*(q-1)
    e=1
    while m%e==0:
        e=_choice(_primes(2,m))
        
    d=1
    while (e*d-1)%m !=0:
        d=d+1
    return(n,e,d)

    
# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    encryption=(x**e)%n
    #stdio.writeln(encryption)
    return encryption

# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    decryption=(y**d)%n
    return decryption
    _primes
# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2

# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))

# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)

# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    #finding the primes
    list=[]
    list_of_primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    list_of_nums=[]

 #   for i in range(2,hi):
  #      list_of_nums=list_of_nums+[i]
   #     i=i+1
    #
#    while len(list_of_nums)!=0:
 #       list_of_primes.append(list_of_nums[0])
  #      first_prime=list_of_nums[0]
   #     for num in list_of_nums:
    #        
     #       if num%first_prime==0:
      #          list_of_nums.remove(num)
#
    for prime in list_of_primes:
        if prime<lo:
            continue
        elif prime>=hi:
            break
        else:
            list.append(prime)
    return(list)
# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    stdrandom.sample(a,k)
# Returns a random item from the list a.
def _choice(a):
    
    random_item=stdrandom.choice(a)
    
    #random_item=5
    return(random_item)

# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))

if __name__ == "__main__":
    _main()
