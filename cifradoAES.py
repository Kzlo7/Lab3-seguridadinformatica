from cryptography.fernet import Fernet
#Se necesita libreria 'cryptography'

#Cargar clave
def cargar_clave():
    return open("clave.key", "rb").read()

#Escribir y guardar clave
def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)


#Encriptar archivo
def encriptar(nombreArchivo, clave):
    f = Fernet(clave)
    with open(nombreArchivo, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nombreArchivo, "wb") as file:
        file.write(encrypted_data)

#Generar Clave
genera_clave()
#Cargar clave
clave = cargar_clave()

#Encriptar archivo
nombreArchivo = "text.txt"
encriptar(nombreArchivo, clave)