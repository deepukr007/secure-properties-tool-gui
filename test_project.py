import os
import yaml


string = input("Enter the file name: ")
file_path = os.getcwd()
full_path = os.path.join(file_path, string)
index = str(input("Enter the key: "))
algo = "AES"
mode = "CBC"
operation = "encrypt" 
command = "java -cp secure-properties-tool.jar com.mulesoft.tools.SecurePropertiesTool"


operation_dictionary = {1:'encrypt', 2:'decrypt'}                                          
operation_index = int(input("Enter 1 for Encryption:\nEnter 2 for decryption:\n"))              
while(operation_index not in operation_dictionary.keys()):                                  
         print("Error")
         quit_flag = input("Press Q to quit\nPress any other key to continue")
         if(quit_flag == 'Q'):
             exit()
         operation_index = int(input("Enter 1 for encryption:\nEnter 2 for decryption:"))
        

operation = operation_dictionary.get(operation_index)      #operation_dictionary[operation_index]  also works , refer https://www.w3schools.com/python/ref_dictionary_get.asp   to know the advantage of get method vs []                     
print(operation)


algo_dictionary = {1:'AES', 2:'Blowfish', 3:'DES', 4:'DESede', 5:'RC2', 6:'RCA'}
algo_index = int(input("Enter 1 for AES:\nEnter 2 for Blowfish:\nEnter 3 for DES:\nEnter 4 for DESede:\nEnter 5 for RC2:\nEnter 6 for RCA:\n"))
while(algo_index not in algo_dictionary.keys()):
         print("Error")
         quit_flag = input("Press Q to quit\nPress any other key to continue:\n")
         if(quit_flag == 'Q'):
             exit()
         algo_index = int(input("Enter 1 for AES:\nEnter 2 for Blowfish:\nEnter 3 for DES:\nEnter 4 for DESede:\nEnter 5 for RC2:\nEnter 6 for RCA:\n"))
        

algorithm = algo_dictionary[algo_index]       
print(algorithm)

mode_dictionary = {1:'CBC', 2:'CFB', 3:'ECB', 4:'OFB'}
mode_index = int(input("Enter 1 for CBC mode:\nEnter 2 for CFB:\nENter 3 for ECB:\nEnter 4 for OFB:\n"))
while(mode_index not in mode_dictionary):
         print("Error")
         quit_flag = input("Press Q to quit\nPress any other key to continue:\n")
         if(quit_flag == 'Q'):
             exit()
         mode_index = int(input("Enter 1 for CBC mode:\nEnter 2 for CFB:\nEnter 3 for ECB:\nEnter 4 for OFB:\n"))
       

mode = mode_dictionary[mode_index]
print(mode)
print("\n\n")

new_dict = {}
with open(full_path) as file:
     file_input = yaml.load(file, Loader=yaml.FullLoader)
     for key, value in file_input.items():
         command = command+ " " + "string " + operation + " " + algorithm + " " + mode +" " + index + " " + value
         print(command)
         a = os.popen(command)                                                                                                                                       
         encrypted = a.read()                                                                                                                                    
         print(encrypted)
         new_dict[key] = encrypted
print(new_dict)
new_path = os.path.join(file_path, 'encrypted_'+string)
with open(new_path, 'w') as file:  
     document = yaml.dump(new_dict, file)

