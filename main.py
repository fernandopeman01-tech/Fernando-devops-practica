from models.Producto import ProductoElectronico, ProductoRopa
from Services.Tienda_service import TiendaService


def main():
    tienda = TiendaService()

    # Registrar usuarios
    cliente1 = tienda.registrar_usuario("cliente", "Ana", "ana@mail.com", "Calle 1")
    cliente2 = tienda.registrar_usuario("cliente", "Luis", "luis@mail.com", "Calle 2")
    cliente3 = tienda.registrar_usuario("cliente", "Marta", "marta@mail.com", "Calle 3")
    admin = tienda.registrar_usuario("admin", "Admin", "admin@mail.com")

    # Crear productos
    p1 = ProductoElectronico("Portátil", 1200.0, 5, 24)
    p2 = ProductoElectronico("Móvil", 800.0, 10, 12)
    p3 = ProductoRopa("Camiseta", 20.0, 50, "M", "Azul")
    p4 = ProductoRopa("Pantalón", 35.0, 30, "L", "Negro")
    p5 = ProductoRopa("Chaqueta", 60.0, 15, "M", "Rojo")

    # Añadir productos al inventario
    for prod in [p1, p2, p3, p4, p5]:
        tienda.agregar_producto(prod)

    print("\n--- Inventario ---")
    for prod in tienda.listar_productos():
        print(prod)

    # Simular pedidos
    print("\n--- Realizando pedidos ---")
    pedido1 = tienda.realizar_pedido(cliente1.id, {p1.id: 1, p3.id: 2})
    pedido2 = tienda.realizar_pedido(cliente2.id, {p2.id: 1, p4.id: 1})
    pedido3 = tienda.realizar_pedido(cliente3.id, {p3.id: 3, p5.id: 1})

    for pedido in [pedido1, pedido2, pedido3]:
        if pedido:
            print(pedido)

    # Histórico de pedidos de un cliente
    print("\n--- Histórico de pedidos de Ana ---")
    pedidos_ana = tienda.listar_pedidos_usuario(cliente1.id)
    for pedido in pedidos_ana:
        print(pedido)

    # Stock actualizado
    print("\n--- Inventario actualizado ---")
    for prod in tienda.listar_productos():
        print(prod)


if __name__ == "__main__":
    main()
