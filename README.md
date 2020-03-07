# Two-pass-Assembler-program-in-python
Program of Two pass Assembler using Python programming language. This program is general specific for the mentioned cases in the program.


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

```
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
```

Instruction with data is 2 byte, first byte is the op-code byte & second byte is data byte itself.

Instruction with address is 3 byte (as address assumed here is 16 bit), 
first byte is the op-code byte & second & third bytes are the address bytes.

Input assembly language program:

Consider an ALP with following instructions:
```
MOV R
Next: ADD R
DCR R
JNZ Next 
STORE 2000 
HALT
```
Output after Pass-1:

Symbol Table (ST):
```
Symbol	Value (Address)
Next	  0001
```

Pass-1 machine code output without reference of the symbolic address:
```
Relative address	Instruction	Machine code
0	                MOV R	      01
1	                ADD R	      02
2	                DCR R	      16
3	                JNZ Next	  19, -- , --
6	                STORE 2000	15, 20, 00
9	                HALT	       20
```
Pass-2 output: Machine code output
```
Relative address	Instruction	Machine code
0	                MOV R	      01
1	                ADD R	      02
2	                DCR R	      16
3	                JNZ Next	  19, 00 , 01
6	                STORE 2000	15, 20, 00
9	                HALT	      20
```
