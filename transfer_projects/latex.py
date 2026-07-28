import zipfile
import collections
from collections import deque
zip_path = "/home/grinberg/primes/0000.zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    with z.open("009900000000_to_010000000000.txt"
) as f:
        last_lines = deque(maxlen=153)
        for line in f:
            last_lines.append(line.decode('utf-8').strip())
number = last_lines[0]
print(number)
