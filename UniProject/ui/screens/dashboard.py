"""Profile and reporting screens."""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from services.catalogo_service import CatalogoService


class PerfilScreen(QWidget):
    """User profile screen."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        layout = QVBoxLayout(self)
        
        title = QLabel("Perfil de Usuario")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.info_label = QLabel("")
        self.info_label.setFont(QFont("Helvetica", 14))
        layout.addWidget(self.info_label, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def cargar_perfil(self):
        """Load and display user profile."""
        user = self.controller.current_user
        email = self.controller.current_email
        role = self.controller.user_role
        self.info_label.setText(f"Usuario: {user}\nEmail: {email}\nRol: {role}")


class InformeScreen(QWidget):
    """Crop management report screen."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        layout = QVBoxLayout(self)
        
        title = QLabel("Informe de Gestión Cultivo")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.informe_area = QTextEdit()
        self.informe_area.setReadOnly(True)
        layout.addWidget(self.informe_area)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def cargar_informe(self):
        """Load and display crop management report."""
        self.informe_area.clear()
        registros = CatalogoService.get_all_gestion_cultivo()
        
        if registros:
            texto = ""
            for r in registros:
                texto += (f"Código: {r[0]}\nUsuario: {r[1]}\nTipo Hortaliza: {r[2]}\n"
                         f"Tipo Suelo: {r[3]}\nClima: {r[4]}\nVideo: {r[5]}\n"
                         f"Observaciones: {r[6]}\n" + "-" * 40 + "\n")
            self.informe_area.setPlainText(texto)
        else:
            self.informe_area.setPlainText("No hay registros de gestión cultivo.")


class ConsultaScreen(QWidget):
    """Crop/vegetable type search screen."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        layout = QVBoxLayout(self)
        
        title = QLabel("Consulta Tipo de Cultivo (Hortaliza)")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        from PyQt5.QtWidgets import QLineEdit, QMessageBox
        
        self.entry_consulta = QLineEdit()
        self.entry_consulta.setPlaceholderText("Ingrese el nombre del tipo de hortaliza")
        layout.addWidget(self.entry_consulta)
        
        btn_buscar = QPushButton("Buscar")
        btn_buscar.clicked.connect(self.buscar_tipo)
        layout.addWidget(btn_buscar, alignment=Qt.AlignCenter)
        
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def buscar_tipo(self):
        """Search for vegetable type."""
        from PyQt5.QtWidgets import QMessageBox
        
        nombre = self.entry_consulta.text().strip()
        if not nombre:
            QMessageBox.critical(self, "Error", "Ingrese un nombre para consultar.")
            return
        
        registros = CatalogoService.search_hortaliza(nombre)
        
        self.result_area.clear()
        if registros:
            texto = ""
            for r in registros:
                texto += (f"Código: {r[0]}\nNombre: {r[1]}\nDescripción: {r[2]}\n"
                         f"Imagen: {r[3]}\n" + "-" * 30 + "\n")
            self.result_area.setPlainText(texto)
        else:
            self.result_area.setPlainText("No se encontró el tipo de cultivo.")
