identificadores_usuarios = []


def validar_longitud(cadena, min_longitud, max_longitud):
    return min_longitud <= len(cadena) <= max_longitud


def validar_telefono(numero):
    return len(numero) == 10 and numero.isdigit()


def validar_correo(correo):
    return 5 <= len(correo) <= 50 and '@' in correo and '.' in correo


def obtener_nombre():
    nombre = input("Ingrese su(s) nombre(s): ")
    if validar_longitud(nombre, 5, 50):
        return nombre
    else:
        print("El nombre debe tener entre 5 y 50 caracteres.")
        return obtener_nombre()


def obtener_apellidos():
    apellidos = input("Ingrese sus apellidos: ")
    if validar_longitud(apellidos, 5, 50):
        return apellidos
    else:
        print("Los apellidos deben tener entre 5 y 50 caracteres.")
        return obtener_apellidos()


def obtener_telefono():
    telefono = input("Ingrese su número de teléfono (10 dígitos): ")
    if validar_telefono(telefono):
        return telefono
    else:
        print("El número de teléfono debe tener 10 dígitos.")
        return obtener_telefono()


def obtener_correo():
    correo = input("Ingrese su correo electrónico: ")
    if validar_correo(correo):
        return correo
    else:
        print("El correo electrónico debe tener entre 5 y 50 caracteres y ser válido.")
        return obtener_correo()


def registrar_usuario(numero):
    print("\nRegistrando usuario", numero)
    nombre = obtener_nombre()
    apellidos = obtener_apellidos()
    telefono = obtener_telefono()
    correo = obtener_correo()
    identificadores_usuarios.append(numero)
    print("Usuario registrado con éxito. Identificador:", numero)


cantidad_usuarios = int(input("¿Cuántos nuevos usuarios desea registrar? "))

for i in range(1, cantidad_usuarios + 1):
    registrar_usuario(i)

print("\nIdentificadores de usuarios registrados:", identificadores_usuarios)
