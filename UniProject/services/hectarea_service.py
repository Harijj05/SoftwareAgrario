"""Hectarea service - Business logic for hectare management."""

from core.models import Hectarea
from data.repositories.hectarea_repo import HectareaRepository


class HectareaService:
    """Service for hectare operations."""

    @staticmethod
    def create_hectarea(numero, crop_type, siembra, tipo_suelo, temperatura,
                       primera_cosecha=None, cosecha_rutinaria=None):
        """Create and save a new hectarea."""
        try:
            hectarea = Hectarea(
                numero, crop_type, siembra,
                primera_cosecha, cosecha_rutinaria,
                tipo_suelo, temperatura
            )
            HectareaRepository.create(hectarea)
            return {"success": True, "hectarea": hectarea}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def get_all_hectareas():
        """Get all hectareas."""
        return HectareaRepository.get_all()

    @staticmethod
    def get_hectarea(numero):
        """Get hectarea by number."""
        return HectareaRepository.get_by_numero(numero)

    @staticmethod
    def delete_hectarea(numero):
        """Delete hectarea."""
        try:
            HectareaRepository.delete(numero)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def update_hectarea(numero, tipo, siembra, primera, rutinaria, tipo_suelo, temperatura):
        """Update hectarea data."""
        try:
            HectareaRepository.update(numero, tipo, siembra, primera, rutinaria, tipo_suelo, temperatura)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def get_next_numero():
        """Get next available hectarea number."""
        return HectareaRepository.get_next_numero()
