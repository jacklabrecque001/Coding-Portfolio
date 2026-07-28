import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture
from color import Color

# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        self._blobs = []
        #assigning variables
        self.marked = stdarray.create2D(pic.width(), pic.height())
        self.pic=pic
        self.tau=tau
        #finding first white pixel in image then calls recursive function _findblob
        for i in range(self.pic.width()):
            for j in range(self.pic.height()):
                y=self.pic.get(i,j)
                if Color.luminance(y)>=self.tau:
                    blob=Blob()
                    self._findBlob(self.pic, i, j, blob)
                    if blob.mass()>0:
                        self._blobs += [blob]
        
        
    def getBeads(self, pixels):
        
        return[blob for blob in self._blobs if blob.mass()>=pixels]
    
    # Identifies a blob using depth-first search. The parameters are the picture (pic), luminance
    # threshold (tau), pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob
    # being identified (blob).
    #using recursion calls itself on the N E S W pixels and finds all the pixels in the blob
    def _findBlob(self, pic:Picture, i, j, blob):
        if i not in range(pic.width()):
            return
        if j not in range(pic.height()):
            return
        if self.marked[i][j]==None:
            x=self.pic.get(i,j)
            if Color.luminance(x)>=self.tau:
                self.marked[i][j]=True
                #self._pixelcounter += 1
                #stdio.writeln(str(i)+"i "+str(j)+"j")
                self._findBlob(pic, i+1, j, blob)
                self._findBlob(pic, i, j+1, blob)
                self._findBlob(pic, i-1, j, blob)
                self._findBlob(pic, i, j-1, blob)
                blob.add(i,j)
            else:
                self.marked[i][j]=False
            
        

    

        

        
        

# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))


if __name__ == "__main__":
    _main()
