"""User repository - Database operations for users."""

from ..database import get_connection


class UsuarioRepository:
    """Repository for user operations."""

    @staticmethod
    def get_all():
        """Get all users."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username FROM usuarios")
        personas = cursor.fetchall()
        conn.close()
        return personas

    @staticmethod
    def get_by_username(username):
        """Get user by username."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password, role, email FROM usuarios WHERE username = ?",
            (username,)
        )
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def get_by_email(email):
        """Get user by email."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT username, password FROM usuarios WHERE email = ?",
            (email,)
        )
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def create(username, password, email, role="usuario"):
        """Create a new user."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (username, password, role, email) VALUES (?, ?, ?, ?)",
            (username, password, role, email)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(username):
        """Delete a user."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
        conn.commit()
        conn.close()

    @staticmethod
    def update(username, new_username, password, email):
        """Update user data."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE usuarios
               SET username = ?, password = ?, email = ?
               WHERE username = ?""",
            (new_username, password, email, username)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_users():
        """Get all users with details."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT username, email FROM usuarios")
        users = cursor.fetchall()
        conn.close()
        return users
