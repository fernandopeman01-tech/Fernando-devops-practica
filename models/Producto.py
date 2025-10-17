import uuid
class Producto:
    """Se hace una clase base para productos de la tienda"""
    
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.precio: float = precio
        self.stock: int = stock

    def hay_stock(self, cantidad: int) -> bool:
        """Se verifica si hay suficiente stock disponible"""
        return self.stock >= cantidad

    def actualizar_stock(self, cantidad: int) -> None:
        """se actualiza el stock del producto (positivo = entrada, negativo = salida)."""
        self.stock += cantidad

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.precio:.2f}€ (Stock: {self.stock})"


class ProductoElectronico(Producto):
    """se hace la  garantía."""

    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int) -> None:
        super().__init__(nombre, precio, stock)
        self.garantia_meses: int = garantia_meses

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} - {self.precio:.2f}€ "
                f"(Stock: {self.stock}, Garantía: {self.garantia_meses} meses)")


class ProductoRopa(Producto):
    """talla y color"""

    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color

    def __str__(self) -> str:
        return (f"[{self.id}] {self.nombre} - {self.precio:.2f}€ "
                f"(Stock: {self.stock}, Talla: {self.talla}, Color: {self.color})")
