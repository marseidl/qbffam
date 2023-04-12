#!/usr/bin/python
#Copyright (c) 2020 Martina Seidl, Johannes Kepler University Linz, Austria

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import sys

def error (message): 
    print("Error: " + message)
    sys.exit (1)


# equality formulas from
# Olaf Beyersdorff, Joshua Blinkhorn, Luke Hinde:
# Size, Cost, and Capacity: A Semantic Technique for Hard Random QBFs. 
# Logical Methods in Computer Science 15(1) (2019)
def EQ (n):

    if n < 2:
        error ("EQ: expect size < 2")

    print("p cnf " + str (3*n) + " " + str (2*n+1))

    # print the prefix

    print(("e"), end=' ')

    for i in range (n): 
        print(str (i+1), end=' ')

    print((0))

    print(("a"), end=' ')

    for i in range (n): 
        print(str (i+n+1), end=' ')

    print((0))
 
    print(("e"), end=' ')

    for i in range (n): 
        print(str (i+2*n+1), end=' ')

    print((0))

    # print the matrix

    for i in range (n): 
        print(str (i+1) + " " + str (i+n+1) + " -" + str (i+2*n+1), end=' ')
        print("0")
        print("-" + str (i+1) + " -" + str (i+n+1) + " -" + str (i+2*n+1), end=' ')
        print("0")

    for i in range (n): 
        print((i+2*n+1), end=' ')

    print("0")


# equality square formulas from 
# Olaf Beyersdorff, Joshua Blinkhorn, Meena Mahajan:
# Building Strategies into QBF Proofs. STACS 2019: 14:1-14:18
def EQ2 (n): 

    if n < 2:
        error ("EQ: expect size < 2")

    print("p cnf " + str (4*n+n*n) + " " + str (4*n*n+1))

    print("e", end=' ') 

    for i in range (n): 
        print(str (i+1) + " " + str (n+i+1), end=' ')

    print ("0")

    print("a", end=' ') 

    for i in range (n): 
        print(str (2*n+i+1) + " " + str (3*n+i+1), end=' ')
    
    print ("0")

    print("e", end=' ')

    for i in range (n): 
        for j in range (n): 
            print(str (4*n + i*n + j + 1), end=' ')

    print ("0")

    # print the matrix

    for i in range (n): 
        for j in range (n):
            print(str (i+1) + " " + str (n + j + 1), end=' ') 
            print(str (2 * n + i + 1) + " " + str (3 * n + j + 1), end=' ')
            print(str (4 * n + i * n + j + 1), end=' ')
            print ("0")

            print(str (i+1) + " -" + str (n + j + 1), end=' ') 
            print(str (2 * n + i + 1) + " -" + str (3 * n + j + 1), end=' ')
            print(str (4 * n + i * n + j + 1), end=' ')
            print ("0")
            
            print("-" + str (i+1) + " " + str (n + j + 1), end=' ') 
            print("-" + str (2 * n + i + 1) + " " + str (3 * n + j + 1), end=' ')
            print(str (4 * n + i * n + j + 1), end=' ')
            print ("0")

            print("-" + str (i+1) + " -" + str (n + j + 1), end=' ') 
            print("-" + str (2 * n + i + 1) + " -" + str (3 * n + j + 1), end=' ')
            print(str (4 * n + i * n + j + 1), end=' ')
            print ("0")

    for i in range (n): 
        for j in range (n): 
         print("-" + str (4*n + i*n + j + 1), end=' ') 
    print(0)

# CR formulas
# Mikolas Janota:
#On Q-Resolution and CDCL QBF Solving. SAT 2016: 402-418
def CR (n): 
    if n < 2:
        error ("CR: expect size < 2")


    print("p cnf " + str ((n+2) * n + 1) + " " + str (2 * n * n + 2)) 


    print("e", end=' ') 

    z = str ((n+2) * n +1)

    for i in range (n):
        for j in range (n): 
            print(str(i * n + j + 1), end=' ')
    print(0)
        
    print("a " + z + " 0")

    print("e", end=' ')

    for i in range (n): 
        print(str (n*n+i+1) + " " + str((n+1)*n+i+1), end=' ')
    print(0)

    for i in range (n):
        for j in range (n): 
            print(str (i*n+j+1) + " " + z + " " +str (n*n+i+1) + " 0")
            print("-" + str (i*n+j+1) + " -" + z + " " +str ((n+1)*n+j+1) + " 0")

    for i in range (n): 
        print("-" + (str (n*n+i+1)), end=' ')
    print("0")

    for i in range (n): 
        print("-" + (str ((n+1)*n+i+1)), end=' ')
    print("0")

