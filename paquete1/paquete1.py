class clientes:
    def __init__(self, nombre, email, edad, gustos):
        self.nombre=nombre
        self.email=email
        self.edad=edad
        self.gustos=gustos
        
    def comprar(self):
        print(f"El cliente {self.nombre} ha comprado en la tienda..")
    
    def enviar_email(self):
        print(f"se la ha enviado con su factura a su e-mail {self.email}")
        
clientes =clientes()

print (clientes.nombre)
print(clientes.email)
print(clientes.gustos)

clientes.comprar