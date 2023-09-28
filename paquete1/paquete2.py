
def registro_usuario():

  usuario = input("Ingrese su nombre de usuario: "),

  contrasenia = input("Ingrese su contraseña: "),
  
  persona_usuario= {"usuario": usuario, "contrasenia": contrasenia}

  print("¡Bienvenido! Tu usuario es", usuario, "y tu contraseña ha sido registrada con éxito.")


persona_usuario = ""
def inicio_sesion():

  usuario_registrado = persona_usuario.get("usuario")

  contrasenia_registrada = persona_usuario.get("contrasenia")

  while True:

    usuario_ingresado = input("Ingrese su usuario: ")

    if usuario_ingresado != usuario_registrado:

      print("Usuario desconocido, vuelva a ingresar su usuario.")

    else:

      contrasenia_ingresada = input("Ingrese su contraseña: ")

      if contrasenia_ingresada != contrasenia_registrada:

        print("Contraseña incorrecta, intente nuevamente.")

      else:

        print("¡Inicio de sesión exitoso!")

        break



def main():

  registro_usuario (" Bienvenido/a, a continuación se le pedirá algunos datos para completar su perfil")

  inicio_sesion()
contrasenia_ = ""
  while True:

    print ("1 - Ingresar datos personales"
           "2 - ver mi contrasenia y usuario"
           "3 - Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
      datos_personales(),

    elif opcion == "2":

        ver_contrasenia_usuario()

    elif opcion == "3":

        print("¡Se desconectaá del sistema, vuelva pronto!")

        break

    else:

        print("pción no encontrada, vuelva a presionar los números que le indican ")


#menu_para_buscar_datos_de_usuarios:
usuario_registrado = ""
def menu_para_buscar_datos_de_usuarios ():

    usuario_a_buscar = input("ingrese el usuario que desee buscar")

    for usuario_registado in usuario_a_buscar:

      if usuario_registrado == usuario_a_buscar:

        print (f"{usuario_a_buscar} encontrado en la lista")

      else:
        print (f"{usuario_a_buscar} no encontrado en la lista")