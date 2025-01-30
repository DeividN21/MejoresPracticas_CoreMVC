from heladeria.models import Proveedor, CategoriaProv
# Builder para crear objetos Proveedor paso a paso
class ProveedorBuilder:
    def __init__(self):
        self.proveedor = Proveedor()  # Inicializar un objeto Proveedor vacío

    def set_nombre(self, nombre):
        self.proveedor.nombreProveedor = nombre
        return self  # Retornar la instancia para encadenar métodos

    def set_categoria(self, categoria_id):
        self.proveedor.categoriaProv = CategoriaProv.objects.get(pk=categoria_id)
        return self

    def set_costo_insumo(self, costo):
        self.proveedor.costoInsumo = costo
        return self

    def set_tiempo_entrega(self, tiempo):
        self.proveedor.tiempoEntrega = tiempo
        return self

    def build(self):
        return self.proveedor  # Retornar el objeto Proveedor construido