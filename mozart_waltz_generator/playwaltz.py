import stdaudio
import stdio
import sys

Measures=stdio.readAllInts()
if len(Measures)!=32:
    stdio.writeln("A waltz must contain exactly 32 measures")
    sys.exit()

for i in range(17):
    if Measures[i] not in range(1,177):
        stdio.writeln("A minuet measure must be from [1, 176]")
        sys.exit()

for j in range(17,32):
    if Measures[j] not in range(1,177):
        stdio.writeln("A trio measure must be from [1, 96]")
        sys.exit()

for v in range(1,17):
    filename="data/M"+str(v)
    stdaudio.playFile(filename)

for y in range(17,32):
    filename="data/T"+str(y)
    stdaudio.playFile(filename)