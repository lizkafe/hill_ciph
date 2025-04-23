import math
import numpy as np
from ciph_hill import inversed
def rec_hill_encode():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    op_text = list(input("Введите сообщение, которое хотите зашифровать, заглавными буквами: "))
    n = int(input("Введите размерность ключевой матрицы: "))

    user_key1 = ''
    key1 = []

    user_key2 = ''
    key2 = []

    for i in range (n):
        user_key1+= str(input(f"Введите значения {i+1} строки ключевой матрицы 1 через пробел:\n"))
        user_key1+=' '
        matr_str1 = user_key1.split(' ')
        key1.append(matr_str1)
        user_key1 = '' 
    
    for x in key1:
        for y in x:
            if y == '':
                x.remove(y)

    for x in key1:
        for i in range(len(x)):
            x[i] = int(x[i])                
    
    key1 = np.array(key1)
    
    det1= round((np.linalg.det(key1)))%26


    for i in range (n):
        user_key2+= str(input(f"Введите значения {i+1} строки ключевой матрицы 2 через пробел:\n"))
        user_key2+=' '
        matr_str2 = user_key2.split(' ')
        key2.append(matr_str2)
        user_key2 = '' 
    
    for x in key2:
        for y in x:
            if y == '':
                x.remove(y)

    for x in key2:
        for i in range(len(x)):
            x[i] = int(x[i])                
    
    key2 = np.array(key2)
    
    det2 = round((np.linalg.det(key2)))%26

        
    if math.gcd(det1, int(26))!=1 or math.gcd(det2, int(26))!=1 or det1==0 or det2==0:
        print("Введено недопустимое значение ключа!")
    else:    
        for i in range (len(op_text)):
            op_text[i] = alphabet.index(op_text[i])
    
        encoded_text = []

        div = len(op_text)%n
      
        if div != 0:
            while len(op_text)%n!=0:
                op_text.append(int(0))  


        list_of_keys = []

        for i in range(len(op_text)):
            list_of_keys.append(i)

        list_of_keys[0] = key1
        list_of_keys[n] = key2
                
        for i in range (n+n, int(len(op_text)), n):
            new_key = np.dot(list_of_keys[i-n], list_of_keys[i-n-n])%26
            list_of_keys[i] = new_key



        for i in range (0, len(op_text), n):
        
            op_block = np.array(op_text[i:(i+n)])
            t_op_block = np.transpose(op_block)
            encod_block = (np.dot(list_of_keys[i], t_op_block))%26
                       
            encoded_text.append(encod_block)
        

        encoded_text_end = []

        for array in encoded_text:
            for el in array:
                encoded_text_end.append(el%26)
        for i in range (len(encoded_text_end)):
            encoded_text_end[i] = alphabet[encoded_text_end[i]]
            
        encoded_text_ready=''.join(encoded_text_end)
        print('Ваш шифртекст: ', encoded_text_ready)  
        return encoded_text_ready
    

def rec_hill_decode():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encoded_text = list(input("Введите сообщение, которое хотите расшифровать, заглавными буквами: "))
    n = int(input("Введите размерность ключевой матрицы: "))

    user_key1 = ''
    key1 = []

    user_key2 = ''
    key2 = []

    for i in range (n):
        user_key1+= str(input(f"Введите значения {i+1} строки ключевой матрицы 1 через пробел:\n"))
        user_key1+=' '
        matr_str1 = user_key1.split(' ')
        key1.append(matr_str1)
        user_key1 = '' 
    
    for x in key1:
        for y in x:
            if y == '':
                x.remove(y)

    for x in key1:
        for i in range(len(x)):
            x[i] = int(x[i])                
    
    key1 = np.array(key1)
    
    det1= round((np.linalg.det(key1)))%26


    for i in range (n):
        user_key2+= str(input(f"Введите значения {i+1} строки ключевой матрицы 2 через пробел:\n"))
        user_key2+=' '
        matr_str2 = user_key2.split(' ')
        key2.append(matr_str2)
        user_key2 = '' 
    
    for x in key2:
        for y in x:
            if y == '':
                x.remove(y)

    for x in key2:
        for i in range(len(x)):
            x[i] = int(x[i])                
    
    key2 = np.array(key2)
    
    det2 = round((np.linalg.det(key2)))%26
        
    if math.gcd(det1, int(26))!=1 or det1==0 or math.gcd(det2, int(26))!=1 or det2==0:
        print("Введено недопустимое значение ключа!")
    else:    
        for i in range (len(encoded_text)):
            encoded_text[i] = alphabet.index(encoded_text[i])
    
        op_text = []

        div = len(encoded_text)%n
      
        if div != 0:
            while len(encoded_text)%n!=0:
                encoded_text.append(int(0))

        inv_key1 = inversed(key1)
        inv_key1 = np.array(inv_key1, dtype = np.int64)
        inv_key2 = inversed(key2)
        inv_key2 = np.array(inv_key2, dtype = np.int64)
        list_of_inv_keys = []
        for i in range(len(encoded_text)):
            list_of_inv_keys.append(i)

        list_of_inv_keys[0] = inv_key1
        list_of_inv_keys[n] = inv_key2
        for i in range (n+n, int(len(encoded_text)), n):
            new_inv_key = np.dot(list_of_inv_keys[i-n-n], list_of_inv_keys[i-n])%26
            list_of_inv_keys[i] = new_inv_key

        print(list_of_inv_keys[0])
        print(list_of_inv_keys[n])
        print(np.dot(inv_key1, inv_key2))    

                     
        for i in range (0, len(encoded_text), n):
        
            encod_block = np.array(encoded_text[i:(i+n)])
            t_encod_block = np.transpose(encod_block)
            
            op_block = (np.dot(list_of_inv_keys[i], t_encod_block))%26
            op_text.append(op_block)

        op_text_end = []

        for array in op_text:
            for el in array:
                op_text_end.append(el%26)
        for i in range (len(op_text_end)):
            op_text_end[i] = alphabet[op_text_end[i]]
            
        op_text_ready=''.join(op_text_end)
        print('Ваш шифртекст: ', op_text_ready)  
        return op_text_ready


        
