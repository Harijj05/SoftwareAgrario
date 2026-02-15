"""User management and admin crop management screens."""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QListWidget, QLineEdit,
    QPushButton, QMessageBox, QDialog, QDialogButtonBox,
    QComboBox, QInputDialog, QSpinBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from services.auth_service import AuthService
from services.catalogo_service import CatalogoService


class UserManagementScreen(QWidget):
    """Screen for managing users (admin only)."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Gestión de Usuarios")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.user_list = QListWidget()
        layout.addWidget(self.user_list)
        self.refresh_user_list()
        
        form_layout = QFormLayout()
        
        self.new_username = QLineEdit()
        form_layout.addRow("Username:", self.new_username)
        
        self.new_password = QLineEdit()
        self.new_password.setEchoMode(QLineEdit.Password)
        form_layout.addRow("Password:", self.new_password)
        
        self.new_email = QLineEdit()
        form_layout.addRow("Email:", self.new_email)
        
        layout.addLayout(form_layout)
        
        btn_crear = QPushButton("Crear Usuario")
        btn_crear.clicked.connect(self.create_user)
        layout.addWidget(btn_crear, alignment=Qt.AlignCenter)
        
        btn_eliminar = QPushButton("Eliminar Usuario")
        btn_eliminar.clicked.connect(self.delete_user)
        layout.addWidget(btn_eliminar, alignment=Qt.AlignCenter)
        
        btn_editar = QPushButton("Editar Usuario")
        btn_editar.clicked.connect(self.edit_user)
        layout.addWidget(btn_editar, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def refresh_user_list(self):
        """Refresh user list."""
        self.user_list.clear()
        users = AuthService.get_all_users_details()
        
        for user in users:
            self.user_list.addItem(f"{user[0]} - {user[1] if user[1] else ''}")
    
    def create_user(self):
        """Create new user."""
        username = self.new_username.text().strip()
        password = self.new_password.text().strip()
        email = self.new_email.text().strip()
        
        if not username or not password or not email:
            QMessageBox.critical(self, "Error", "Todos los campos son requeridos.")
            return
        
        result = AuthService.create_user(username, password, email)
        
        if result["success"]:
            QMessageBox.information(self, "Éxito", "Usuario creado correctamente.")
            self.refresh_user_list()
            self.new_username.clear()
            self.new_password.clear()
            self.new_email.clear()
        else:
            QMessageBox.critical(self, "Error", result["error"])
    
    def delete_user(self):
        """Delete selected user."""
        selected = self.user_list.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione un usuario para eliminar.")
            return
        
        user_info = selected.text()
        username = user_info.split(" - ")[0]
        
        result = AuthService.delete_user(username)
        
        if result["success"]:
            QMessageBox.information(self, "Éxito", "Usuario eliminado.")
        else:
            QMessageBox.critical(self, "Error", result["error"])
        
        self.refresh_user_list()
    
    def edit_user(self):
        """Edit selected user."""
        selected = self.user_list.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione un usuario para editar.")
            return
        
        user_info = selected.text()
        username = user_info.split(" - ")[0]
        
        new_username, ok1 = QInputDialog.getText(
            self, "Editar Usuario", "Nuevo username:", text=username
        )
        new_password, ok2 = QInputDialog.getText(
            self, "Editar Usuario", "Nueva contraseña:",
            echo=QLineEdit.Password
        )
        new_email, ok3 = QInputDialog.getText(
            self, "Editar Usuario", "Nuevo email:"
        )
        
        if not (ok1 and ok2 and ok3 and new_username and new_password and new_email):
            QMessageBox.critical(self, "Error", "Edición cancelada.")
            return
        
        result = AuthService.update_user(username, new_username, new_password, new_email)
        
        if result["success"]:
            QMessageBox.information(self, "Éxito", "Usuario actualizado.")
        else:
            QMessageBox.critical(self, "Error", result["error"])
        
        self.refresh_user_list()


class GestionCultivoScreen(QWidget):
    """Screen for managing crop cultivation records (admin only)."""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout(self)
        
        title = QLabel("Gestión Cultivo")
        title.setFont(QFont("Helvetica", 18, QFont.Bold))
        layout.addWidget(title, alignment=Qt.AlignCenter)
        
        btn_registrar = QPushButton("Registrar Gestión Cultivo")
        btn_registrar.clicked.connect(self.registrar_gestion)
        layout.addWidget(btn_registrar, alignment=Qt.AlignCenter)
        
        self.gestion_list = QListWidget()
        layout.addWidget(self.gestion_list)
        self.cargar_gestiones()
        
        btn_editar = QPushButton("Editar Seleccionada")
        btn_editar.clicked.connect(self.editar_gestion)
        layout.addWidget(btn_editar, alignment=Qt.AlignCenter)
        
        btn_eliminar = QPushButton("Eliminar Seleccionada")
        btn_eliminar.clicked.connect(self.eliminar_gestion)
        layout.addWidget(btn_eliminar, alignment=Qt.AlignCenter)
        
        btn_volver = QPushButton("Volver")
        btn_volver.clicked.connect(lambda: self.controller.show_screen("main"))
        layout.addWidget(btn_volver, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
    
    def cargar_gestiones(self):
        """Load cultivation management records."""
        self.gestion_list.clear()
        gestiones = CatalogoService.get_gestion_cultivo_raw()
        
        for g in gestiones:
            self.gestion_list.addItem(
                f"Código: {g[0]} | Persona ID: {g[1]} | Hortaliza ID: {g[2]} | "
                f"Suelo ID: {g[3]} | Clima ID: {g[4]} | Video: {g[5]}"
            )
    
    def registrar_gestion(self):
        """Register new cultivation management record."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Registrar Gestión Cultivo")
        d_layout = QFormLayout(dialog)
        
        personas = AuthService.get_all_users()
        if not personas:
            QMessageBox.critical(dialog, "Error", "No hay usuarios registrados.")
            return
        
        personas_dict = {f"{p[0]}: {p[1]}": p[0] for p in personas}
        combo_persona = QComboBox()
        combo_persona.addItems(list(personas_dict.keys()))
        d_layout.addRow("Seleccione Persona:", combo_persona)
        
        hort_data = CatalogoService.get_all_tipo_hortaliza()
        if not hort_data:
            QMessageBox.critical(dialog, "Error", "No hay tipos de hortaliza.")
            return
        
        hort_dict = {f"{h[0]}: {h[1]}": h[0] for h in hort_data}
        combo_hortaliza = QComboBox()
        combo_hortaliza.addItems(list(hort_dict.keys()))
        d_layout.addRow("Seleccione Tipo de Hortaliza:", combo_hortaliza)
        
        suelo_data = CatalogoService.get_all_tipo_suelo()
        if not suelo_data:
            QMessageBox.critical(dialog, "Error", "No hay tipos de suelo.")
            return
        
        suelo_dict = {f"{s[0]}: {s[1]}": s[0] for s in suelo_data}
        combo_suelo = QComboBox()
        combo_suelo.addItems(list(suelo_dict.keys()))
        d_layout.addRow("Seleccione Tipo de Suelo:", combo_suelo)
        
        clima_data = CatalogoService.get_all_clima()
        if not clima_data:
            QMessageBox.critical(dialog, "Error", "No hay climas registrados.")
            return
        
        clima_dict = {f"{c[0]}: {c[1]}": c[0] for c in clima_data}
        combo_clima = QComboBox()
        combo_clima.addItems(list(clima_dict.keys()))
        d_layout.addRow("Seleccione Clima:", combo_clima)
        
        entry_video = QLineEdit()
        d_layout.addRow("Video (URL o ruta):", entry_video)
        
        entry_obs = QLineEdit()
        d_layout.addRow("Observaciones:", entry_obs)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        d_layout.addRow(buttons)
        
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        
        if dialog.exec_() == QDialog.Accepted:
            try:
                id_persona = personas_dict[combo_persona.currentText()]
                id_hortaliza = hort_dict[combo_hortaliza.currentText()]
                id_suelo = suelo_dict[combo_suelo.currentText()]
                id_clima = clima_dict[combo_clima.currentText()]
                
                CatalogoService.create_gestion_cultivo(
                    id_persona, id_hortaliza, id_suelo, id_clima,
                    entry_video.text().strip(), entry_obs.text().strip()
                )
                QMessageBox.information(self, "Éxito", "Gestión cultivo registrada.")
                self.cargar_gestiones()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")
    
    def editar_gestion(self):
        """Edit selected cultivation management record."""
        selected = self.gestion_list.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione una gestión para editar.")
            return
        
        line = selected.text()
        codigo = int(line.split("|")[0].split(":")[1].strip())
        
        data = CatalogoService.get_gestion_by_id(codigo)
        if not data:
            QMessageBox.critical(self, "Error", "No se encontró la gestión.")
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Gestión Cultivo")
        d_layout = QFormLayout(dialog)
        
        personas = AuthService.get_all_users()
        personas_dict = {f"{p[0]}: {p[1]}": p[0] for p in personas}
        combo_persona = QComboBox()
        combo_persona.addItems(list(personas_dict.keys()))
        
        for key, value in personas_dict.items():
            if value == data[0]:
                index = combo_persona.findText(key)
                combo_persona.setCurrentIndex(index)
                break
        
        d_layout.addRow("Seleccione Persona:", combo_persona)
        
        hort_data = CatalogoService.get_all_tipo_hortaliza()
        hort_dict = {f"{h[0]}: {h[1]}": h[0] for h in hort_data}
        combo_hortaliza = QComboBox()
        combo_hortaliza.addItems(list(hort_dict.keys()))
        
        for key, value in hort_dict.items():
            if value == data[1]:
                index = combo_hortaliza.findText(key)
                combo_hortaliza.setCurrentIndex(index)
                break
        
        d_layout.addRow("Seleccione Tipo de Hortaliza:", combo_hortaliza)
        
        suelo_data = CatalogoService.get_all_tipo_suelo()
        suelo_dict = {f"{s[0]}: {s[1]}": s[0] for s in suelo_data}
        combo_suelo = QComboBox()
        combo_suelo.addItems(list(suelo_dict.keys()))
        
        for key, value in suelo_dict.items():
            if value == data[2]:
                index = combo_suelo.findText(key)
                combo_suelo.setCurrentIndex(index)
                break
        
        d_layout.addRow("Seleccione Tipo de Suelo:", combo_suelo)
        
        clima_data = CatalogoService.get_all_clima()
        clima_dict = {f"{c[0]}: {c[1]}": c[0] for c in clima_data}
        combo_clima = QComboBox()
        combo_clima.addItems(list(clima_dict.keys()))
        
        for key, value in clima_dict.items():
            if value == data[3]:
                index = combo_clima.findText(key)
                combo_clima.setCurrentIndex(index)
                break
        
        d_layout.addRow("Seleccione Clima:", combo_clima)
        
        entry_video = QLineEdit()
        entry_video.setText(data[4])
        d_layout.addRow("Video (URL o ruta):", entry_video)
        
        entry_obs = QLineEdit()
        entry_obs.setText(data[5])
        d_layout.addRow("Observaciones:", entry_obs)
        
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        d_layout.addRow(buttons)
        
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        
        if dialog.exec_() == QDialog.Accepted:
            try:
                id_persona = personas_dict[combo_persona.currentText()]
                id_hortaliza = hort_dict[combo_hortaliza.currentText()]
                id_suelo = suelo_dict[combo_suelo.currentText()]
                id_clima = clima_dict[combo_clima.currentText()]
                
                CatalogoService.update_gestion_cultivo(
                    codigo, id_persona, id_hortaliza, id_suelo, id_clima,
                    entry_video.text().strip(), entry_obs.text().strip()
                )
                QMessageBox.information(self, "Éxito", "Gestión cultivo actualizada.")
                self.cargar_gestiones()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")
    
    def eliminar_gestion(self):
        """Delete selected cultivation management record."""
        selected = self.gestion_list.currentItem()
        if not selected:
            QMessageBox.critical(self, "Error", "Seleccione una gestión para eliminar.")
            return
        
        line = selected.text()
        codigo = int(line.split("|")[0].split(":")[1].strip())
        
        if QMessageBox.question(
            self, "Confirmar",
            f"¿Está seguro de eliminar la gestión con código {codigo}?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            try:
                CatalogoService.delete_gestion_cultivo(codigo)
                QMessageBox.information(self, "Éxito", "Gestión cultivo eliminada.")
                self.cargar_gestiones()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error: {str(e)}")


# Import missing components
from PyQt5.QtWidgets import QLabel
