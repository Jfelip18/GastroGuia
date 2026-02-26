import os
os.system("cls")


def AsignarRepartidorPorZona(zona):
    
    zona_lower = zona.lower()
    
    if "marbella" in zona_lower:
        return "Rory"
    elif "torices" in zona_lower:
        if "marbella" not in zona_lower:
            return "Fletcher"
        return "Rory"
    elif "bicentenario" in zona_lower:
        return "Tarapal"
    elif "centro" in zona_lower:
        return "Carlos"
    else:
        return "Carlos" 

# ============================================
# REGISTRO DE PEDIDOS
# ============================================
print("=" * 50)
print(" REGISTRO DE PEDIDOS ")
print("=" * 50)


def RegistroPedidos(nombre_completo, telefono, direccion, zona, pedido, precio, precio_domicilio):
    
    repartidor = AsignarRepartidorPorZona(zona)
    total = precio + precio_domicilio
    print(f"\nPedido registrado:")
    print(f"  Nombre completo: {nombre_completo}")
    print(f"  Teléfono: {telefono}")
    print(f"  Dirección: {direccion}")
    print(f"  Zona: {zona}")
    print(f"  Pedido: {pedido}")
    print(f"  Precio: ${precio:,}")
    print(f"  Precio domicilio: ${precio_domicilio:,}")
    print(f"  Total: ${total:,}")
    print(f"  Repartidor asignado: {repartidor}")
    return {
        "nombre_completo": nombre_completo,
        "telefono": telefono,
        "direccion": direccion,
        "zona": zona,
        "pedido": pedido,
        "precio": precio,
        "precio_domicilio": precio_domicilio,
        "total": total,
        "repartidor": repartidor
    }


pedidos = []

# ============================================
# MOTOR DE RUTAS
# ============================================

def MotorRutas(*args):
    
    rutas = []
    for i in range(0, len(args), 3):
        if i + 2 < len(args):
            zona = args[i]
            distancia_km = args[i + 1]
            precio_domicilio = args[i + 2]
            rutas.append({
                "zona": zona,
                "distancia_km": distancia_km,
                "precio_domicilio": precio_domicilio
            })
    return rutas

rutas = MotorRutas(
    "Marbella", 10, 10000,
    "Torices", 15, 25000,
    "Bicentenario", 30, 90000
)

def ObtenerPrecioDomicilio(zona):
    zona_lower = zona.lower()
    
    for ruta in rutas:
        if ruta["zona"].lower() in zona_lower or zona_lower in ruta["zona"].lower():
            return ruta["precio_domicilio"]
    
    return 0  

# ============================================
# ASIGNACIÓN DE REPARTIDORES
# ============================================

def AsignacionRepartidores(**kwargs):

    repartidores = []
    for nombre_repartidor, zona in kwargs.items():
        repartidores.append({
            "repartidor": nombre_repartidor,
            "punto_partida": "Centro",
            "zona_entrega": zona
        })
    return repartidores


repartidores = AsignacionRepartidores(
    Carlos="Centro",
    Rory="Marbella",
    Tarapal="Bicentenario",
    Fletcher="Torices"
)

# ============================================
# INGRESO DE PEDIDOS
# ============================================
print("\nIngrese los datos del pedido:")
nombre_completo = input("Nombre completo: ")
telefono = input("Teléfono: ")
direccion = input("Dirección: ")
zona = input("Zona: ")
pedido = input("Pedido: ")
precio = int(input("Precio: $"))
precio_domicilio = ObtenerPrecioDomicilio(zona)


pedido_registrado = RegistroPedidos(nombre_completo, telefono, direccion, zona, pedido, precio, precio_domicilio)
pedidos.append(pedido_registrado)


while True:
    continuar = input("\n¿Desea agregar otro pedido? (si/no): ").lower()
    if continuar == 'si':
        print("\nIngrese los datos del pedido:")
        nombre_completo = input("Nombre completo: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        zona = input("Zona: ")
        pedido = input("Pedido: ")
        precio = int(input("Precio: $"))
        precio_domicilio = ObtenerPrecioDomicilio(zona)
        pedido_registrado = RegistroPedidos(nombre_completo, telefono, direccion, zona, pedido, precio, precio_domicilio)
        pedidos.append(pedido_registrado)
    else:
        break

# ============================================
# RESUMEN DE PEDIDOS
# ============================================
print("\n" + "=" * 50)
print(" RESUMEN DE PEDIDOS ")
print("=" * 50)

if len(pedidos) > 0:
    for i, pedido in enumerate(pedidos, 1):
        print(f"\nPedido #{i}:")
        print(f"  Cliente: {pedido['nombre_completo']}")
        print(f"  Teléfono: {pedido['telefono']}")
        print(f"  Dirección: {pedido['direccion']}")
        print(f"  Zona: {pedido['zona']}")
        print(f"  Pedido: {pedido['pedido']}")
        print(f"  Precio: ${pedido['precio']:,}")
        print(f"  Precio domicilio: ${pedido['precio_domicilio']:,}")
        print(f"  Total a pagar: ${pedido['total']:,}")
        print(f"  Repartidor: {pedido['repartidor']}")
else:
    print("\nNo hay pedidos registrados.")

# ============================================
# RESUMEN DEL SISTEMA
# ============================================
print("\n" + "=" * 50)
print(" RESUMEN DEL SISTEMA ")
print("=" * 50)
print(f"\nTotal de pedidos registrados: {len(pedidos)}")
print(f"Total de rutas disponibles: {len(rutas)}")
print(f"Total de repartidores activos: {len(repartidores)}")

print("\n" + "-" * 50)
print(" REPARTIDORES (Todos parten del Centro) ")
print("-" * 50)
for repartidor in repartidores:
    print(f"  {repartidor['repartidor']}: Centro → {repartidor['zona_entrega']}")