# trapdoor formulas
# Olaf Beyersdorff, Benjamin Boehm:
# Understanding the Relative Strength of QBF CDCL Solvers and QBF Resolution. Electronic Colloquium on Computational Complexity (ECCC) 27: 53 (2020)
def TRAP (n) : 

    print("p cnf " + str ((n+1)*n*2 + 3) + " " + str (n * (n+1) * (n+1)  - (n-1)* (n+1) + 6 * n*(n+1)))

    w = str ((n+1)*n*2+1)
    u = str ((n+1)*n*2+2)
    t = str ((n+1)*n*2+3)

    print("e", end=' ')

    for i in range ((n+1)*n):
        print(str ((n+1)*n+i+1), end=' ')
    print("0")
    print("a " + w + " 0")
    print("e "+ t, end=' ') 
    for i in range ((n+1)*n):
        print(str (i+1), end=' ')
    print("0")
    print("a " + u + " 0")

    # matrix

    # pigeon hole

    for i in range (n+1): 
        for j in range (n): 
            print(str (i*n + j +1), end=' ') 
        print("0")

    for j in range (n): 
        for i1 in range (n+1): 
            for i2 in range (n+1) :
                if i1 != i2: 
                    print("-" + str (i1*n+j+1) + " -" + str (i2*n+j+1) + " 0")

    # rest
    for i in range (n*(n+1)): 
        o = n*(n+1)
        print("-" + str (i+1) + " " + str (o + i + 1) + " " + u + " 0")
        print(str (i+1) + " -" + str (o + i + 1) + " " + u + " 0")

        print(str (o+i+1) + " " + w + " " + t + " 0")
        print("-" + str (o+i+1) + " " + w + " " + t + " 0")
        print(str (o+i+1) + " -" + w + " " + t + " 0")
        print(str (o+i+1) + " " + w + " -" + t + " 0")

# PhD thesis of Florian Lonsing, JKU Linz, 2012 
def LONSING (n): 

    print("p cnf " + str (n * (n+1) + 6) + " " + str (n + 1 + n * (n+1) * (n+1) - (n * (n+1))+5))

    a = str (n * (n+1) + 1)
    b = str (n * (n+1) + 2)
    c = str (n * (n+1) + 3)
    d = str (n * (n+1) + 4)
    x = str (n * (n+1) + 5)
    y = str (n * (n+1) + 6)

    print("e" + " " + a + " " +b, end=' ')

    for i in range ((n+1)*n):
        print(str (i+1), end=' ')

    print("0")

    print("a " + x + " " + y + " 0") 
    print("e " + c + " " + d + " 0") 

    # pigeon hole

    for i in range (n+1): 
        for j in range (n): 
            print(str (i*n + j +1), end=' ') 
        print("0")

    for j in range (n): 
        for i1 in range (n+1): 
            for i2 in range (n+1) :
                if i1 != i2: 
                    print("-" + str (i1*n+j+1) + " -" + str (i2*n+j+1) + " 0")

    print(a + " " + x + " " + c + " 0")

    print(a + " " + b, end=' ') 
    for i in range (n * (n+1)): 
        print(i+1, end=' ')
    print(0)

    print(b + " " + y + " " + d + " 0")


    print(x + " " + c + " 0")
    print(x + " -" + c + " 0")



