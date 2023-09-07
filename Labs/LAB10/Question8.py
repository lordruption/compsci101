def get_encrypted(word, key):
    password_location = []
    encrypted = []
    for char in word:
        if 'a' <= char <= 'z':
            password_location.append(ord(char) - ord('a'))
    for i in password_location:
        encrypted.append(key[i])
    return ''.join(encrypted)
    



        










encrypted = get_encrypted('bank', 'ydfvwxhaqoibsjnreglzptckum')
print('bank', encrypted)
