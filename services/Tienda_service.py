from typing import Dict, List, Optional
from models.Usuario import Usuario, Cliente, Administrador
from models.Producto import Producto
from models.Pedido import Pedido


class TiendaService:
    """Servicio central para la gestión de la tienda."""

    def __init__(self) -> None:
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    # -------------------- Usuarios --------------------
    def registrar_usuario(self, tipo: str, nombre: str, correo: str, direccion: Optional[str] = None) -> Usuario:
        if tipo == "cliente":
            usuario = Cliente(nombre, correo, direccion or "")
        elif tipo == "admin":
            usuario = Administrador(nombre, correo)
        else:
            raise ValueError("Tipo de usuario no válido")
        self.usuarios[usuario.id] = usuario
        return usuario

    # -------------------- Productos --------------------
    def agregar_producto(self, producto: Producto) -> None:
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> bool:
        return self.productos.pop(producto_id, None) is not None

    def listar_productos(self) -> List[Producto]:
        return list(self.productos.values())

    # -------------------- Pedidos --------------------
    def realizar_pedido(self, cliente_id: str, productos_cantidades: Dict[str, int]) -> Optional[Pedido]:
        cliente = self.usuarios.get(cliente_id)
        if not cliente or not isinstance(cliente, Cliente):
            print("El usuario no existe o no es un cliente.")
            return None

        productos_seleccionados: Dict[Producto, int] = {}
        for prod_id, cantidad in productos_cantidades.items():
            producto = self.productos.get(prod_id)
            if not producto or not producto.hay_stock(cantidad):
                print(f"Producto {prod_id} no disponible o sin stock suficiente.")
                return None
            productos_seleccionados[producto] = cantidad

        # Descontar stock
        for producto, cantidad in productos_seleccionados.items():
            producto.actualizar_stock(-cantidad)

        pedido = Pedido(cliente, productos_seleccionados)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_usuario(self, usuario_id: str) -> List[Pedido]:
        return [pedido for pedido in self.pedidos if pedido.cliente.id == usuario_id]

