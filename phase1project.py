import os

string = str(input("Enter a string: "))                                                                                                                     #input of string to be encoded or decoded
key = str(input("Enter the key: "))                                                                                                                         #input of key that is used for encoding or decoding
# default values
algo = "AES"
mode = "CBC"
operation = "encrypt" 
command = "java -cp secure-properties-tool.jar com.mulesoft.tools.SecurePropertiesTool"                                                                     #command tool which receives the input values 


operation_dictionary = {1:'encrypt', 2:'decrypt'}                                                                                                           #Dictionary set of operations which the user can choose by entering integers such as 1 and 2                                                     
operation_index = int(input("Enter 1 for Encryption:\nEnter 2 for decryption:\n"))              
while(operation_index not in operation_dictionary.keys()):                                                                                                  #when the input i.e. the integers is not present in the operation dictionary keys then the loop follows
         print("Error")
         quit_flag = input("Press Q to quit\nPress any other key to continue:\n")
         if(quit_flag == 'Q'):                                                                                                                              #When the user enter a wrong input he is given an option to press Q in order to quit
             exit()
         operation_index = int(input("Enter 1 for encryption:\nEnter 2 for decryption:\n"))
        

operation = operation_dictionary.get(operation_index)                                                                                                        #accessing the value of operation dictionary with respect to the input which is operation index is given using get method
print(operation)                                                                                                                                             #prints operation 


algo_dictionary = {1:'AES', 2:'Blowfish', 3:'DES', 4:'DESede', 5:'RC2', 6:'RCA'}                                                                            #Dictionary set of algorithms which the user can choose by entering integers 
algo_index = int(input("Enter 1 for AES:\nEnter 2 for Blowfish:\nEnter 3 for DES:\nEnter 4 for DESede:\nEnter 5 for RC2:\nEnter 6 for RCA:\n"))
while(algo_index not in algo_dictionary.keys()):                                                                                                            #when the input i.e. the integers is not present in the algorithm dictionary keys then the loop follows
         print("Error")
         quit_flag = input("Press Q to quit\nPress any other key to continue:\n")                                                                           #When the user enter a wrong input he is given an option to press Q in order to quit
         if(quit_flag == 'Q'):
             exit()
         algo_index = int(input("Enter 1 for AES:\nEnter 2 for Blowfish:\nEnter 3 for DES:\nEnter 4 for DESede:\nEnter 5 for RC2:\nEnter 6 for RCA:\n"))
        

algorithm = algo_dictionary[algo_index]                                                                                                                     #accessing the value of algorithm dictionary with respect to the input which is algorithm index is given using bracket notation
print(algorithm)                                                                                                                                            #prints algorithm

mode_dictionary = {1:'CBC', 2:'CFB', 3:'ECB', 4:'OFB'}                                                                                                      #Dictionary set of mode which the user can choose by entering integers                                                
mode_index = int(input("Enter 1 for CBC mode:\nEnter 2 for CFB:\nENter 3 for ECB:\nEnter 4 for OFB:\n"))
while(mode_index not in mode_dictionary):                                                                                                                   #when the input i.e. the integers is not present in the mode dictionary keys then the loop follows
         print("Error")
         quit_flag = input("Press Q to quit\nPress any other key to continue:\n")          
         if(quit_flag == 'Q'):                                                                                                                              #When the user enter a wrong input he is given an option to press Q in order to quit
             exit()
         mode_index = int(input("Enter 1 for CBC mode:\nEnter 2 for CFB:\nEnter 3 for ECB:\nEnter 4 for OFB:\n"))
       

mode = mode_dictionary[mode_index]                                                                                                                          #accessing the value of mode dictionary with respect to the input which is mode index is given using bracket notation
print(mode)                                                                                                                                                 #prints mode
print("\n\n")
command = command+ " " + "string " + operation + " " + algorithm + " " + mode +" " + key + " " + string                                                     #command takes the value of this format
print(command)
a = os.popen(command)                                                                                                                                       #opens a pipe to command prompt that is , the operation is executed based on the mode and algorithm and stored value in variable "a"
print(a.read())                                                                                                                                             #outputs the value of variable "a" and it will be an encoded or decoded string