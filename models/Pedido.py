import uuid
from datetime import datetime
from typing import Dict
from models.Usuario import Cliente
from models.Producto import Producto


class Pedido:
    """Representa un pedido realizado por un cliente."""

    def __init__(self, cliente: Cliente, productos: Dict[Producto, int]) -> None:
        self.id: str = str(uuid.uuid4())
        self.cliente: Cliente = cliente
        self.productos: Dict[Producto, int] = productos
        self.fecha: datetime = datetime.now()

    def calcular_total(self) -> float:
        return sum(prod.precio * cantidad for prod, cantidad in self.productos.items())

    def __str__(self) -> str:
        productos_str = "\n".join(
            [f"  - {prod.nombre} x{cantidad}" for prod, cantidad in self.productos.items()]
        )
        return (f"Pedido {self.id}\nCliente: {self.cliente.nombre}\n"
                f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Productos:\n{productos_str}\n"
                f"Total: {self.calcular_total():.2f}€")