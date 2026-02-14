from datetime import datetime, timedelta
import sqlite3


class Hectarea:
    """Modelo de datos para una hectárea de cultivo."""
    
    def __init__(self, numero, tipo_de_cultivo, siembra, primera_cosecha=None, cosecha_rutinaria=None, tipo_suelo=None, temperatura=None):
        self.numero = numero
        self.tipo_de_cultivo = tipo_de_cultivo.lower()
        self.siembra = datetime.strptime(siembra, "%Y-%m-%d")
        if self.tipo_de_cultivo == "limones":
            self.primeracosecha = self.siembra.replace(year=self.siembra.year + 5)
            self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=180)).strftime("%Y-%m-%d")
        else:
            if not primera_cosecha:
                if self.tipo_de_cultivo == "maíz":
                    self.primeracosecha = self.siembra + timedelta(days=90)
                elif self.tipo_de_cultivo == "trigo":
                    self.primeracosecha = self.siembra + timedelta(days=120)
                elif self.tipo_de_cultivo == "tomate":
                    self.primeracosecha = self.siembra + timedelta(days=70)
                else:
                    self.primeracosecha = self.siembra + timedelta(days=80)
            else:
                self.primeracosecha = datetime.strptime(primera_cosecha, "%Y-%m-%d")
            if not cosecha_rutinaria:
                if self.tipo_de_cultivo == "maíz":
                    self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=30)).strftime("%Y-%m-%d")
                elif self.tipo_de_cultivo == "trigo":
                    self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=30)).strftime("%Y-%m-%d")
                elif self.tipo_de_cultivo == "tomate":
                    self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=15)).strftime("%Y-%m-%d")
                else:
                    self.cosecha_rutinaria = (self.primeracosecha + timedelta(days=20)).strftime("%Y-%m-%d")
            else:
                self.cosecha_rutinaria = cosecha_rutinaria
        self.tipo_suelo = tipo_suelo
        try:
            self.temperatura = float(temperatura) if temperatura not in (None, "") else None
        except ValueError:
            self.temperatura = None

    def guardar_en_bd(self):
        conn = sqlite3.connect("cultivos.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO hectareas (numero, tipo_de_cultivo, siembra, primera_cosecha, cosecha_rutinaria, tipo_suelo, temperatura) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (self.numero, self.tipo_de_cultivo, self.siembra.strftime("%Y-%m-%d"),
              self.primeracosecha.strftime("%Y-%m-%d"), self.cosecha_rutinaria, self.tipo_suelo, self.temperatura))
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(numero):
        conn = sqlite3.connect("cultivos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM hectareas WHERE numero = ?", (numero,))
        conn.commit()
        conn.close()

    @staticmethod
    def actualizar(numero, tipo, siembra, primera, rutinaria, tipo_suelo, temperatura):
        conn = sqlite3.connect("cultivos.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE hectareas 
            SET tipo_de_cultivo = ?, siembra = ?, primera_cosecha = ?, cosecha_rutinaria = ?, tipo_suelo = ?, temperatura = ?
            WHERE numero = ?
        """, (tipo.lower(), siembra, primera, rutinaria, tipo_suelo, temperatura, numero))
        conn.commit()
        conn.close()