# Blocked equality formulas
# Joshua Blinkhorn, Olaf Beyersdorff:
# Proof Complexity of QBF Symmetry Recomputation. SAT 2019: 36-52
def blocked_EQ (n):

    if n < 2:
        error ("Blocked-EQ: expect size < 2")

    print("p cnf " + str (6*n+2) + " " + str (2*n+1+3*n+1))

    # print the prefix

    a = str (6*n+1)
    c = str (6*n+2)

    print(("e"), end=' ')


    print(a, end=' ')

    for i in range (3*n): 
        print(str (3*n + i + 1), end=' ')

    for i in range (n): 
        print(str (i+1), end=' ')

    print((0))

    print(("a"), end=' ')

    for i in range (n): 
        print(str (i+n+1), end=' ')

    print((0))
 
    print(("e"), end=' ')

    for i in range (n): 
        print(str (i+2*n+1), end=' ')

    print((0))

    print("a " + c + " 0")

    # print the matrix

    for i in range (n): 
        print(str (i+1) + " " + str (i+n+1) + " -" + str (i+2*n+1), end=' ')
        print("-" + a + " " + c + " 0")
        print("-" + str (i+1) + " -" + str (i+n+1) + " -" + str (i+2*n+1), end=' ')
        print("-" + a + " " + c + " 0")

    for i in range (n): 
        print((i+2*n+1), end=' ')
    print("-" + a + " " + c + " 0")

    print(a + " 0")

    for i in range (3 * n): 
        for j in range (i+1): 
            print((3*n + j +1), end=' ') 
        print((i+1), end=' ')
        print("0")


def printXOR (x, y, z): 

    print("-" + str (x) + " -" + str (y) + " -" + str (z) + " 0")
    print("-" + str (x) + " " + str (y) + " " + str (z) + " 0")
    print(str (x) + " -" + str (y) + " " + str (z) + " 0")
    print(str (x) + " " + str (y) + " -" + str (z) + " 0")



# parity formulas 
# Olaf Beyersdorff, Leroy Chew, Mikolas Janota:
# New Resolution-Based QBF Calculi and Their Proof Complexity. TOCT 11(4): 26:1-26:42 (2019)

def PARITY (n): 

    print("p cnf " + str (n*2) + " " + str (4 * (n-1) + 2))

    print("e", end=' ') 

    for i in range (n):
        print(str (i+1), end=' ') 

    print("0")

    z = str (n+1)

    print("a " + z + " 0")

    print("e", end=' ') 
    for i in range (n-1): 
        print(str (n + i + 2), end=' ')

    print("0")

    printXOR (1, 2, n+2)

    for i in range (n-2): 
        printXOR (n+i+2, i+3, n+i+3)
 
    print(z + " " + str (2 * n) + " 0")
    print("-" + z + " -" + str (2 * n) + " 0")


def PARITYTrue (n):
    print("p cnf " + str (n*2) + " " + str (4 * (n-1) + 2))

    print("a", end=' ') 

    for i in range (n):
        print(str (i+1), end=' ') 

    print("0")

    z = str (n+1)

    print("e " + z + " 0")

    print("e", end=' ') 
    for i in range (n-1): 
        print(str (n + i + 2), end=' ')

    print("0")

    printXOR (1, 2, n+2)

    for i in range (n-2): 
        printXOR (n+i+2, i+3, n+i+3)
 
    print(z + " " + str (2 * n) + " 0")
    print("-" + z + " -" + str (2 * n) + " 0")


def printXORl (x, y, z, a): 

    print("-" + str (x) + " -" + str (y) + " -" + str (z) + " " + str (a) + " 0")
    print("-" + str (x) + " " + str (y) + " " + str (z) + " " + str (a) + " 0")
    print(str (x) + " -" + str (y) + " " + str (z) + " " + str (a) + " 0")
    print(str (x) + " " + str (y) + " -" + str (z) + " " + str (a) + " 0")



# LD-parity formulas 
# Olaf Beyersdorff, Leroy Chew, Mikolas Janota:
# New Resolution-Based QBF Calculi and Their Proof Complexity. TOCT 11(4): 26:1-26:42 (2019)

