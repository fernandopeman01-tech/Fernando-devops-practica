import uuid


class Usuario:
    """Clase base para usuarios de la tienda."""

    def __init__(self, nombre: str, correo: str) -> None:
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.correo: str = correo

    def is_admin(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} ({self.correo})"


class Cliente(Usuario):
    """Usuario cliente con dirección postal."""

    def __init__(self, nombre: str, correo: str, direccion: str) -> None:
        super().__init__(nombre, correo)
        self.direccion: str = direccion

    def __str__(self) -> str:
        return f"Cliente {self.nombre} , su correo {self.correo} y direccion {self.direccion}"


class Administrador(Usuario):
    """Usuario administrador."""

    def is_admin(self) -> bool:
        return  

    def __str__(self) -> str:
        return f"Administrador {self.nombre} y {self.correo}"
