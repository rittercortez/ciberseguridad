import hashlib

def main():
    cifrado = input("Introduce el cifrado HASH a resolver: ")
    archivo = open("pwd.txt",'r')
    
    for i in archivo:
        x = i.strip("\n")
        x = bytes(x,'utf-8')
        
        sha1 = hashlib.sha1()
        sha1.update(x)
        sha1 = sha1.hexdigest()
        
        sha224 = hashlib.sha224()
        sha224.update(x)
        sha224 = sha224.hexdigest()
        
        sha512 = hashlib.sha512()
        sha512.update(x)
        sha512 = sha512.hexdigest()
        
        if cifrado == sha1:
            print(" Tu contraseña SHAI 1 es: "+ i)
            print(" Yo de ti cambio la contraseña! :P")
            break
        elif cifrado == sha224:
            print(" Tu contraseña SHAI 224 es: "+ i)
            print(" Yo de ti cambio la contraseña! :P")
            break
        elif cifrado == sha512:
            print(" Tu contraseña SHAI 512 es: "+ i)
            print(" Yo de ti cambio la contraseña! :P")
            break
            
           
        
if __name__ == '__main__':
    main()