def LQ_PARITY (n): 

    print("p cnf " + str (n*2) + " " + str (8 * (n-1) + 2))

    print("e", end=' ') 

    for i in range (n):
        print(str (i+1), end=' ') 

    print("0")

    z = (n+1)

    print("a " + str(z) + " 0")

    print("e", end=' ') 
    for i in range (n-1): 
        print(str (n + i + 2), end=' ')

    print("0")

    printXORl (1, 2, n+2, z)
    printXORl (1, 2, n+2, -z)

    for i in range (n-2): 
        printXORl (n+i+2, i+3, n+i+3, z)
        printXORl (n+i+2, i+3, n+i+3, -z)
 
    print(str(z) + " " + str (2 * n) + " 0")
    print("-" + str(z) + " -" + str (2 * n) + " 0")


def printXORu (x, y, z, a, b): 

    print("-" + str (x) + " -" + str (y) + " -" + str (z) + " " + str (a) + " " + str (b) +" 0")
    print("-" + str (x) + " " + str (y) + " " + str (z) + " " + str (a) + " " + str (b) + " 0")
    print(str (x) + " -" + str (y) + " " + str (z) + " " + str (a) + " " + str (b) + " 0")
    print(str (x) + " " + str (y) + " -" + str (z) + " " + str (a) + " " + str (b) + " 0")



# QU-parity formulas 
# Olaf Beyersdorff, Leroy Chew, Mikolas Janota:
# New Resolution-Based QBF Calculi and Their Proof Complexity. TOCT 11(4): 26:1-26:42 (2019)
def QU_PARITY (n): 

    print("p cnf " + str (n*2+1) + " " + str (8 * (n-1) + 2))

    print("e", end=' ') 

    for i in range (n):
        print(str (i+1), end=' ') 

    print("0")

    z1 = (n+1)
    z2 = (2*n+1)

    print("a " + str(z1) + " " + str (z2) + " 0")

    print("e", end=' ') 
    for i in range (n-1): 
        print(str (n + i + 2), end=' ')

    print("0")

    printXORu (1, 2, n+2, z1, z2)
    printXORu (1, 2, n+2, -z1, -z2)

    for i in range (n-2): 
        printXORu (n+i+2, i+3, n+i+3, z1, z2)
        printXORu (n+i+2, i+3, n+i+3, -z1, -z2)
 
    print(str(z1) + " " + str(z2) + " " + str (2 * n) + " 0")
    print("-" + str(z1) + " -" + str (z2) + " -" + str (2 * n) + " 0")





#Valeriy Balabanov, Magdalena Widl, Jie-Hong R. Jiang:
#QBF Resolution Systems and Their Proof Complexities. SAT 2014: 154-169
def KBKF_QU (n): 

    print("p cnf " + str (5 * n) +  " " + str (4*n+1))  

    for i in range (n): 
        print("e " + str (n + i +1) + " " + str (2*n +i +1) + " 0")
        print("a " + str (i+1) + " " + str (4*n+i+1) + " 0")

    print("e", end=' ') 
    for i in range (n): 
        print(str (3*n + i + 1), end=' ') 
    print("0")


    for i in range (n-1):
        print(str (n + i + 1) + " " + str (i+1) + " " + str (4*n+i + 1), end=' ') 
        print("-" + str (n+i+2) + " -" + str (2*n+i+2) + " 0")
 
        print(str (2*n + i + 1) + " -" + str (i+1) + " -" + str (4*n+i+1), end=' ') 
        print("-" + str (n+i+2) + " -" + str (2*n+i+2) + " 0")

    print(str (n + n) + " " + str (n) + " " + str (5*n), end=' ') 

    for i in range (n): 
        print("-" + str (3 * n + i + 1), end=' ') 
    print("0")

    print(str (2*n + n) + " -" + str (n) + " -" + str (5*n), end=' ') 

    for i in range (n): 
        print("-" + str (3 * n + i + 1), end=' ') 
    print("0")

    for i in range (n): 

        print(str (i+1) + " " + str (4*n+i+1) + " " +str (3*n+i+1) + " 0")
        print("-" + str (i+1) +" -" + str (4*n+i+1)+ " " + str (3*n+i+1) + " 0")

    print("-" + str (n + 1) + " -" + str (2*n + 1) + " 0")

#kleine buening et al. Q-Resolution Paper

