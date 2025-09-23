#it makes a table and fills it with letters in zigzag order
def maketable(text,key):
    #cleaning the text
    text = text.lower()
    text = text.replace(' ','')
    text_list = [x for x in text if "a" <= x <= "z"]
    #defining column and rows of table
    row  = key
    col = len(text_list)
    table = [[' ' for x in range(col)] for y in range(row)]
    #up for placing characters in forward order in rows and down for backward order
    up = 0
    down =  row-2
    i=0
    #loop to fill text characters in table
    while (i<len(text_list)):
            if(up< row):
                  table[up][i]=text_list[i]
                  up+=1
                  i += 1
            elif(down>0):
                  table[down][i]=text_list[i]
                  down-=1
                  i += 1
            else :
                up=0
                down=row-2
    up-=1
    #array to fill x at the end if text does not end at last column of last row
    while(table[-1][-1]!='x'):
       if down>-1 and up==row-1:
         table[down].append('x')
         for x in range(row):
             if x!=down:
                 table[x].append(' ')
         down-=1
       elif up<row-1:
          table[up+1].append('x')
          for x in range(row):
             if x != up+1:
                 table[x].append(' ')
          up += 1
       else:
           up = 0
    for row in table:
        print(row)
    return table
#It combines the the text row wise
def give_encrypted_text(table):
    encrypted_text = ''

    for row in table:
        encrypted_text += ''.join(row)
    return encrypted_text.replace(" ","")
#Now this function fills table for decryption
def filltable_decryption(encypted_text,key):
    decrypt_table = [['' for x in range(len(encypted_text))] for y in range(key)]
    up = 0
    down = key - 2
    i = 0
    #it fills * in zigzag order in table
    while (i<len(encypted_text)):
            if(up< key):
                  decrypt_table[up][i]="*"
                  up+=1
                  i += 1
            elif(down>0):
                  decrypt_table[down][i]="*"
                  down-=1
                  i += 1
            else :
                up=0
                down=key-2
    return decrypt_table
#it palces encrypted text chars in place of * and then picks it in zig zag pattern to generate decrypted text
def decrypt_text(encrypted_text,decrypt_table):
    char_index = 0
    for row in range(len(decrypt_table)):
        for col in range(len(encrypted_text)):
            if (decrypt_table[row][col]=='*'):
                decrypt_table[row][col] = encrypted_text[char_index]
                char_index += 1
    up = 0
    down = key - 2
    i = 0
    decrypted_text = ""
    while (i<len(encrypted_text)):
            if(up< key):
                  decrypted_text+=decrypt_table[up][i]
                  up+=1
                  i += 1
            elif(down>0):
                  decrypted_text+=decrypt_table[down][i]
                  down-=1
                  i += 1
            else :
                up=0
                down=key-2
    return decrypted_text
#this is menu for the user to interact

while(True):
    input1 = int(input("Press 1 to encrypt text\n"
                "Press 2 to decrypt text\n"
                "Press 3 to exit"))
    if input1 == 1:
        sentence = input("Give sentence to encrypt.")

        key = int(input("Give key."))
        if key > 2 or key <(len(sentence)/2):
            encrypt_table = maketable(sentence,key)
            print( give_encrypted_text(encrypt_table))
        else:
            print("invalid key")
    elif input1 == 2:
        encrypted_text = input("Give sentence to decrypt.")
        key = int(input("Give key."))
        if key > 2 or key < (len(encrypted_text) / 2):
            decrypt_table = filltable_decryption(encrypted_text,key)
            print(decrypt_text(encrypted_text,decrypt_table))
        else:
            print("invalid key.")
    elif input1 == 3:
        break
