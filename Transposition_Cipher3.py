import functools

class Transposition_Cipher3D:
    three = ((0,0), (0,2), (0,4), (1,0), (1,1), (1,2), (1,3), (1,4))
    four  = ((0,0), (0,1), (0,2), (1,2), (2,0), (2,1), (2,2), (2,3))
    five  = ((0,0), (0,1), (0,2), (0,4), (1,0), (1,2), (1,3), (1,4))
    six   = ((0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,3), (1,4))
    seven = ((0,0), (0,1), (0,2), (1,0), (2,0), (2,1), (2,2), (2,3))
    
    key_shape = {3:three, 4:four, 5:five, 6:six, 7:seven}

    def encrypt(plaintext:str , key:str) -> str:

        #明文儲存的3維
        dim3D = []

        for idx, ascii in enumerate(key):

            # key轉成ASCii二進位
            print(f"key[{idx}] = {ascii}")
            ascii = ord(ascii)
            key_bin = format(int(ascii), "b").zfill(8)
            print(f"{ascii} = {key_bin}")

            # plain轉成ASCii二進位
            num = ord(plaintext[idx])
            num = format(int(num), "b").zfill(8)
            print(f"plain[{idx}] = {num}")

            # key十位數代表形狀，個位數代表明文開始idx
            step = int(key_bin[4:8], 2)
            pos = int(key_bin[0:4], 2)
            print(str(pos)+' '+str(step))

            for idx2, ii in enumerate(Transposition_Cipher3D.key_shape[pos]):       
                dim3D.append([ii[0], ii[1], idx , num[(idx2+step)%8]])
                

        dim3D = sorted(dim3D, key=functools.cmp_to_key(Transposition_Cipher3D.encrypt_cmp))

        cipher_str = ""
        for bit in dim3D:
            cipher_str += bit[3]

        cipher = ""
        for idx in range(0 , len(cipher_str) , 8):
            # Getting the ASCII value
            cipher += chr(int(cipher_str[idx:idx+8],2))
            print("{:02x}".format(int(cipher_str[idx:idx+8],2)) , int(cipher_str[idx:idx+8],2))

                
        return cipher
        
    def decrypt(plaintext:str , key:str) -> str:
        pass
    def encrypt_cmp(a:list, b:list) -> bool:
        if a[0] != b[0]:
            rel = 1 if a[0] > b[0] else -1
            return rel
        if a[1] != b[1]:
            rel = 1 if a[1] > b[1] else -1
            return rel
        if a[2] != b[2]:
            rel = 1 if a[2] < b[2] else -1
            return rel
    
    def decrypt_cmp(a:list, b:list) -> bool:
        if a[2] != b[2]:
            rel = 1 if a[2] < b[2] else -1
            return rel
        if a[1] != b[1]:
            rel = 1 if a[1] > b[1] else -1
            return rel
        if a[0] != b[0]:
            rel = 1 if a[0] > b[0] else -1
            return rel
        

    
# arr1 = np.array([[[2,17], [45, 78]], [[88, 92], [60, 76]],[[76,33],[20,18]]])
# print("Create 3-d array:",arr1)

# three = ('11','01','11','01','11')
# four  = ('0010','0110','1111','0010')
# five  = ('11','10','11','01','11')
# six   = ('11','10','10','11','11')
# seven = ('1111','1001','0001','0001')

# key_num = (three, four, five, six, seven)

#加密形狀
# three = ((0,0), (0,2), (0,4), (1,0), (1,1), (1,2), (1,3), (1,4))
# four  = ((0,0), (0,1), (0,2), (1,2), (2,0), (2,1), (2,2), (2,3))
# five  = ((0,0), (0,1), (0,2), (0,4), (1,0), (1,2), (1,3), (1,4))
# six   = ((0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,3), (1,4))
# seven = ((0,0), (0,1), (0,2), (1,0), (2,0), (2,1), (2,2), (2,3))

# key_shape = {3:three, 4:four, 5:five, 6:six, 7:seven}

# #明文 金鑰
# plaintext = "11"
# key =  "11"

# #明文儲存的3維
# dim3D = []

# for idx, ascii in enumerate(key):

#     # key轉成ASCii二進位
#     print(f"key[{idx}] = {ascii}")
#     ascii = ord(ascii)
#     key_bin = format(int(ascii), "b").zfill(8)
#     print(f"{ascii} = {key_bin}")

#     # plain轉成ASCii二進位
#     num = ord(plaintext[idx])
#     num = format(int(num), "b").zfill(8)
#     print(f"plain[{idx}] = {num}")

#     # key十位數代表形狀，個位數代表明文開始idx
#     step = int(key_bin[4:8], 2)
#     pos = int(key_bin[0:4], 2)
#     print(str(pos)+' '+str(step))

#     for idx2, ii in enumerate(key_shape[pos]):       
#         dim3D.append([ii[0], ii[1], idx , num[(idx2+step)%8]])
        

# dim3D = sorted(dim3D, key=functools.cmp_to_key(encrypt_cmp))



# cipher_str = ""
# for bit in dim3D:
#     cipher_str += bit[3]

# cipher = ""
# for idx in range(0 , len(cipher_str) , 8):
#     # Getting the ASCII value
#     cipher += chr(int(cipher_str[idx:idx+8],2))
#     print("{:02x}".format(int(cipher_str[idx:idx+8],2)) , int(cipher_str[idx:idx+8],2))

plaintext = "11"
key =  "11"

cipher = Transposition_Cipher3D.encrypt(plaintext, key)
# print(cipher)


 