#------------------------------------------------------------------------
#true KBKF formulas
def KBKFTrue (n):
   
    #counter for variables (first number - variable count)
    counter = 0
    # counter for initial variables
    counter2 = 0
 
    allvariables = 8*n+1
    
    print("p cnf " + str(8*n+1) + " " + str(14*n-1))

    for i in range (n): 
        print("a " + str (n + i +1) + " " + str (2*n +i +1) + " 0")
        print("e " + str (i+1) + " 0")
        counter += 3
        counter2 += 3

    print("a", end=' ')
    for i in range (n): 
        print(str (3*n + i + 1), end=' ') 
        counter += 1
        counter2 += 1
    print("0")

    newlyGvariables = allvariables - counter2

    print("e", end=' ')
    for i in range(newlyGvariables):
        print(str(counter2+i+1), end=' ')
    print("0")

    for i in range (n-1):
        
        print("-" + str(counter+1) + " -" + str (n + i + 1) + " 0")
        print("-" + str(counter+1) + " -" + str (i+1) + " 0")
        print("-" + str(counter+1) + " " + str (n+i+2) + " 0")
        print("-" + str(counter+1) + " " + str (2*n+i+2) + " 0")
        counter += 1

        print("-" + str(counter+1) + " -" + str (2*n + i + 1)+ " 0")
        print("-" + str(counter+1) + " " + str (i+1) + " 0")
        print("-" + str(counter+1) + " " + str (n+i+2) + " 0")
        print("-" + str(counter+1) + " " + str (2*n+i+2) + " 0")
        counter += 1

    print("-" + str(counter+1) + " -" + str (n + n)+ " 0")
    print("-" + str(counter+1) + " -" + str (n)+ " 0")
    
    for i in range (n): 
        print("-" + str(counter+1) + " " + str (3 * n + i + 1) + " 0") 
        
    counter += 1
    print("-" + str(counter+1) + " -" + str (2*n + n) + " 0")
    print("-" + str(counter+1) + " " + str (n) + " 0")

    for i in range (n): 
        print("-" + str(counter+1) + " " + str (3 * n + i + 1) + " 0") 
        
    counter += 1
    
    for i in range (n): 

        print("-" + str(counter+1) + " -" + str (i+1)+ " 0")
        print("-" + str(counter+1) + " -" + str (3*n+i+1)+ " 0")
        counter += 1

        print("-" + str(counter+1) + " " + str (i+1) + " 0")
        print("-" + str(counter+1) + " -" + str (3*n+i+1) + " 0")
        counter += 1

    print("-" + str(counter+1) + " " + str (n + 1) + " 0")
    print("-" + str(counter+1) + " " + str (2*n + 1) + " 0")
    
    for i in range(newlyGvariables):
        print(str(counter2+i+1), end=' ')
    print("0")
   
   
