#!/usr/bin/python3


print ("                                                                       ")
print ("                                                                       ")
print ("            #####################################################" )       
print ("            #                                                   #" )        
print ("            #                   Logic Gate                    	#" ) 
print ("            #                                                   #" )                          
print ("            #             Automated Calculation Tool         	#" )        
print ("            #                                                   #" )        
print ("            #                   Version 1.0                   	#" )        
print ("            #                                                   #" )       
print ("            #            Author : Mohin Paramasivam             #" )       
print ("            #                                                   #" )       
print ("            #   						#")       
print ("            #                                       		#")
print ("            #####################################################" )       

print("                                                                   ")


#Get type of gates input from the user

gate=input("Please enter the name of logic gate : ")

##Get binary input from user

binary_A=input("Please enter the binary A input : ")

binary_B=input("Please enter the binary B input : ")


## Array for binary

binary_array_A=[]

binary_array_B=[]


#Check length of binary input for counter

binary_length_A=len(binary_A)
binary_length_B=len(binary_B)


#specify counter for loop

counter_A=0

while(counter_A!=binary_length_A):
	binary_array_A.append(binary_A[counter_A])
	counter_A=counter_A+1


counter_B=0

while(counter_B!=binary_length_B):
	binary_array_B.append(binary_B[counter_B])
	counter_B=counter_B+1




# Calculation for Logic Gate

if (gate=="AND" or gate=="and" or gate=="And"):
	formula="X = A * B "
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) or calculation_counter!=len(binary_array_B)):
		binary_X=int(binary_array_A[calculation_counter])*int(binary_array_B[calculation_counter])
		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")


elif (gate=="OR" or gate=="or" or gate=="Or"):
	formula="X = A + B "
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) or calculation_counter!=len(binary_array_B)):
		binary_X=int(binary_array_A[calculation_counter])+int(binary_array_B[calculation_counter])
		if binary_X==2:
			binary_X=1
		else:
			binary_X=binary_X

		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")

elif (gate=="NOT" or gate=="not" or gate=="Not"):
	formula="X = A Inverted "
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) ):
		binary_X=int(binary_array_A[calculation_counter])
		if(binary_X==1):
			binary_X=0
		elif(binary_X==0):
			binary_X=1

		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")

elif (gate=="NAND" or gate=="nand" or gate=="Nand"):
	formula="X = A * B (Inverted) "
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) or calculation_counter!=len(binary_array_B)):
		binary_X=int(binary_array_A[calculation_counter])*int(binary_array_B[calculation_counter])
		if(binary_X==1):
			binary_X=0
		elif(binary_X==0):
			binary_X=1

		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")

elif (gate=="NOR" or gate=="nor" or gate=="Nor"):
	formula="X = A + B  (Inverted)"
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) or calculation_counter!=len(binary_array_B)):
		binary_X=int(binary_array_A[calculation_counter])+int(binary_array_B[calculation_counter])
		if binary_X==2:
			binary_X=0
		elif binary_X==1:
			binary_X=0
		else:
			binary_X=1

		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")

elif (gate=="XOR" or gate=="xor" or gate=="Xor"):
	formula="X = A + B (Exclusive) "
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) or calculation_counter!=len(binary_array_B)):
		if(int(binary_array_A[calculation_counter])==1 and int(binary_array_B[calculation_counter])==1):
			binary_X=0
		elif(int(binary_array_A[calculation_counter])==0 and int(binary_array_B[calculation_counter])==0):
			binary_X=0
		else:
			binary_X=int(binary_array_A[calculation_counter])+int(binary_array_B[calculation_counter])
		
		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")


elif (gate=="XNOR" or gate=="xnor" or gate=="Xnor"):
	formula="X = A + B (Inverted Exclusive)"
	calculation_counter=0
	print("")
	print("Gate 		: ",gate.upper())
	print("")
	print("Formula 	: ",formula)
	print("")
	print("X 		: ",end="")

	while(calculation_counter!=len(binary_array_A) or calculation_counter!=len(binary_array_B)):
		
		if(int(binary_array_A[calculation_counter])==0 and int(binary_array_B[calculation_counter])==0):
			binary_X=1
		elif(int(binary_array_A[calculation_counter])==1 and int(binary_array_B[calculation_counter])==1):
			binary_X=1
		else:
			binary_X=int(binary_array_A[calculation_counter])+int(binary_array_B[calculation_counter])
			if(binary_X==1):
				binary_X=0
			else:
				binary_X=1
		
		
		

		print(binary_X,end="")
		calculation_counter=calculation_counter+1
	
	print("")
	print("")
