#Shreya Karia AU2040076
nrows = 3
ncols = 3

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

    def sparrs(self):
        size = 0
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if (self.rows[i][j] != 0):
                    size = size + 1
        #Creating a matrix for sparse matrix representation
        arr = Array2D(size,3)
        m = 0
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if (self.rows[i][j] != 0):
                    arr.setitem(m,0,i)
                    arr.setitem(m,1,j)
                    arr.setitem(m,2,self.rows[i][j])
                    m = m + 1 #incrementing the row number in the sparse matrix representation
                    
        return arr


    def print2d( self ):
        for i in range( len(self.rows )):
            for j in range( len(self.rows[0]) ):
                print(self.rows[i][j],end=" ")
            print("")
        return("")




    def snumRows(self):
        return nrows
    def snumCols(self):
        return ncols

        
    def sgetitem(self,i1,i2):
        if 0<=i1<nrows and 0<=i2<ncols:
            for i in range(self.numRows()):
                if (self.rows[i][0] == i1):
                    for j in range(self.numCols()):
                        if (self.rows[i][1] == i2):
                            return self.rows[i][2]
                
            return 0
        else:
            return print("Invalid index numbers.")
        
    def ssetitem(self,i1,i2,value):
        if 0<=i1<nrows and 0<=i2<ncols:
            for i in range(self.numRows()):
                if (self.rows[i][0] == i1):
                    for j in range(self.numCols()):
                        if (self.rows[i][1] == i2):
                             self.rows[i][2] = value
                             return " "
            self.rows.append([i1,i2,value])
        else:
            return print("Invalid index numbers.")
        
    def scaleBy(self,val):
       for i in range(self.numRows()):
           a = self.rows[i][2]
           self.rows[i][2] = val*a
        
       return "  "
    
    def transpose(self):
         for i in range(self.numRows()):
                a = self.rows[i][0]
                self.rows[i][0] = self.rows[i][1]
                self.rows[i][1] = a
         return self

    def add(self,rhsMatrix):
        arrn = rhsMatrix.sparrs()
        if arrn.snumCols() == self.snumCols() and arrn.snumRows() == self.snumRows():
            arr = Array2D(0,3)
            for i in range(self.snumRows()):
                for j in range(self.snumCols()):
                    b = arrn.sgetitem(i,j)
                    a = self.sgetitem(i,j)
                    s = a + b
                    if s != 0:
                        arr.rows.append([i,j,s])
            return arr
        else:
            return "Addition not possible"
    
    def subtract(self,rhsMatrix):
        arrn = rhsMatrix.sparrs()
        if arrn.snumCols() == self.snumCols() and arrn.snumRows() == self.snumRows():
            arr = Array2D(0,3)
            for i in range(self.snumRows()):
                for j in range(self.snumCols()):
                    b = arrn.sgetitem(i,j)
                    a = self.sgetitem(i,j)
                    s = a - b
                    if s != 0:
                        arr.rows.append([i,j,s])
            return arr
        else:
            return "Subraction not possible"
    
    def multiply(self,rhsMatrix):
        arrn = rhsMatrix.sparrs()
        if self.snumCols() == rhsMatrix.numRows():
            arr = Array2D(0,3)
            for i in range(self.snumRows()):
                for j in range(rhsMatrix.numCols()):
                    s =  0
                    for k in range(rhsMatrix.numRows()):
                        b = arrn.sgetitem(i,k)
                        a = self.sgetitem(k,i)
                        s = s + a*b
                    if s != 0:
                        arr.rows.append([i,j,s])
            return arr
        else:
            return "Multiplication not possible!!"
        




#Creating an array
arr1 = Array2D(nrows,ncols)
print("Original Matrix:")
arr1.print2d()

print(arr1.numRows())
print(arr1.numRows())

#setting items
arr1.setitem(1,2,10)
arr1.setitem(1,2,4)
arr1.setitem(0,2,19)
arr1.setitem(0,1,1)
print("Modified Matrix:")
arr1.print2d()

# getting the sparse matrix representation
arrn = arr1.sparrs()
print("Sparse Matrix Representation:")
arrn.print2d()
print(" ")
arrt = arrn.transpose()
arrt.print2d()


#getting and setting item in sparse representation
print(arrn.sgetitem(1,4))
arrn.ssetitem(1,2,24)
arrn.print2d()
print(arrn.sgetitem(1,0))
print(" ")


arrn.scaleBy(2)
arrn.print2d()
print(" ")

arrn.transpose()
arrn.print2d()
print(" ")

#Creating a new matrix for adding purpose
arr2 = Array2D(nrows,ncols)
print("RHS Matrix:")
arr2.setitem(1,2,10)
arr2.setitem(1,1,42)
arr2.setitem(1,0,191)
arr2.setitem(0,1,11)
arr2.print2d()

#sparse for the same
arrn1 = arr2.sparrs()
print(" s1")
arrn.print2d()
print("s2 ")
arrn1.print2d()

#Adding
print(" add")
add = arrn.add(arr2)
add.print2d()
print(" ")

#Substracting
sub = arrn.subtract(arr2)
sub.print2d()
print(" ")

#Multiplying
mul = arrn.multiply(arr2)
print(mul)


arr3 = Array2D(ncols,nrows)
print("RHS Matrix:")
arr3.setitem(2,1,10)
arr3.setitem(1,1,42)
arr3.setitem(1,0,191)
arr3.setitem(0,1,11)
arr3.print2d()
print(" ")
arrn2 = arr3.sparrs()
arrn2.print2d()
print(" ")
mul1 = arrn.multiply(arr3)
mul1.print2d()




    