"""Main screen - Primary application interface."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from services.hectarea_service import HectareaService


class MainScreen(QWidget):
    """Main application screen with navigation menu."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        main_layout = QVBoxLayout(self)
        
        # Header
        self.header_label = QLabel("")
        self.header_label.setFont(QFont("Helvetica", 16, QFont.Bold))
        main_layout.addWidget(self.header_label, alignment=Qt.AlignLeft)
        
        self.email_label = QLabel("")
        main_layout.addWidget(self.email_label, alignment=Qt.AlignLeft)
        
        # Menu buttons
        menu_layout = QHBoxLayout()
        
        buttons_config = [
            ("Registrar Hectárea", "registrar"),
            ("Mostrar Hectáreas", self.show_hectareas),
            ("Buscar Hectárea", "buscar"),
            ("Perfil", "perfil"),
            ("Informe Cultivo", "informe"),
            ("Consulta Cultivo", "consulta"),
            ("Gestionar Hectáreas", "gestionar_hectareas"),
            ("Gestión Cultivo", "gestion_cultivo"),
            ("Gestionar Usuarios", "usuarios"),
            ("Logout", "login"),
        ]
        
        for btn_text, action in buttons_config:
            btn = QPushButton(btn_text)
            if callable(action):
                btn.clicked.connect(action)
            else:
                btn.clicked.connect(lambda checked, a=action: self.controller.show_screen(a))
            menu_layout.addWidget(btn)
        
        main_layout.addLayout(menu_layout)
        
        # Content area
        self.content_area = QTextEdit()
        self.content_area.setReadOnly(True)
        main_layout.addWidget(self.content_area)
        
        self.setLayout(main_layout)
    
    def update_header(self):
        """Update header with user information."""
        if self.controller.user_role == "usuario":
            self.header_label.setText(f"Bienvenido {self.controller.current_user}")
            self.email_label.setText(f"({self.controller.current_email})")
        else:
            self.header_label.setText(
                f"Bienvenido {self.controller.current_user} ({self.controller.user_role})"
            )
            self.email_label.setText("")
    
    def show_hectareas(self):
        """Display all hectareas."""
        self.content_area.clear()
        hectareas = HectareaService.get_all_hectareas()
        
        if hectareas:
            texto = ""
            for h in hectareas:
                texto += (f"Hectárea {h[1]}:\n  Tipo: {h[2]}\n  Siembra: {h[3]}\n"
                         f"  1ra Cosecha: {h[4]}\n  Cosecha Rutinaria: {h[5]}\n"
                         f"  Tipo de Suelo: {h[6]}\n  Temperatura: {h[7]}\n\n")
            self.content_area.setPlainText(texto)
        else:
            self.content_area.setPlainText("No hay hectáreas registradas.")
