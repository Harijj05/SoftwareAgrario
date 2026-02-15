"""Domain models for agricultural management system."""

from datetime import datetime, timedelta
from .enums import HARVEST_CYCLES, DEFAULT_HARVEST_DAYS, DEFAULT_ROUTINE_HARVEST_DAYS


class Hectarea:
    """Model for a hectare of cultivation."""
    
    def __init__(self, numero, tipo_de_cultivo, siembra, primera_cosecha=None, 
                 cosecha_rutinaria=None, tipo_suelo=None, temperatura=None):
        self.numero = numero
        self.tipo_de_cultivo = tipo_de_cultivo.lower()
        self.siembra = datetime.strptime(siembra, "%Y-%m-%d")
        self._set_harvest_dates(primera_cosecha, cosecha_rutinaria)
        self.tipo_suelo = tipo_suelo
        try:
            self.temperatura = float(temperatura) if temperatura not in (None, "") else None
        except ValueError:
            self.temperatura = None

    def _set_harvest_dates(self, primera_cosecha, cosecha_rutinaria):
        """Set harvest dates based on crop type and provided dates."""
        if self.tipo_de_cultivo == "limones":
            self.primeracosecha = self.siembra.replace(year=self.siembra.year + 5)
            self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=180)).strftime("%Y-%m-%d")
        else:
            self._set_first_harvest(primera_cosecha)
            self._set_routine_harvest(cosecha_rutinaria)

    def _set_first_harvest(self, primera_cosecha):
        """Calculate or set first harvest date."""
        if not primera_cosecha:
            if self.tipo_de_cultivo in HARVEST_CYCLES:
                days = HARVEST_CYCLES[self.tipo_de_cultivo]["first"]
            else:
                days = DEFAULT_HARVEST_DAYS
            self.primeracosecha = self.siembra + timedelta(days=days)
        else:
            self.primeracosecha = datetime.strptime(primera_cosecha, "%Y-%m-%d")

    def _set_routine_harvest(self, cosecha_rutinaria):
        """Calculate or set routine harvest date."""
        if not cosecha_rutinaria:
            if self.tipo_de_cultivo in HARVEST_CYCLES:
                days = HARVEST_CYCLES[self.tipo_de_cultivo]["routine"]
            else:
                days = DEFAULT_ROUTINE_HARVEST_DAYS
            self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=days)).strftime("%Y-%m-%d")
        else:
            self.cosecha_rutinaria = cosecha_rutinaria

    def to_dict(self):
        """Convert hectarea to dictionary representation."""
        return {
            "numero": self.numero,
            "tipo_de_cultivo": self.tipo_de_cultivo,
            "siembra": self.siembra.strftime("%Y-%m-%d"),
            "primera_cosecha": self.primeracosecha.strftime("%Y-%m-%d"),
            "cosecha_rutinaria": self.cosecha_rutinaria,
            "tipo_suelo": self.tipo_suelo,
            "temperatura": self.temperatura,
        }
