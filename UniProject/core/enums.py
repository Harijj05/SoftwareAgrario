"""Enumerations and constants for the application."""

from enum import Enum


class UserRole(str, Enum):
    """User roles in the system."""
    ADMIN = "admin"
    USUARIO = "usuario"


class CropType(str, Enum):
    """Crop types with their harvest timelines."""
    LIMONES = "limones"
    MAIZ = "maíz"
    TRIGO = "trigo"
    TOMATE = "tomate"


class SoilType(str, Enum):
    """Soil types."""
    ARENOSO = "Arenoso"
    LIMOSO = "Limoso"
    FRANCO = "Franco"
    ARCILLOSO = "Arcilloso"


class ClimateType(str, Enum):
    """Climate types."""
    TROPICAL = "Tropical"
    SECO = "Seco"
    TEMPLADO = "Templado"
    CONTINENTAL = "Continental"
    POLAR = "Polar"


class VegetableType(str, Enum):
    """Vegetable/Hortaliza types."""
    BULBOS = "Bulbos"
    TALLOS = "Tallos comestibles"
    RAICES = "Raíces comestibles"
    FRUTOS = "Frutos"
    HOJAS = "Hojas"
    FLORES = "Flores"
    TUBERCULOS = "Tubérculos"


# Harvest cycle defaults (in days)
HARVEST_CYCLES = {
    CropType.LIMONES.value: {"first": 1825, "routine": 180},  # 5 years + 180 days
    CropType.MAIZ.value: {"first": 90, "routine": 30},
    CropType.TRIGO.value: {"first": 120, "routine": 30},
    CropType.TOMATE.value: {"first": 70, "routine": 15},
}

# Default seasonal values
DEFAULT_HARVEST_DAYS = 80
DEFAULT_ROUTINE_HARVEST_DAYS = 20

# Default temperatures by climate
DEFAULT_TEMPS = {
    ClimateType.TROPICAL.value: 30,
    ClimateType.SECO.value: 25,
    ClimateType.TEMPLADO.value: 20,
    ClimateType.CONTINENTAL.value: 15,
    ClimateType.POLAR.value: 0,
}
