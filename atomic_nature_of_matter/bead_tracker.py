import math
import stdio
import sys
from blob import Blob
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    #command line inputs
    pixels=int(sys.argv[1])
    tau=float(sys.argv[2])
    delta=float(sys.argv[3])
    pic=Picture(sys.argv[4])
    frame=BlobFinder(pic,tau)
    prevBeads=frame.getBeads(pixels)

#command line inputs 5 and beyond
    for arg in sys.argv[5:]:
        #creating picture and blobfinder objects
        currPic=Picture(arg)
        currFrame=BlobFinder(currPic,tau)
        currBeads=currFrame.getBeads(pixels)
#for loops that test distance for each current bead and each previous bead
        for currBead in currBeads:
            smallestdistance=delta+1
            for prevBead in prevBeads:
                distance=currBead.distanceTo(prevBead)
                if distance <= delta and distance < smallestdistance:
                    smallestdistance=distance
            if smallestdistance <= delta:
                stdio.writef('%.4f\n',smallestdistance)
        prevBeads=currBeads
        #newline character to seperate outputs from different picture frames
        stdio.writeln()

if __name__ == "__main__":
    main()
