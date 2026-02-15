"""Login screen - User authentication."""

import sqlite3
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget,
    QLineEdit, QInputDialog, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from services.auth_service import AuthService


class LoginScreen(QWidget):
    """Login screen for system access."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Acceso al Sistema de Cultivos")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        subtitle = QLabel("Seleccione un usuario:")
        subtitle.setFont(QFont("Helvetica", 14))
        layout.addWidget(subtitle, alignment=Qt.AlignCenter)
        
        self.users_list = QListWidget()
        layout.addWidget(self.users_list)
        self.refresh_users()
        
        btn_recuperar = QPushButton("Recuperar Contraseña")
        btn_recuperar.clicked.connect(self.recuperar_contrasena)
        layout.addWidget(btn_recuperar, alignment=Qt.AlignCenter)
        
        self.users_list.itemDoubleClicked.connect(self.do_login)
        self.setLayout(layout)
    
    def refresh_users(self):
        """Refresh user list."""
        self.users_list.clear()
        users = AuthService.get_all_users()
        for u in users:
            self.users_list.addItem(u[1])
    
    def do_login(self, item):
        """Handle login."""
        username = item.text()
        password, ok = QInputDialog.getText(
            self, "Contraseña",
            f"Ingrese la contraseña para {username}:",
            QLineEdit.Password
        )
        if not ok:
            return
        
        result = AuthService.validate_credentials(username, password)
        
        if result["valid"]:
            self.controller.current_user = username
            self.controller.user_role = result["role"]
            self.controller.current_email = result["email"]
            self.controller.show_screen("main")
        else:
            QMessageBox.critical(self, "Error", "Contraseña incorrecta.")
    
    def recuperar_contrasena(self):
        """Handle password recovery."""
        email, ok = QInputDialog.getText(
            self, "Recuperar Contraseña",
            "Ingrese su correo electrónico:"
        )
        if not ok or not email:
            return
        
        result = AuthService.recover_password_by_email(email)
        
        if result["found"]:
            QMessageBox.information(
                self, "Recuperación",
                f"Usuario: {result['username']}\nContraseña: {result['password']}\n"
                "(Se simula envío de correo)"
            )
        else:
            QMessageBox.critical(self, "Error", "No se encontró un usuario con ese correo.")
