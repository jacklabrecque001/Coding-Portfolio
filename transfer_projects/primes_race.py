# importing necessary libraries:
import subprocess
import zipfile
import collections
from collections import deque

# for subprossess getting file directories
cmd = [
    "ls", "/home/grinberg/primes/" , "-1"]
files = subprocess.Popen(cmd,stdout=subprocess.PIPE)
filenames = files.stdout.readlines()

mod_remainder_1=0
mod_remainder_2=0
major_events=0
count=0

# this first line selects one zipfile within /grinberg/primes
for zipnumber in filenames:

    # since i will be using this function on zipnumber multiple times, i have re-assigned
    # zipnumber to this function
    zipnumber = zipnumber.decode("utf-8").rstrip()

    # this next line ensures that no unwanted zip files get into the program
    if not zipnumber.startswith("0"):
        break

    # this is the zip path assigned to each zip file containing primes
    zip_path = "/home/grinberg/primes/"+zipnumber

    # this next line does NOT unzip any zip files. it reads the zip file without unzipping and allows
    # me to to be able to list the text files inside
    with zipfile.ZipFile(zip_path, 'r') as textfiles:

        # this next line turns textfiles into a list, then selects elements (text files) from it, one by one
        for files in textfiles.namelist():

            # this line takes the textfile and opens it
            with textfiles.open(files) as f:

                # this line selects each number within the text file one by one
                for line in f:
                    count += 1
                    # this line decides if a major event is happening
                    if mod_remainder_1==mod_remainder_2:
                        major_events+=1
                        print("a major event happened with mod1 at " +str(mod_remainder_1)+" and mod2 at "+str(mod_remainder_2)+".")

                    # this is the code that decides if an entry has remainder 1 or 2
                    entry = int(line.decode("utf-8"))
                    
                    # i included remainder 0 because the number 3 has remainder 0, but is niether remainder 1 or 2
                    if entry%3==0:
                        continue
                    elif entry%3==1:
                        mod_remainder_1 += 1
                    else:
                        mod_remainder_2 += 1
                        
                        
print(major_events)
print(mod_remainder_1)
print(mod_remainder_2)


