from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QCheckBox
from gui_components.gear_selector import GearSelector
from gui_components.stat_slider import StatSliderPanel
from gui_components.result_display import ResultDisplay
from optimizer import score_armor_set, calculate_total_mitigation, calculate_total_resistance
from gear_data import headgear, chestgear, armgear, leggear, ArmorPiece
import itertools
import sys

class GearOptimizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gear Optimizer")

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.gear_selector = GearSelector()
        main_layout.addWidget(self.gear_selector)

        # High Madness checkbox
        self.madness_checkbox = QCheckBox("High madness?")
        self.madness_checkbox.setChecked(True)
        main_layout.addWidget(self.madness_checkbox)

        horizontal = QHBoxLayout()

        # Left: Sliders + Button
        left_panel = QVBoxLayout()
        self.weight_slider = StatSliderPanel()
        left_panel.addWidget(self.weight_slider)

        self.run_button = QPushButton("Run Optimization")
        self.run_button.clicked.connect(self.run_optimization)
        left_panel.addWidget(self.run_button)
        horizontal.addLayout(left_panel, 3)

        # Right: Results
        self.results = ResultDisplay()
        horizontal.addWidget(self.results, 1)

        main_layout.addLayout(horizontal)

    def run_optimization(self):
        selected_gear = self.gear_selector.get_selected_gear()
        weights = self.weight_slider.get_weights()
        base_resistance_stat = 130 if self.madness_checkbox.isChecked() else 100

        best_score = float("-inf")
        best_combo = None

        for combo in itertools.product(*selected_gear.values()):
            score = score_armor_set(combo, weights, base_resistance_stat)
            if score > best_score:
                best_score = score
                best_combo = combo

        mitigation = calculate_total_mitigation(best_combo)
        resistance = calculate_total_resistance(best_combo, base_resistance_stat)
        self.results.display_results(best_combo, mitigation, resistance, best_score)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GearOptimizerApp()
    window.resize(1600, 800)
    window.show()
    sys.exit(app.exec())
