from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QVBoxLayout
from PySide6.QtCore import Qt

class ResultDisplay(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel("Best Combination Results:")
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setStyleSheet("font-family: Consolas; font-size: 12pt;")
        layout.addWidget(self.label)
        layout.addWidget(self.text_area)

    def display_results(self, combo, mitigation, resistance, score):
        output = f"<b>Best In Slots Based on your weights:</b><br><br>"
        for piece in combo:
            output += f"<span style='color:#4CAF50; font-weight:bold'>{piece.slot.capitalize()}: {piece.name}</span><br>"

        output += "<br><b>Mitigation:</b><br>"
        for stat, value in mitigation.items():
            if stat in {"Slash", "Blunt", "Stab"}:
                output += f"<b>{stat:<10}: {value * 100:.2f}%</b><br>"
            else:
                output += f"{stat:<10}: {value * 100:.2f}%<br>"

        output += "<br><b>Resistance:</b><br>"
        for stat, value in resistance.items():
            output += f"{stat:<12}: {value:.2f}<br>"

        self.text_area.setHtml(output)
