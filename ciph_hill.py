import numpy as np
import math

def ciph_hill_encode():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    op_text = list(input("Введите сообщение, которое хотите зашифровать, заглавными буквами: "))
    n = int(input("Введите размерность ключевой матрицы: "))

    user_key = ''
    key = []

    for i in range (n):
        user_key+= str(input(f"Введите значения {i+1} строки ключевой матрицы через пробел:\n"))
        user_key+=' '
        matr_str = user_key.split(' ')
        key.append(matr_str)
        user_key = '' 
    
    for x in key:
        for y in x:
            if y == '':
                x.remove(y)

    for x in key:
        for i in range(len(x)):
            x[i] = int(x[i])                
    
    key = np.array(key)
    
    det = round((np.linalg.det(key)))%26
    
    if math.gcd(det, int(26))!=1 or det==0:
        print("Введено недопустимое значение ключа!")
    else:    
        for i in range (len(op_text)):
            op_text[i] = alphabet.index(op_text[i])
    
        encoded_text = []

        div = len(op_text)%n
      
        if div != 0:
            while len(op_text)%n!=0:
                op_text.append(int(0))
            
        for i in range (0, len(op_text), n):
        
            op_block = np.array(op_text[i:(i+n)])
            t_op_block = np.transpose(op_block)
            
            encod_block = (np.dot(key, t_op_block))%26
            
             
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

                 

def inversed(key):
    det = int(round(np.linalg.det(key)))
    key = np.linalg.inv(key) * det
    if det < 0:
        det = -det
        for i in range(len(key)):
            for j in range(len(key)):
                elem = -int(round(key[i][j]))
                while elem % det != 0 or elem / det < 0:
                    elem += 26
                key[i][j] = int(elem // det)
        return key
    else:
        for i in range(len(key)):
            for j in range(len(key)):
                elem = int(round(key[i][j]))
                while elem % det != 0 or elem / det < 0:
                    elem += 26
                key[i][j] = int(elem // det)
        return key

    
          
        
def ciph_hill_decode():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    encoded_text = list(input("Введите сообщение, которое хотите расшифровать, заглавными буквами: "))
    n = int(input("Введите размерность ключевой матрицы: "))

    user_key = ''
    key = []
    
    for i in range (n):
        user_key+= str(input(f"Введите значения {i+1} строки матрицы через пробел:\n"))
        user_key+=' '
        matr_str = user_key.split(' ')
        key.append(matr_str)
        user_key = '' 
    
    for x in key:
        for y in x:
            if y == '':
                x.remove(y)

    for x in key:
        for i in range(len(x)):
            x[i] = int(x[i])                

    key = np.array(key, dtype=np.int64)
    
    det = round((np.linalg.det(key)))%26
        
    if math.gcd(det, int(26))!=1 or det==0:
        print("Введено недопустимое значение ключа!")
    else:    
        for i in range (len(encoded_text)):
            encoded_text[i] = alphabet.index(encoded_text[i])
    
        op_text = []

        div = len(encoded_text)%n
      
        if div != 0:
            while len(encoded_text)%n!=0:
                encoded_text.append(int(0))

        inv_key = inversed(key)
        inv_key = np.array(inv_key, dtype = np.int64)
           
            
        for i in range (0, len(encoded_text), n):
        
            encod_block = np.array(encoded_text[i:(i+n)])
            t_encod_block = np.transpose(encod_block)
            
            op_block = (np.dot(inv_key, t_encod_block))%26
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


        
                   
        






# key = np.array([[5, 3, 2], [3, 4, 7], [9, 8, 5]])
# key1 = np.append(key, [int(5), int(3), int(2)])
# key2 = np.append(key1, [int(2), int(4), int(7)])
# print(key)

# a = list(input("Введите значения первой строки ключевой матрицы через пробел: "))

# for x in a:
#     if x == ' ':
#         a.remove(x)

# for i in range(len(a)):
#     a[i] = int(a[i])        
# print(a)

# b = list(input("Введите значения второй строки ключевой матрицы через пробел: "))
# for x in b:
#     if x == ' ':
#         b.remove(x)
# for i in range(len(b)):
#     b[i] = int(b[i])     
# print(b)

# key = np.array([a, b])    

# print(key)

# key = []
# key.append([1, 2]) [[1, 2], [3, 4]]
# print(key)
# print(key[0][1])



# n = int(input("Введите размерность ключевой матрицы: "))
# key = []

# for i in range (n):
#     key.append(i)

# for i in range (n):
#     key[i] = list(input(f"Введите значения {i+1} строки матрицы через пробел:\n"))


# for x in key:
#     for y in x:
#         if y == ' ':
#             x.remove(y)
#         else:
#             y = int(y)
# for x in key:
#     for i in range(len(x)):
#         x[i] = int(x[i])               

# key = np.array(key)

# print (key)



# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
#                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# op_text = list(input("Введите сообщение, которое хотите зашифровать, заглавными буквами: "))
# n = int(input("Введите размерность ключевой матрицы: "))
# block_list = []

# for i in range (len(op_text)):
#     op_text[i] = alphabet.index(op_text[i])

# if len(op_text)%n==0:
#     num_of_blocks = int(len(op_text)/n)
# else:
#     num_of_blocks = len(op_text)//n + 1        

# for i in range (num_of_blocks):
#     block = np.full(n, op_text[i:n])
#     block_list.append(block)


# print(block_list)

# op_text = [1, 2, 3, 4, 5, 6, 7 ,8]
# a = np.array(op_text[0:3])
# print(a)