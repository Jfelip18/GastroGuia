import os
os.system("cls")

print("-----------------------------------" \
" Registro de pedidos " \
"-----------------------------------")

#Registro de pedidos
def RegistroPedidos(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

RegistroPedidos(Nombre = "Juan Carmona", Direccion = "Calle 10 #10-124", Zona = "Norte", Producto = "Camiseta", Precio = 25000)