#------------------------------------------------------------------------
#true KBKF formulas with reordered quantifiers
def KBKFQRE (n):
   
    #counter for variables (first number - variable count)
    counter = 0
    # counter for initial variables
    counter2 = 0
 
    allvariables = 8*n+1
    originalVariables = 4*n
    
    
    print("p cnf " + str(8*n+1) + " " + str(14*n-1))

    for i in range (n): 
        print("a " + str (n + i +1) + " " + str (2*n +i +1) + " 0")
        if(i < 1):
            print("e " + str(allvariables) + " 0")
        else:
            print("e "+ str(originalVariables+1) + " " + str(originalVariables+2) + " 0") 
            originalVariables = originalVariables+2
        print("e " + str (i+1) + " 0")
        counter += 3
        counter2 += 3

    

    tempCounter = originalVariables + 3
    lastVar = 0
    for i in range (n-1): 
        print("a " + str (3*n + i + 1) + " 0") 
        lastVar = 3*n + i + 1
        print("e " + str(tempCounter) + " " + str(tempCounter+1) + " 0")
        tempCounter = tempCounter + 2
        counter += 1
        counter2 += 1
    
    counter = counter +1
    counter2 = counter2 +1
    newlyGvariables = allvariables - counter2
    
    print("a " + str(lastVar + 1) + " 0")

    print("e " + str(originalVariables+1) + " " + str(originalVariables+2) + " " + str(tempCounter) + " " + str(tempCounter+1) + " 0")

    for i in range (n-1):
        
        print("-" + str(counter+1) + " -" + str (n + i + 1) + " 0")
        print("-" + str(counter+1) + " -" + str (i+1) + " 0")
        print("-" + str(counter+1) + " " + str (n+i+2) + " 0")
        print("-" + str(counter+1) + " " + str (2*n+i+2) + " 0")
        counter += 1

        print("-" + str(counter+1) + " -" + str (2*n + i + 1)+ " 0")
        print("-" + str(counter+1) + " " + str (i+1) + " 0")
        print("-" + str(counter+1) + " " + str (n+i+2) + " 0")
        print("-" + str(counter+1) + " " + str (2*n+i+2) + " 0")
        counter += 1

    print("-" + str(counter+1) + " -" + str (n + n)+ " 0")
    print("-" + str(counter+1) + " -" + str (n)+ " 0")
    
    for i in range (n): 
        print("-" + str(counter+1) + " " + str (3 * n + i + 1) + " 0") 
        
    counter += 1
    print("-" + str(counter+1) + " -" + str (2*n + n) + " 0")
    print("-" + str(counter+1) + " " + str (n) + " 0")

    for i in range (n): 
        print("-" + str(counter+1) + " " + str (3 * n + i + 1) + " 0") 
        
    counter += 1
    
    for i in range (n): 

        print("-" + str(counter+1) + " -" + str (i+1)+ " 0")
        print("-" + str(counter+1) + " -" + str (3*n+i+1)+ " 0")
        counter += 1

        print("-" + str(counter+1) + " " + str (i+1) + " 0")
        print("-" + str(counter+1) + " -" + str (3*n+i+1) + " 0")
        counter += 1

    print("-" + str(counter+1) + " " + str (n + 1) + " 0")
    print("-" + str(counter+1) + " " + str (2*n + 1) + " 0")
    
    for i in range(newlyGvariables):
        print(str(counter2+i+1), end=' ')
    print("0")
 

#kleine buening et al. Q-Resolution Paper
def KBKF (n): 

    print("p cnf " + str (4 * n) +  " " + str (4*n+1))  

    for i in range (n): 
        print("e " + str (n + i +1) + " " + str (2*n +i +1) + " 0")
        print("a " + str (i+1) + " 0")

    print("e", end=' ') 
    for i in range (n): 
        print(str (3*n + i + 1), end=' ') 
    print("0")


    for i in range (n-1):
        print(str (n + i + 1) + " " + str (i+1), end=' ') 
        print("-" + str (n+i+2) + " -" + str (2*n+i+2) + " 0")
 
        print(str (2*n + i + 1) + " -" + str (i+1), end=' ') 
        print("-" + str (n+i+2) + " -" + str (2*n+i+2) + " 0")

    print(str (n + n) + " " + str (n), end=' ') 

    for i in range (n): 
        print("-" + str (3 * n + i + 1), end=' ') 
    print("0")

    print(str (2*n + n) + " -" + str (n), end=' ') 

    for i in range (n): 
        print("-" + str (3 * n + i + 1), end=' ') 
    print("0")

    for i in range (n): 

        print(str (i+1) + " " + str (3*n+i+1) + " 0")
        print("-" + str (i+1) + " " + str (3*n+i+1) + " 0")

    print("-" + str (n + 1) + " -" + str (2*n + 1) + " 0")

