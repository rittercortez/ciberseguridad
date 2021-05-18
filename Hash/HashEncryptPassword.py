import hashlib
def main():
    
    
     
    #print("#### CiFrar PassWord ####")
    clave = bytes(input("Introduce una  contraseña: "),'utf-8')
    print(clave)
    md5 = hashlib.md5()
    md5.update(clave)
    md5 = md5.hexdigest()
    print("Cifrado md5: "+ md5)

    sha1 = hashlib.sha1()
    sha1.update(clave)
    sha1 = sha1.hexdigest()
    print("Cifrado sha1: "+ sha1)

    sha224 = hashlib.sha224()
    sha224.update(clave)
    sha224 = sha224.hexdigest()
    print("Cifrado sha224: "+ sha224)

    sha512 = hashlib.sha512()
    sha512.update(clave)
    sha512 = sha512.hexdigest()
    print("Cifrado sha512: "+ sha512)
        
        

if __name__ == '__main__':
    main()