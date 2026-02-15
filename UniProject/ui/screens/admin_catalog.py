"""Catalog management screens - Admin only screens for managing reference data."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QListWidget, QLineEdit,
    QPushButton, QMessageBox, QSpinBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from services.catalogo_service import CatalogoService


class TipoHortalizaManagementScreen(QWidget):
    """Screen for managing vegetable types."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Gestionar Tipos de Hortaliza")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.list_hortalizas = QListWidget()
        layout.addWidget(self.list_hortalizas)
        
        form_layout = QFormLayout()
        
        self.input_nombre = QLineEdit()
        self.input_descripcion = QLineEdit()
        self.input_imagen = QLineEdit()
        
        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Descripción:", self.input_descripcion)
        form_layout.addRow("Imagen (ruta/URL):", self.input_imagen)
        
        layout.addLayout(form_layout)
        
        btn_crear = QPushButton("Crear/Actualizar")
        btn_crear.clicked.connect(self.crear_actualizar_hortaliza)
        layout.addWidget(btn_crear, alignment=Qt.AlignCenter)
        
        btn_eliminar = QPushButton("Eliminar Seleccionada")
        btn_eliminar.clicked.connect(self.eliminar_hortaliza)
        layout.addWidget(btn_eliminar, alignment=Qt.AlignCenter)
        
        btn_limpiar = QPushButton("Limpiar Campos")
        btn_limpiar.clicked.connect(self.limpiar_campos)
        layout.addWidget(btn_limpiar, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
        self.cargar_hortalizas()
        self.list_hortalizas.itemClicked.connect(self.cargar_en_formulario)
    
    def cargar_hortalizas(self):
        """Load vegetable types."""
        self.list_hortalizas.clear()
        rows = CatalogoService.get_tipo_hortaliza_full()
        
        for r in rows:
            self.list_hortalizas.addItem(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
    
    def crear_actualizar_hortaliza(self):
        """Create or update vegetable type."""
        nombre = self.input_nombre.text().strip()
        descripcion = self.input_descripcion.text().strip()
        imagen = self.input_imagen.text().strip()
        
        if not nombre:
            QMessageBox.critical(self, "Error", "El nombre es obligatorio.")
            return
        
        selected = self.list_hortalizas.currentItem()
        
        try:
            if selected:
                codigo = selected.text().split("|")[0].strip()
                CatalogoService.update_hortaliza(codigo, nombre, descripcion, imagen)
                QMessageBox.information(self, "Éxito", "Tipo de hortaliza actualizado.")
            else:
                CatalogoService.create_hortaliza(nombre, descripcion, imagen)
                QMessageBox.information(self, "Éxito", "Nuevo tipo de hortaliza creado.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")
        
        self.cargar_hortalizas()
        self.limpiar_campos()
    
    def eliminar_hortaliza(self):
        """Delete selected vegetable type."""
        selected = self.list_hortalizas.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione un tipo de hortaliza para eliminar.")
            return
        
        codigo = selected.text().split("|")[0].strip()
        
        if QMessageBox.question(
            self, "Confirmar",
            f"¿Desea eliminar el código {codigo}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                CatalogoService.delete_hortaliza(codigo)
                QMessageBox.information(self, "Éxito", "Hortaliza eliminada.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")
            
            self.cargar_hortalizas()
            self.limpiar_campos()
    
    def cargar_en_formulario(self, item):
        """Load item data into form."""
        line = item.text().split("|")
        nombre = line[1].strip()
        descripcion = line[2].strip()
        imagen = line[3].strip()
        
        self.input_nombre.setText(nombre)
        self.input_descripcion.setText(descripcion)
        self.input_imagen.setText(imagen)
    
    def limpiar_campos(self):
        """Clear form fields."""
        self.input_nombre.clear()
        self.input_descripcion.clear()
        self.input_imagen.clear()
        self.list_hortalizas.clearSelection()


class TipoSueloManagementScreen(QWidget):
    """Screen for managing soil types."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Gestionar Tipos de Suelo")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.list_suelos = QListWidget()
        layout.addWidget(self.list_suelos)
        
        form_layout = QFormLayout()
        
        self.input_nombre = QLineEdit()
        self.input_descripcion = QLineEdit()
        self.input_imagen = QLineEdit()
        
        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Descripción:", self.input_descripcion)
        form_layout.addRow("Imagen (ruta/URL):", self.input_imagen)
        
        layout.addLayout(form_layout)
        
        btn_crear = QPushButton("Crear/Actualizar")
        btn_crear.clicked.connect(self.crear_actualizar_suelo)
        layout.addWidget(btn_crear, alignment=Qt.AlignCenter)
        
        btn_eliminar = QPushButton("Eliminar Seleccionado")
        btn_eliminar.clicked.connect(self.eliminar_suelo)
        layout.addWidget(btn_eliminar, alignment=Qt.AlignCenter)
        
        btn_limpiar = QPushButton("Limpiar Campos")
        btn_limpiar.clicked.connect(self.limpiar_campos)
        layout.addWidget(btn_limpiar, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
        self.cargar_suelos()
        self.list_suelos.itemClicked.connect(self.cargar_en_formulario)
    
    def cargar_suelos(self):
        """Load soil types."""
        self.list_suelos.clear()
        rows = CatalogoService.get_tipo_suelo_full()
        
        for r in rows:
            self.list_suelos.addItem(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")
    
    def crear_actualizar_suelo(self):
        """Create or update soil type."""
        nombre = self.input_nombre.text().strip()
        descripcion = self.input_descripcion.text().strip()
        imagen = self.input_imagen.text().strip()
        
        if not nombre:
            QMessageBox.critical(self, "Error", "El nombre es obligatorio.")
            return
        
        selected = self.list_suelos.currentItem()
        
        try:
            if selected:
                codigo = selected.text().split("|")[0].strip()
                CatalogoService.update_suelo(codigo, nombre, descripcion, imagen)
                QMessageBox.information(self, "Éxito", "Tipo de suelo actualizado.")
            else:
                CatalogoService.create_suelo(nombre, descripcion, imagen)
                QMessageBox.information(self, "Éxito", "Nuevo tipo de suelo creado.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")
        
        self.cargar_suelos()
        self.limpiar_campos()
    
    def eliminar_suelo(self):
        """Delete selected soil type."""
        selected = self.list_suelos.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione un tipo de suelo para eliminar.")
            return
        
        codigo = selected.text().split("|")[0].strip()
        
        if QMessageBox.question(
            self, "Confirmar",
            f"¿Desea eliminar el código {codigo}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                CatalogoService.delete_suelo(codigo)
                QMessageBox.information(self, "Éxito", "Tipo de suelo eliminado.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")
            
            self.cargar_suelos()
            self.limpiar_campos()
    
    def cargar_en_formulario(self, item):
        """Load item data into form."""
        line = item.text().split("|")
        nombre = line[1].strip()
        descripcion = line[2].strip()
        imagen = line[3].strip()
        
        self.input_nombre.setText(nombre)
        self.input_descripcion.setText(descripcion)
        self.input_imagen.setText(imagen)
    
    def limpiar_campos(self):
        """Clear form fields."""
        self.input_nombre.clear()
        self.input_descripcion.clear()
        self.input_imagen.clear()
        self.list_suelos.clearSelection()


class ClimaManagementScreen(QWidget):
    """Screen for managing climate types."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Gestionar Clima")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.list_climas = QListWidget()
        layout.addWidget(self.list_climas)
        
        form_layout = QFormLayout()
        
        self.input_nombre = QLineEdit()
        self.input_grados = QLineEdit()
        self.input_descripcion = QLineEdit()
        self.input_imagen = QLineEdit()
        
        form_layout.addRow("Nombre:", self.input_nombre)
        form_layout.addRow("Grados Temperatura:", self.input_grados)
        form_layout.addRow("Descripción:", self.input_descripcion)
        form_layout.addRow("Imagen (ruta/URL):", self.input_imagen)
        
        layout.addLayout(form_layout)
        
        btn_crear = QPushButton("Crear/Actualizar")
        btn_crear.clicked.connect(self.crear_actualizar_clima)
        layout.addWidget(btn_crear, alignment=Qt.AlignCenter)
        
        btn_eliminar = QPushButton("Eliminar Seleccionado")
        btn_eliminar.clicked.connect(self.eliminar_clima)
        layout.addWidget(btn_eliminar, alignment=Qt.AlignCenter)
        
        btn_limpiar = QPushButton("Limpiar Campos")
        btn_limpiar.clicked.connect(self.limpiar_campos)
        layout.addWidget(btn_limpiar, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
        self.cargar_climas()
        self.list_climas.itemClicked.connect(self.cargar_en_formulario)
    
    def cargar_climas(self):
        """Load climate types."""
        self.list_climas.clear()
        rows = CatalogoService.get_clima_full()
        
        for r in rows:
            self.list_climas.addItem(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
    
    def crear_actualizar_clima(self):
        """Create or update climate type."""
        nombre = self.input_nombre.text().strip()
        grados_str = self.input_grados.text().strip()
        descripcion = self.input_descripcion.text().strip()
        imagen = self.input_imagen.text().strip()
        
        if not nombre:
            QMessageBox.critical(self, "Error", "El nombre es obligatorio.")
            return
        
        try:
            grados = float(grados_str) if grados_str else 0.0
        except ValueError:
            QMessageBox.critical(self, "Error", "Ingrese un valor numérico en grados de temperatura.")
            return
        
        selected = self.list_climas.currentItem()
        
        try:
            if selected:
                codigo = selected.text().split("|")[0].strip()
                CatalogoService.update_clima(codigo, nombre, grados, descripcion, imagen)
                QMessageBox.information(self, "Éxito", "Clima actualizado.")
            else:
                CatalogoService.create_clima(nombre, grados, descripcion, imagen)
                QMessageBox.information(self, "Éxito", "Nuevo clima creado.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")
        
        self.cargar_climas()
        self.limpiar_campos()
    
    def eliminar_clima(self):
        """Delete selected climate type."""
        selected = self.list_climas.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione un clima para eliminar.")
            return
        
        codigo = selected.text().split("|")[0].strip()
        
        if QMessageBox.question(
            self, "Confirmar",
            f"¿Desea eliminar el código {codigo}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                CatalogoService.delete_clima(codigo)
                QMessageBox.information(self, "Éxito", "Clima eliminado.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")
            
            self.cargar_climas()
            self.limpiar_campos()
    
    def cargar_en_formulario(self, item):
        """Load item data into form."""
        line = item.text().split("|")
        nombre = line[1].strip()
        grados = line[2].strip()
        descripcion = line[3].strip()
        imagen = line[4].strip()
        
        self.input_nombre.setText(nombre)
        self.input_grados.setText(grados)
        self.input_descripcion.setText(descripcion)
        self.input_imagen.setText(imagen)
    
    def limpiar_campos(self):
        """Clear form fields."""
        self.input_nombre.clear()
        self.input_grados.clear()
        self.input_descripcion.clear()
        self.input_imagen.clear()
        self.list_climas.clearSelection()


# Import missing components
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTextEdit
