"""Main application entry point and window controller."""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMessageBox
from PyQt5.QtGui import QFont

from data.database import initialize_db
from ui.styles.stylesheet import get_stylesheet
from ui.screens.login import LoginScreen
from ui.screens.main import MainScreen
from ui.screens.hectareas.register import RegistrarScreen, BuscarScreen, GestionarHectareasScreen
from ui.screens.dashboard import PerfilScreen, InformeScreen, ConsultaScreen
from ui.screens.admin_catalog import TipoHortalizaManagementScreen, TipoSueloManagementScreen, ClimaManagementScreen
from ui.screens.admin_management import UserManagementScreen, GestionCultivoScreen
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_X, WINDOW_Y, ADMIN_ROLE


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Cultivos")
        self.setGeometry(WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # User state
        self.current_user = None
        self.user_role = None
        self.current_email = None
        
        # Stack widget for screen management
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # Apply stylesheet
        self.setStyleSheet(get_stylesheet())
        
        # Initialize screens
        self.screens = self._initialize_screens()
        self._add_screens_to_stack()
        
        # Show login screen
        self.show_screen("login")
    
    def _initialize_screens(self):
        """Initialize all screens."""
        return {
            "login": LoginScreen(self),
            "main": MainScreen(self),
            "registrar": RegistrarScreen(self),
            "buscar": BuscarScreen(self),
            "perfil": PerfilScreen(self),
            "informe": InformeScreen(self),
            "consulta": ConsultaScreen(self),
            "gestionar_hectareas": GestionarHectareasScreen(self),
            "gestion_cultivo": GestionCultivoScreen(self),
            "usuarios": UserManagementScreen(self),
            "gestion_hortaliza": TipoHortalizaManagementScreen(self),
            "gestion_suelo": TipoSueloManagementScreen(self),
            "gestion_clima": ClimaManagementScreen(self),
        }
    
    def _add_screens_to_stack(self):
        """Add all screens to the stack widget."""
        for screen in self.screens.values():
            self.stack.addWidget(screen)
    
    def show_screen(self, name):
        """Show a screen by name."""
        # Check admin-only screens
        if name in ["usuarios", "gestion_cultivo", "gestionar_hectareas"] and self.user_role != ADMIN_ROLE:
            QMessageBox.critical(self, "Acceso Denegado", "Solo el administrador puede acceder a esta opción.")
            return
        
        # Special screen handling
        if name == "login":
            self.screens["login"].refresh_users()
            self.menuBar().clear()
        elif name == "main":
            self.screens["main"].update_header()
            self._update_menu()
        elif name == "perfil":
            self.screens["perfil"].cargar_perfil()
        elif name == "informe":
            self.screens["informe"].cargar_informe()
        
        # Show the screen
        if name in self.screens:
            self.stack.setCurrentWidget(self.screens[name])
    
    def _update_menu(self):
        """Update menu bar based on user role."""
        menu_bar = self.menuBar()
        menu_bar.clear()
        
        if self.user_role == ADMIN_ROLE:
            datos_menu = menu_bar.addMenu("Datos")
            
            accion_gestionar_suelo = datos_menu.addAction("Gestionar Tipos de Suelo")
            accion_gestionar_suelo.triggered.connect(lambda: self.show_screen("gestion_suelo"))
            
            accion_gestionar_clima = datos_menu.addAction("Gestionar Climas")
            accion_gestionar_clima.triggered.connect(lambda: self.show_screen("gestion_clima"))
            
            accion_gestionar_hortaliza = datos_menu.addAction("Gestionar Tipos de Hortaliza")
            accion_gestionar_hortaliza.triggered.connect(lambda: self.show_screen("gestion_hortaliza"))


def main():
    """Main entry point for the application."""
    # Initialize database
    initialize_db()
    
    # Create and run application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