#Valeriy Balabanov, Magdalena Widl, Jie-Hong R. Jiang:
#QBF Resolution Systems and Their Proof Complexities. SAT 2014: 154-169
def KBKF_LD (n): 

    print("p cnf " + str (4 * n) +  " " + str (4*n+1))  

    for i in range (n): 
        print("e " + str (n + i +1) + " " + str (2*n +i +1) + " 0")
        print("a " + str (i+1) + " 0")

    print("e", end=' ') 
    for i in range (n): 
        print(str (3*n + i + 1), end=' ') 
    print("0")


    for i in range (n-1):
        print(str (n + i + 1) + " " + str (i+1), end=' ') 
        print("-" + str (n+i+2) + " -" + str (2*n+i+2), end=' ') 

        for j in range (n): 
            print("-" + str (3*n + j +1), end=' ')
        print("0")
 
        print(str (2*n + i + 1) + " -" + str (i+1), end=' ') 
        print("-" + str (n+i+2) + " -" + str (2*n+i+2), end=' ')
        
        for j in range (n): 
            print("-" + str (3*n + j +1), end=' ')
        print("0")

    print(str (n + n) + " " + str (n), end=' ') 

    for i in range (n): 
        print("-" + str (3 * n + i + 1), end=' ') 
    print("0")

    print(str (2*n + n) + " -" + str (n), end=' ') 

    for i in range (n): 
        print("-" + str (3 * n + i + 1), end=' ') 
    print("0")

    for i in range (n): 

        print(str (i+1) + " " + str (3*n+i+1), end=' ') 
        for j in range (n-i-1): 
            print("-" + str (3*n+i+j+2), end=' ')
        print("0")


        print("-" + str (i+1) + " " + str (3*n+i+1), end=' ')
        for j in range (n-i-1): 
            print("-" + str (3*n+i+j+2), end=' ')
        print("0")

    print("-" + str (n + 1) + " -" + str (2*n + 1), end=' ')
    for j in range (n): 
        print("-" + str (3*n + j +1), end=' ')
    print("0")


if (len (sys.argv) == 2): 
    f = sys.argv[1]
    if f != "-h": 
        error ("unknown option\nusage: qbffam.py -h")
    else: 
        print ("usage: qbffam.py <family> <size> or -h for help")
        print ("supported familes: ")
        print ("EQ          Equalities")
        print ("EQ2         Squared Equalities")
        print ("CR          Completion Principle")
        print ("TRAP        Trapdoor Familiy")
        print ("LONSING     Lonsing familiy")
        print ("BEQ         Blocked Equality Formula")
        print ("PARITY      Parity Formulas")
        print ("LQ_PARITY   Variation of Parity Formulas hard for LD")
        print ("QU_PARITY   Variation of Parity Formulas hard for QU")
        print ("KBKF        Kleine Buening et al Formulas")
        print ("KBKF_QU     Variation of Kleine Buening et al Formulas hard for QU")
        print ("KBKF_LD     Variation of Kleine Buening et al Formulas hard for LD")
        print ("KBKFTrue     Kleine Buening et al Formulas - Satisfiable")
        print ("PARITYTrue   Parity Formulas - Satisfiable")
        print ("KBKFQRE    Kleine Buening et al Formulas - Satisfiable and quantifier rearranged")
        sys.exit (0)


if len (sys.argv) != 3: 
    error ("invalid number of arguments\nusage: qbffam.py <family> <size> or -h for help")

try: 
    n = int (sys.argv[2])
except ValueError: 
    error ("size has to be an integer \nusage: qbffam.py <family> <size>")


f = sys.argv[1]



if f == "EQ": 
    EQ (n)
    sys.exit (0)

if f == "KBKFTrue": 
    KBKFTrue(n)
    sys.exit (0)
if f == "PARITYTrue": 
    PARITYTrue(n)
    sys.exit (0)
if f == "KBKFQRE": 
    KBKFQRE(n)
    sys.exit (0)

if f == "EQ2": 
    EQ2 (n)
    sys.exit (0)

if f == "CR": 
    CR (n)
    sys.exit (0)

if f == "TRAP": 
    TRAP (n)
    sys.exit (0)


if f == "LONSING": 
    LONSING (n)
    sys.exit (0)


if f == "BEQ": 
    blocked_EQ(n)
    sys.exit (0)


if f == "PARITY": 
    PARITY(n)
    sys.exit (0)

if f == "LQ_PARITY": 
    LQ_PARITY (n)
    sys.exit (0)

if f == "QU_PARITY": 
    QU_PARITY (n)
    sys.exit (0)

if f == "KBKF_QU": 
    KBKF_QU (n)
    sys.exit (0)

if f == "KBKF":
    KBKF(n)
    sys.exit (0)


if f == "KBKF_LD": 
    KBKF_LD (n)
    sys.exit (0)

error ("unknown family; use -h option to list families")
