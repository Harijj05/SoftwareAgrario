"""Catalog repository - Database operations for reference data."""

from ..database import get_connection


class CatalogoRepository:
    """Repository for catalog/reference data operations."""

    # ========================
    # Tipo Hortaliza
    # ========================

    @staticmethod
    def get_all_tipo_hortaliza():
        """Get all hortaliza types."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre FROM tipo_hortaliza")
        datos = cursor.fetchall()
        conn.close()
        return datos

    @staticmethod
    def get_tipo_hortaliza_full():
        """Get all hortaliza types with full details."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre, descripcion, imagen FROM tipo_hortaliza")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_tipo_hortaliza(nombre):
        """Search hortaliza type by name."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT codigo, nombre, descripcion, imagen FROM tipo_hortaliza WHERE nombre LIKE ?",
            ('%' + nombre + '%',)
        )
        registros = cursor.fetchall()
        conn.close()
        return registros

    @staticmethod
    def create_tipo_hortaliza(nombre, descripcion, imagen):
        """Create new hortaliza type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tipo_hortaliza (nombre, descripcion, imagen) VALUES (?, ?, ?)",
            (nombre, descripcion, imagen)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update_tipo_hortaliza(codigo, nombre, descripcion, imagen):
        """Update hortaliza type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE tipo_hortaliza
               SET nombre = ?, descripcion = ?, imagen = ?
               WHERE codigo = ?""",
            (nombre, descripcion, imagen, codigo)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_tipo_hortaliza(codigo):
        """Delete hortaliza type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tipo_hortaliza WHERE codigo = ?", (codigo,))
        conn.commit()
        conn.close()

    # ========================
    # Tipo Suelo
    # ========================

    @staticmethod
    def get_all_tipo_suelo():
        """Get all soil types."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre FROM tipo_suelo")
        datos = cursor.fetchall()
        conn.close()
        return datos

    @staticmethod
    def get_tipo_suelo_full():
        """Get all soil types with full details."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre, descripcion, imagen FROM tipo_suelo")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def create_tipo_suelo(nombre, descripcion, imagen):
        """Create new soil type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tipo_suelo (nombre, descripcion, imagen) VALUES (?, ?, ?)",
            (nombre, descripcion, imagen)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update_tipo_suelo(codigo, nombre, descripcion, imagen):
        """Update soil type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE tipo_suelo
               SET nombre = ?, descripcion = ?, imagen = ?
               WHERE codigo = ?""",
            (nombre, descripcion, imagen, codigo)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_tipo_suelo(codigo):
        """Delete soil type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tipo_suelo WHERE codigo = ?", (codigo,))
        conn.commit()
        conn.close()

    # ========================
    # Clima
    # ========================

    @staticmethod
    def get_all_clima():
        """Get all climate types."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre FROM clima")
        datos = cursor.fetchall()
        conn.close()
        return datos

    @staticmethod
    def get_clima_full():
        """Get all climate types with full details."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre, grados_temperatura, descripcion, imagen FROM clima")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def create_clima(nombre, grados, descripcion, imagen):
        """Create new climate type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clima (nombre, grados_temperatura, descripcion, imagen) VALUES (?, ?, ?, ?)",
            (nombre, grados, descripcion, imagen)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update_clima(codigo, nombre, grados, descripcion, imagen):
        """Update climate type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE clima
               SET nombre = ?, grados_temperatura = ?, descripcion = ?, imagen = ?
               WHERE codigo = ?""",
            (nombre, grados, descripcion, imagen, codigo)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_clima(codigo):
        """Delete climate type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clima WHERE codigo = ?", (codigo,))
        conn.commit()
        conn.close()

    # ========================
    # Tipo Cultivo
    # ========================

    @staticmethod
    def get_all_tipo_cultivo():
        """Get all crop types."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM tipo_cultivo")
        rows = cursor.fetchall()
        conn.close()
        return rows if rows else [
            (1, "limones"),
            (2, "maíz"),
            (3, "trigo"),
            (4, "tomate")
        ]

    @staticmethod
    def get_tipo_cultivo_full():
        """Get all crop types with full details."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, meses_primera, meses_rutinaria FROM tipo_cultivo")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def create_tipo_cultivo(nombre, meses_primera, meses_rutinaria):
        """Create new crop type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tipo_cultivo (nombre, meses_primera, meses_rutinaria) VALUES (?, ?, ?)",
            (nombre, meses_primera, meses_rutinaria)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def update_tipo_cultivo(cultivo_id, nombre, meses_primera, meses_rutinaria):
        """Update crop type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE tipo_cultivo
               SET nombre = ?, meses_primera = ?, meses_rutinaria = ?
               WHERE id = ?""",
            (nombre, meses_primera, meses_rutinaria, cultivo_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_tipo_cultivo(cultivo_id):
        """Delete crop type."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tipo_cultivo WHERE id = ?", (cultivo_id,))
        conn.commit()
        conn.close()

    # ========================
    # Gestion Cultivo
    # ========================

    @staticmethod
    def get_all_gestion_cultivo():
        """Get all crop management records."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT gc.codigo, u.username, th.nombre, ts.nombre, c.nombre, gc.video, gc.observaciones
            FROM gestion_cultivo gc
            JOIN usuarios u ON gc.id_persona = u.id
            JOIN tipo_hortaliza th ON gc.id_tipo_hortaliza = th.codigo
            JOIN tipo_suelo ts ON gc.id_tipo_suelo = ts.codigo
            JOIN clima c ON gc.id_clima = c.codigo
        """)
        registros = cursor.fetchall()
        conn.close()
        return registros

    @staticmethod
    def get_gestion_cultivo_raw():
        """Get crop management records with IDs."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT codigo, id_persona, id_tipo_hortaliza, id_tipo_suelo, id_clima, video, observaciones FROM gestion_cultivo"
        )
        gestiones = cursor.fetchall()
        conn.close()
        return gestiones

    @staticmethod
    def create_gestion_cultivo(id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones):
        """Create new crop management record."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO gestion_cultivo
               (id_persona, id_tipo_hortaliza, id_tipo_suelo, id_clima, video, observaciones)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_gestion_cultivo_by_id(codigo):
        """Get specific crop management record."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """SELECT id_persona, id_tipo_hortaliza, id_tipo_suelo, id_clima, video, observaciones
               FROM gestion_cultivo WHERE codigo = ?""",
            (codigo,)
        )
        data = cursor.fetchone()
        conn.close()
        return data

    @staticmethod
    def update_gestion_cultivo(codigo, id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones):
        """Update crop management record."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE gestion_cultivo
               SET id_persona = ?, id_tipo_hortaliza = ?, id_tipo_suelo = ?,
                   id_clima = ?, video = ?, observaciones = ?
               WHERE codigo = ?""",
            (id_persona, id_hortaliza, id_suelo, id_clima, video, observaciones, codigo)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete_gestion_cultivo(codigo):
        """Delete crop management record."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM gestion_cultivo WHERE codigo = ?", (codigo,))
        conn.commit()
        conn.close()
