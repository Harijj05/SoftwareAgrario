"""Catalog service - Business logic for reference data."""

from data.repositories.catalogo_repo import CatalogoRepository


class CatalogoService:
    """Service for catalog operations."""

    # ============ Tipo Hortaliza ============
    @staticmethod
    def get_all_tipo_hortaliza():
        """Get all hortaliza types."""
        return CatalogoRepository.get_all_tipo_hortaliza()

    @staticmethod
    def search_hortaliza(nombre):
        """Search hortaliza by name."""
        return CatalogoRepository.search_tipo_hortaliza(nombre)

    @staticmethod
    def get_tipo_hortaliza_full():
        """Get hortaliza types with details."""
        return CatalogoRepository.get_tipo_hortaliza_full()

    @staticmethod
    def create_hortaliza(nombre, descripcion, imagen):
        """Create hortaliza type."""
        return CatalogoRepository.create_tipo_hortaliza(nombre, descripcion, imagen)

    @staticmethod
    def update_hortaliza(codigo, nombre, descripcion, imagen):
        """Update hortaliza type."""
        return CatalogoRepository.update_tipo_hortaliza(codigo, nombre, descripcion, imagen)

    @staticmethod
    def delete_hortaliza(codigo):
        """Delete hortaliza type."""
        return CatalogoRepository.delete_tipo_hortaliza(codigo)

    # ============ Tipo Suelo ============
    @staticmethod
    def get_all_tipo_suelo():
        """Get all soil types."""
        return CatalogoRepository.get_all_tipo_suelo()

    @staticmethod
    def get_tipo_suelo_full():
        """Get soil types with details."""
        return CatalogoRepository.get_tipo_suelo_full()

    @staticmethod
    def create_suelo(nombre, descripcion, imagen):
        """Create soil type."""
        return CatalogoRepository.create_tipo_suelo(nombre, descripcion, imagen)

    @staticmethod
    def update_suelo(codigo, nombre, descripcion, imagen):
        """Update soil type."""
        return CatalogoRepository.update_tipo_suelo(codigo, nombre, descripcion, imagen)

    @staticmethod
    def delete_suelo(codigo):
        """Delete soil type."""
        return CatalogoRepository.delete_tipo_suelo(codigo)

    # ============ Clima ============
    @staticmethod
    def get_all_clima():
        """Get all climate types."""
        return CatalogoRepository.get_all_clima()

    @staticmethod
    def get_clima_full():
        """Get climate types with details."""
        return CatalogoRepository.get_clima_full()

    @staticmethod
    def create_clima(nombre, grados, descripcion, imagen):
        """Create climate type."""
        return CatalogoRepository.create_clima(nombre, grados, descripcion, imagen)

    @staticmethod
    def update_clima(codigo, nombre, grados, descripcion, imagen):
        """Update climate type."""
        return CatalogoRepository.update_clima(codigo, nombre, grados, descripcion, imagen)

    @staticmethod
    def delete_clima(codigo):
        """Delete climate type."""
        return CatalogoRepository.delete_clima(codigo)

    # ============ Tipo Cultivo ============
    @staticmethod
    def get_all_tipo_cultivo():
        """Get all crop types."""
        return CatalogoRepository.get_all_tipo_cultivo()

    @staticmethod
    def get_tipo_cultivo_full():
        """Get crop types with details."""
        return CatalogoRepository.get_tipo_cultivo_full()

    @staticmethod
    def create_tipo_cultivo(nombre, meses_primera, meses_rutinaria):
        """Create crop type."""
        return CatalogoRepository.create_tipo_cultivo(nombre, meses_primera, meses_rutinaria)

    @staticmethod
    def update_tipo_cultivo(cultivo_id, nombre, meses_primera, meses_rutinaria):
        """Update crop type."""
        return CatalogoRepository.update_tipo_cultivo(cultivo_id, nombre, meses_primera, meses_rutinaria)

    @staticmethod
    def delete_tipo_cultivo(cultivo_id):
        """Delete crop type."""
        return CatalogoRepository.delete_tipo_cultivo(cultivo_id)

    # ============ Gestion Cultivo ============
    @staticmethod
    def get_all_gestion_cultivo():
        """Get all crop management records."""
        return CatalogoRepository.get_all_gestion_cultivo()

    @staticmethod
    def get_gestion_cultivo_raw():
        """Get crop management raw data."""
        return CatalogoRepository.get_gestion_cultivo_raw()

    @staticmethod
    def create_gestion_cultivo(id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones):
        """Create crop management record."""
        return CatalogoRepository.create_gestion_cultivo(
            id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones
        )

    @staticmethod
    def get_gestion_by_id(codigo):
        """Get crop management record by ID."""
        return CatalogoRepository.get_gestion_cultivo_by_id(codigo)

    @staticmethod
    def update_gestion_cultivo(codigo, id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones):
        """Update crop management record."""
        return CatalogoRepository.update_gestion_cultivo(
            codigo, id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones
        )

    @staticmethod
    def delete_gestion_cultivo(codigo):
        """Delete crop management record."""
        return CatalogoRepository.delete_gestion_cultivo(codigo)
