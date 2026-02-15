"""Authentication service - User login and validation."""

from data.repositories.usuario_repo import UsuarioRepository


class AuthService:
    """Service for authentication operations."""

    @staticmethod
    def validate_credentials(username, password):
        """Validate user credentials."""
        result = UsuarioRepository.get_by_username(username)
        if result and password == result[0]:
            return {
                "valid": True,
                "role": result[1],
                "email": result[2]
            }
        return {"valid": False, "role": None, "email": None}

    @staticmethod
    def get_all_users():
        """Get all registered users."""
        return UsuarioRepository.get_all()

    @staticmethod
    def recover_password_by_email(email):
        """Recover password using email."""
        result = UsuarioRepository.get_by_email(email)
        if result:
            return {"found": True, "username": result[0], "password": result[1]}
        return {"found": False}

    @staticmethod
    def create_user(username, password, email):
        """Create new user."""
        try:
            UsuarioRepository.create(username, password, email)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def delete_user(username):
        """Delete user."""
        if username == "admin":
            return {"success": False, "error": "Cannot delete admin user"}
        try:
            UsuarioRepository.delete(username)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def update_user(username, new_username, password, email):
        """Update user data."""
        if username == "admin":
            return {"success": False, "error": "Cannot modify admin user"}
        try:
            UsuarioRepository.update(username, new_username, password, email)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @staticmethod
    def get_all_users_details():
        """Get all users with details."""
        return UsuarioRepository.get_all_users()
