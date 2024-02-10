usuarios = []


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


def new_user():
    print("\nRegistrando nuevo usuario")
    nombre = obtener_nombre()
    apellidos = obtener_apellidos()
    telefono = obtener_telefono()
    correo = obtener_correo()
    usuario = {"Nombre": nombre, "Apellidos": apellidos, "Teléfono": telefono, "Correo": correo}
    usuarios.append(usuario)
    print("Usuario registrado con éxito.")


def show_user(id_usuario):
    if 1 <= id_usuario <= len(usuarios):
        usuario = usuarios[id_usuario - 1]
        print("\nInformación del usuario con ID", id_usuario)
        print("Nombre:", usuario["Nombre"])
        print("Apellidos:", usuario["Apellidos"])
        print("Teléfono:", usuario["Teléfono"])
        print("Correo:", usuario["Correo"])
    else:
        print("El ID de usuario ingresado no es válido.")


def edit_user(id_usuario):
    if 1 <= id_usuario <= len(usuarios):
        print("\nEditando información del usuario con ID", id_usuario)
        nombre = obtener_nombre()
        apellidos = obtener_apellidos()
        telefono = obtener_telefono()
        correo = obtener_correo()
        usuarios[id_usuario - 1] = {"Nombre": nombre, "Apellidos": apellidos, "Teléfono": telefono, "Correo": correo}
        print("Información del usuario actualizada con éxito.")
    else:
        print("El ID de usuario ingresado no es válido.")


def delete_user(id_usuario):
    if 1 <= id_usuario <= len(usuarios):
        del usuarios[id_usuario - 1]
        print("Usuario eliminado con éxito.")
    else:
        print("El ID de usuario ingresado no es válido.")


def list_users():
    print("\nIDs de usuarios registrados:")
    for i, usuario in enumerate(usuarios, start=1):
        print("ID:", i)


opciones_menu = {
    'A': new_user,
    'B': list_users,
    'C': show_user,
    'D': edit_user,
    'E': delete_user,
    'F': exit
}


while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("A.- Registrar nuevo usuario")
    print("B.- Listar IDs de usuarios registrados")
    print("C.- Ver información de un usuario")
    print("D.- Editar información de un usuario")
    print("E.- Eliminar usuario")
    print("F.- Finalizar programa")
    opcion = input("Seleccione una opción (A/B/C/D/E/F): ").upper()

    if opcion in opciones_menu:
        if opcion == 'C' or opcion == 'D' or opcion == 'E':
            id_usuario = int(input("Ingrese el ID del usuario: "))
            opciones_menu[opcion](id_usuario)
        elif opcion == 'F':
            opciones_menu[opcion]()
        else:
            opciones_menu[opcion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (A/B/C/D/E/F).")
