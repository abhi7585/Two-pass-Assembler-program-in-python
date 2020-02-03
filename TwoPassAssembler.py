"""
Instructions to the programmer:
1) Consider an hypothetical processor with approx. 20 assembly language instructions.
2) Define a standard MOT as shown below.
3) Write a ALP using few instructions from the MOT.
4) Use at least one address label in the program so it needs 2 passes for the assembly process.
5) Write a program using C to perform the assembly of the program.
6) Execute the program to generate the output of pass-1 & pass-2
7) In pass-1 output, develop Symbol Table (ST) & pass-1 output without reference to symbol.
8) In pass-2 output, generate the final machine code.
9) Output shall display in 3 columns namely Relative address, ALP instruction & machine code.

Mnemonics	  		Op-code			Size
MOV R				01			1
ADD R				02			1
SUB R				03			1
MUL R				04			1
DIV R				05			1
AND R				06			1
OR R				07			1		
ADD data			08			2
SUB data			09			2
MUL data			10			2
DIV data			11			2
AND data			12			2
OR data				13			2
LOAD address    		14			3
STORE address   		15			3
DCR R				16			1
INC R				17			1
JMP address			18			3
JNZ address			19			3
HALT				20			1


Instruction with data is 2 byte, first byte is the op-code byte & second byte is data byte itself.

Instruction with address is 3 byte (as address assumed here is 16 bit), 
first byte is the op-code byte & second & third bytes are the address bytes.

Input assembly language program:

Consider an ALP with following instructions:

MOV R
Next: ADD R
DCR R
JNZ Next 
STORE 2000 
HALT

Output after Pass-1:

Symbol Table (ST):

Symbol	Value (Address)
Next	  0001


Pass-1 machine code output without reference of the symbolic address:
Relative address	Instruction	Machine code
0	                MOV R	      01
1	                ADD R	      02
2	                DCR R	      16
3	                JNZ Next	  19, -- , --
6	                STORE 2000	15, 20, 00
9	                HALT	       20

Pass-2 output: Machine code output
Relative address	Instruction	Machine code
0	                MOV R	      01
1	                ADD R	      02
2	                DCR R	      16
3	                JNZ Next	  19, 00 , 01
6	                STORE 2000	15, 20, 00
9	                HALT	      20

"""

# PROGRAM :-

from sys import exit
motOpCode = {
    "MOV": 1,
    "A": 2,
    "S": 3,
    "M": 4,
    "D": 5,
    "AN": 6,
    "O": 7,
    "ADD": 8,
    "SUB": 9,
    "MUL": 10,
    "DIV": 11,
    "AND": 12,
    "OR": 13,
    "LOAD": 14,
    "STORE": 15,
    "DCR": 16,
    "INC": 17,
    "JMP": 18,
    "JNZ": 19,
    "HALT": 20
}

motSize = {
    "MOV": 1,
    "A": 1,
    "S": 1,
    "M": 1,
    "D": 1,
    "AN": 1,
    "O": 1,
    "ADD": 1,
    "SUB": 2,
    "MUL": 2,
    "DIV": 2,
    "AND": 2,
    "OR ": 2,
    "LOAD": 3,
    "STORE": 3,
    "DCR": 1,
    "INC": 1,
    "JMP": 3,
    "JNZ": 3,
    "HALT": 1
}

l = []
relativeAddress = []
machineCode = []
symbol = []
symbolValue = []
RA = 0
current = 0
count = 0
temp = []
n = int(input("Enter the no of instruction lines : "))
for i in range(n):
    instructions = input("Enter instruction line {} : ".format(i + 1))
    l.append(instructions)
l = [x.upper() for x in l]
for i in range(n):
    x = l[i]
    if "NEXT:" in x:
        s1 = ''.join(x)
        a, b, c = s1.split()
        a = a[:4]
        l[i] = b + " " + c
        symbol.append(a)
        x = l[i]
        if b in motOpCode:
            value = motOpCode.get(b)
            size = motSize.get(b)
            if len(str(size)) == 1:
                temp = "000" + str(size)
            elif len(str(size)) == 2:
                temp = "00" + str(size)
            elif len(str(size)) == 3:
                temp = "0"+str(size)
        else:
            print("Instruction is not in Op Code.")
            exit(0)
        symbolValue.append(temp)
        previous = size
        RA += current
        current = previous
        relativeAddress.append(RA)
        if c.isalpha() is True:
            machineCode.append(str(value))
        else:
            temp = list(b)
            for i in range(len(temp)):
                if count == 2:
                    temp.insert(i, ',')
                    count = 0
                else:
                    count = count + 1
            s = ''.join(temp)
            machineCode.append(str(value) + "," + s)
    elif " " in x:
        s1 = ''.join(x)
        a, b = s1.split()
        if a in motOpCode:
            value = motOpCode.get(a)
            size = motSize.get(a)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            if b.isalpha() is True:
                machineCode.append(str(value))
            else:
                temp = list(b)
                for i in range(len(temp)):
                    if count == 2:
                        temp.insert(i, ',')
                        count = 0
                    else:
                        count = count + 1
                s = ''.join(temp)
                machineCode.append(str(value) + "," + s)
        else:
            print("Instruction is not in Op Code.")
            exit(0)
    else:
        if x in motOpCode:
            value = motOpCode.get(x)
            size = motSize.get(x)
            previous = size
            RA += current
            current = previous
            relativeAddress.append(RA)
            machineCode.append(value)
        else:
            print("Instruction is not in Op Code.")
            exit(0)
print("Symbol Table  :  \n")
print("\n Symbol           Value(Address)")
for i in range(len(symbol)):
    print(" {}              {}".format(symbol[i], symbolValue[i]))

print("\n Pass-1 machine code output without reference of the symbolic address : \n")
print("Relative Address	Instruction	    OpCode")
for i in range(n):
    if "NEXT" in l[i]:
        print("{}                                 {}	              {}, - ".format(
            relativeAddress[i], l[i], machineCode[i]))
    else:
        print("{}                                 {}	              {} ".format(
            relativeAddress[i], l[i], machineCode[i]))

print("\n Pass-2 output: Machine code output \n ")
print("Relative Address	Instruction	    OpCode")
for i in range(n):
    if "NEXT" in l[i]:
        for j in range(len(symbol)):
            if "NEXT" in symbol[j]:
                pos = j
                print("{}                                 {}	              {} , {}".format(
                    relativeAddress[i], l[i], machineCode[i], symbolValue[pos]))
    else:
        print("{}                                 {}	              {} ".format(
            relativeAddress[i], l[i], machineCode[i]))



