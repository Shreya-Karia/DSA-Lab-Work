#Shreya Karia AU2040076
class Array2D:
    def __init__(self,nrows,ncols):
        self.rows = [0]*nrows 
        for i in range( nrows ) :
            self.rows[i] = [0]*( ncols )
        #creates an array of desired size with all enties as zeoros

    def numRows(self):
        return len(self.rows)
    
    def numCols(self):
        return len(self.rows[0])

    def clear(self,value):
        c = self.numCols()
        self.rows = [value]*self.numRows()
        for i in range( self.numRows() ) :
            self.rows[i] = [value]*(c)
        return self
    
    def getitem(self,i1,i2):
        if 0<=i1<self.numRows() and 0<=i2<self.numCols():
            g = self.rows[i1][i2]
            return g
        else:
            return print("Invalid idex numbers.")
    
    def setitem(self,i1,i2,value):
        if 0<=i1<self.numRows() and 0<=i2<self.numCols():
            self.rows[i1][i2] = value
            return ""
        else:
            return print("Invalid index numbers.")

    
    def print2d( self ):
        for i in range( len(self.rows )):
            for j in range( len(self.rows[0]) ):
                print(self.rows[i][j],end=" ")
            print("")
        return("")
        




#Creating an array
arr1 = Array2D(3,3)
print("Original Matrix:")
arr1.print2d()
print(arr1.numRows())
#setting items
arr1.setitem(1,2,10)
arr1.setitem(1,2,4)
arr1.setitem(0,2,19)
arr1.setitem(0,1,1)
print("Modified Matrix:")
arr1.print2d()
print(arr1.getitem(0,1))

