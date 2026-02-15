"""Hectarea screens - UI for hectare management."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLabel, QPushButton, QLineEdit,
    QComboBox, QMessageBox, QListWidget, QInputDialog
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from core.models import Hectarea
from services.hectarea_service import HectareaService
from services.catalogo_service import CatalogoService


class RegistrarScreen(QWidget):
    """Screen for registering new hectareas."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Registrar Hectárea")
        title.setFont(QFont("Helvetica", 14, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        form_layout = QFormLayout()
        
        self.combo_crop = QComboBox()
        form_layout.addRow("Tipo de Cultivo:", self.combo_crop)
        
        self.entry_siembra = QLineEdit()
        form_layout.addRow("Fecha de Siembra (YYYY-MM-DD):", self.entry_siembra)
        
        self.combo_suelo = QComboBox()
        form_layout.addRow("Tipo de Suelo:", self.combo_suelo)
        
        self.entry_temp = QLineEdit()
        form_layout.addRow("Temperatura (°C):", self.entry_temp)
        
        layout.addLayout(form_layout)
        
        btn_registrar = QPushButton("Registrar")
        btn_registrar.clicked.connect(self.registrar_hectarea)
        layout.addWidget(btn_registrar, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def showEvent(self, event):
        """Load options when screen is shown."""
        super().showEvent(event)
        self.cargar_opciones()
    
    def cargar_opciones(self):
        """Load crop and soil type options."""
        self.combo_crop.clear()
        crop_types = CatalogoService.get_all_tipo_cultivo()
        crop_names = [r[1] for r in crop_types] if crop_types else ["limones", "maíz", "trigo", "tomate"]
        self.combo_crop.addItems(crop_names)
        
        self.combo_suelo.clear()
        suelos = CatalogoService.get_all_tipo_suelo()
        suelo_names = [s[1] for s in suelos] if suelos else ["Sin suelo registrado"]
        self.combo_suelo.addItems(suelo_names)
    
    def registrar_hectarea(self):
        """Handle hectarea registration."""
        siembra = self.entry_siembra.text().strip()
        crop = self.combo_crop.currentText()
        
        if not siembra:
            QMessageBox.critical(self, "Error", "Ingrese la fecha de siembra.")
            return
        
        suelo = self.combo_suelo.currentText()
        temperatura = self.entry_temp.text().strip()
        
        numero = HectareaService.get_next_numero()
        
        result = HectareaService.create_hectarea(
            numero, crop, siembra, suelo, temperatura
        )
        
        if result["success"]:
            QMessageBox.information(self, "Registro", "Hectárea registrada con éxito.")
            self.controller.show_screen("main")
        else:
            QMessageBox.critical(self, "Error", result["error"])


class BuscarScreen(QWidget):
    """Screen for searching hectareas."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Buscar Hectárea")
        title.setFont(QFont("Helvetica", 14, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.entry_numero = QLineEdit()
        self.entry_numero.setPlaceholderText("Número de Hectárea")
        layout.addWidget(self.entry_numero)
        
        btn_buscar = QPushButton("Buscar")
        btn_buscar.clicked.connect(self.buscar_hectarea)
        layout.addWidget(btn_buscar, alignment=Qt.AlignCenter)
        
        self.result_area = QLineEdit()
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def buscar_hectarea(self):
        """Handle hectarea search."""
        num_text = self.entry_numero.text().strip()
        
        if not num_text.isdigit():
            self.result_area.setText("Ingrese un número válido.")
            return
        
        hectarea = HectareaService.get_hectarea(int(num_text))
        
        self.result_area.clear()
        if hectarea:
            texto = (f"Hectárea {hectarea[1]}:\n  Tipo: {hectarea[2]}\n  Siembra: {hectarea[3]}\n"
                    f"  1ra Cosecha: {hectarea[4]}\n  Cosecha Rutinaria: {hectarea[5]}\n"
                    f"  Tipo de Suelo: {hectarea[6]}\n  Temperatura: {hectarea[7]}")
            self.result_area.setText(texto)
        else:
            self.result_area.setText(f"No se encontró la Hectárea {num_text}.")
