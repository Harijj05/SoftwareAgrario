"""Hectarea repository - Database operations for hectareas."""

from ..database import get_connection


class HectareaRepository:
    """Repository for hectarea (hectare) operations."""

    @staticmethod
    def create(hectarea):
        """Save a hectarea to database."""
        conn = get_connection()
        cursor = conn.cursor()
        data = hectarea.to_dict()
        cursor.execute("""
            INSERT INTO hectareas 
            (numero, tipo_de_cultivo, siembra, primera_cosecha, 
             cosecha_rutinaria, tipo_suelo, temperatura)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data['numero'],
            data['tipo_de_cultivo'],
            data['siembra'],
            data['primera_cosecha'],
            data['cosecha_rutinaria'],
            data['tipo_suelo'],
            data['temperatura']
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        """Get all hectareas."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hectareas")
        hectareas = cursor.fetchall()
        conn.close()
        return hectareas

    @staticmethod
    def get_by_numero(numero):
        """Get hectarea by number."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM hectareas WHERE numero = ?", (numero,))
        hectarea = cursor.fetchone()
        conn.close()
        return hectarea

    @staticmethod
    def delete(numero):
        """Delete a hectarea."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM hectareas WHERE numero = ?", (numero,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(numero, tipo, siembra, primera, rutinaria, tipo_suelo, temperatura):
        """Update hectarea data."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE hectareas
            SET tipo_de_cultivo = ?, siembra = ?, primera_cosecha = ?,
                cosecha_rutinaria = ?, tipo_suelo = ?, temperatura = ?
            WHERE numero = ?
        """, (tipo.lower(), siembra, primera, rutinaria, tipo_suelo, temperatura, numero))
        conn.commit()
        conn.close()

    @staticmethod
    def get_next_numero():
        """Get next available hectarea number."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(numero) FROM hectareas")
        max_num = cursor.fetchone()[0]
        conn.close()
        return 1 if max_num is None else max_num + 1
