"""Application stylesheet configuration."""


def get_stylesheet():
    """Get application stylesheet."""
    return """
        QMainWindow {
            background-color: #e8f5e9;
        }
        QPushButton {
            background-color: #66bb6a;
            border: none;
            border-radius: 5px;
            padding: 8px 15px;
            font-size: 14px;
            color: white;
        }
        QPushButton:hover {
            background-color: #4caf50;
        }
        QLabel {
            color: #33691e;
        }
        QLineEdit, QComboBox, QTextEdit, QListWidget {
            background-color: #f1f8e9;
            border: 1px solid #c5e1a5;
            border-radius: 3px;
            padding: 4px;
        }
    """
