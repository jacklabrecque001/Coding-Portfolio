import stdarray
import stdrandom
import stdio

minuetMeasures=stdarray.create2D(11,16)

for i in range(11):
    for j in range(16):
        minuetMeasures[i][j]=stdio.readInt()


for a in range(16):
    die_roll=stdrandom.uniformInt(1,7)+stdrandom.uniformInt(1,7)
    stdio.write(str(minuetMeasures[die_roll-2][a]) + " ")
    


trioMeasures=stdarray.create2D(6,16)

for m in range(6):
    for n in range(16):
        trioMeasures[m][n]=stdio.readInt()

for b in range(16):
    die_roll_2=stdrandom.uniformInt(1,7)
    stdio.write(str(trioMeasures[die_roll_2-1][b])+" ")
    


