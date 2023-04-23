import functools
import qrcode
import binascii

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

        for zidx, ascii in enumerate(key):

            # key轉成ASCii二進位
            # print(f"key[{idx}] = {ascii}")
            ascii = ord(ascii)
            key_bin = format(int(ascii), "b").zfill(8)
            # print(f"{ascii} = {key_bin}")

            # plaintext轉成ASCii二進位
            plain_ascii = ord(plaintext[zidx])
            plain_ascii = format(int(plain_ascii), "b").zfill(8)
            # print(f"plain[{idx}] = {num}")

            # key十位數代表形狀，個位數代表明文開始idx
            step = int(key_bin[4:8], 2)
            number = int(key_bin[0:4], 2)
            # print(str(pos)+' '+str(step))

            for plain_idx, pos in enumerate(Transposition_Cipher3D.key_shape[number]):       
                dim3D.append([pos[0], pos[1], zidx , plain_ascii[(plain_idx+step)%8]])
                
        

        sort_dim3D = sorted(dim3D, key=functools.cmp_to_key(Transposition_Cipher3D.__encrypt_cmp__))

        # for i in range(0,len(dim3D)):
        #     if i%8 == 0: print("-----------")
        #     print(dim3D[i], sort_dim3D[i])

        cipher_str = ""
        for bit in sort_dim3D:
            cipher_str += bit[3]

        cipher = ""
        cipher_hex = ""
        for idx in range(0 , len(cipher_str) , 8):
            # Getting the ASCII value
            cipher += chr(int(cipher_str[idx:idx+8],2))
            cipher_hex += "{:02x}".format(int(cipher_str[idx:idx+8],2))
            # print(type(int(cipher_str[idx:idx+8],2)))
            # print("{:02x}".format(int(cipher_str[idx:idx+8],2)) , int(cipher_str[idx:idx+8],2))

                
        return cipher_hex
        
    def decrypt(ciphertext:str , key:str) -> str:
        
        dim3D = [] # key先建構3維
        total_step = [] # 根據不同key密文要移動的步數
        total_cipher = "" # 密文排成一排

        for zidx, ascii in enumerate(key):

            # key轉成ASCii二進位
            # print(f"key[{idx}] = {ascii}")
            ascii = ord(ascii)
            key_bin = format(int(ascii), "b").zfill(8)
            # print(f"{ascii} = {key_bin}")

            # ciphertext(16進位)轉成ASCii二進位
            # print(ciphertext[2*zidx:2*zidx+2])
            

            byte_string = binascii.unhexlify(ciphertext[2*zidx:2*zidx+2])
            cipher_ascii = format(bin(int.from_bytes(byte_string, byteorder='big')).lstrip('0b')).zfill(8)
            total_cipher += cipher_ascii
            # print(f"plain[{zidx}] = {cipher_ascii}")

            # key十位數代表形狀，個位數代表明文開始idx
            step = int(key_bin[4:8], 2)
            total_step.append(step)
            number = int(key_bin[0:4], 2)
            # print(str(pos)+' '+str(step))

            # 畫出key的3D陣列
            for pos in Transposition_Cipher3D.key_shape[number]:       
                dim3D.append([pos[0], pos[1], zidx , ""])

         
        dim3D = sorted(dim3D, key=functools.cmp_to_key(Transposition_Cipher3D.__encrypt_cmp__))


        for idx, cipher_info in enumerate(dim3D):
            cipher_info[3] = total_cipher[idx]

        sort_dim3D = sorted(dim3D, key=functools.cmp_to_key(Transposition_Cipher3D.__decrypt_cmp__))


        cipher_to_plain = ""
        cipher_to_plain = cipher_to_plain.zfill(len(dim3D))


        plain_str = ""
        for idx in range(0, len(sort_dim3D)):        
            number = int(idx/8)*8 # 第幾個明文
            plain_str += sort_dim3D[number + (8-total_step[int(idx/8)]%8+idx)%8][3]

        # print(plain_str)
        
        plain = ""
        plain_hex = ""
        for idx in range(0 , len(plain_str) , 8):
            # Getting the ASCII value
            plain += chr(int(plain_str[idx:idx+8],2))
            plain_hex += "{:02x}".format(int(plain_str[idx:idx+8],2))
            # print("{:02x}".format(int(plain_str[idx:idx+8],2)) , int(plain_str[idx:idx+8],2))

                
        return plain_hex


    def __encrypt_cmp__(a:list, b:list) -> bool:
        if a[1] != b[1]:
            rel = 1 if a[1] > b[1] else -1
            return rel
        if a[0] != b[0]:
            rel = 1 if a[0] > b[0] else -1
            return rel
        if a[2] != b[2]:
            rel = 1 if a[2] < b[2] else -1
            return rel
        
    def __decrypt_cmp__(a:list, b:list) -> bool:
        if a[2] != b[2]:
            rel = 1 if a[2] > b[2] else -1
            return rel
        if a[0] != b[0]:
            rel = 1 if a[0] > b[0] else -1
            return rel
        if a[1] != b[1]:
            rel = 1 if a[1] > b[1] else -1
            return rel

def ciphertext_to_qrcode(cipher:str):
    img = qrcode.make(cipher)
    img.save("qrcode.png")
    # img.show()
   

# three = ('11','01','11','01','11')
# four  = ('0010','0110','1111','0010')
# five  = ('11','10','11','01','11')
# six   = ('11','10','10','11','11')
# seven = ('1111','1001','0001','0001')

# key_num = (three, four, five, six, seven)


plaintext = "a1095514"
key       = "aaaaaaaa"
print(f"plaintext = {plaintext}, key = {key}")

ciphertext_input = Transposition_Cipher3D.encrypt(plaintext, key)
ciphertext_to_qrcode(ciphertext_input)
plaintext_output = Transposition_Cipher3D.decrypt(ciphertext_input, key)
print(f"plaintext = {plaintext_output}")


