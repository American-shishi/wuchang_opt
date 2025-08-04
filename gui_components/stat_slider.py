from PySide6.QtWidgets import QWidget, QFormLayout, QSlider, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt

class StatSliderPanel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        instructions = QLabel("Adjust the sliders to indicate how much you value each type of defense. Higher values prioritize that stat more in the optimization.")
        instructions.setWordWrap(True)
        instructions.setStyleSheet("margin-bottom: 10px; font-style: italic;")
        layout.addWidget(instructions)

        self.sliders = {"mitigation": {}, "resistance": {}}

        self.ranges = {
            "mitigation": {
                "Slash": (0.1, 5), "Blunt": (0.1, 5), "Stab": (0.1, 5),
                "Feathering": (0.1, 5), "Magic": (0.1, 5), "Lightning": (0.1, 5),
                "Fire": (0.1, 5), "Tenacity": (0.1, 5)
            },
            "resistance": {
                "Blight": (0.1, 2), "PoiseBreak": (0.1, 2), "Burn": (0.1, 2),
                "Frostbite": (0.1, 2), "Corruption": (0.1, 2),
                "Despair": (0.1, 2), "Paralysis": (0.1, 2)
            }
        }

        for i, (group_name, stats) in enumerate(self.ranges.items()):
            if i > 0:
                layout.addSpacing(15)
                layout.addWidget(QLabel("—" * 40))
            group_label = QLabel(group_name.capitalize())
            group_label.setStyleSheet("font-weight: bold; font-size: 12pt; margin-bottom: 5px;")
            layout.addWidget(group_label)

            form = QFormLayout()
            layout.addLayout(form)

            for stat, (min_val, max_val) in stats.items():
                slider = QSlider(Qt.Horizontal)
                slider.setMinimum(0)
                slider.setMaximum(1000)

                # Set default values (just based on personal preference)
                if group_name == "mitigation":
                    if stat in ["Slash", "Blunt", "Stab"]:
                        default_val = 3
                    elif stat == "Tenacity":
                        default_val = 0.25
                    else:
                        default_val = 0.5
                else:
                    default_val = 0.1

                # Scale to 0–1000
                normalized = (default_val - min_val) / (max_val - min_val)
                normalized = max(0, min(1, normalized))
                slider.setValue(int(1000 * normalized))

                label = QLabel()
                def update_label(val, s=slider, l=label, mi=min_val, ma=max_val):
                    scaled = mi + (val / 1000) * (ma - mi)
                    l.setText(f"{scaled:.2f}")
                slider.valueChanged.connect(update_label)
                update_label(slider.value())

                hbox = QHBoxLayout()
                hbox.addWidget(slider)
                hbox.addWidget(label)
                form.addRow(f"{stat}", hbox)
                self.sliders[group_name][stat] = (slider, min_val, max_val)

    def get_weights(self):
        weights = {"mitigation": {}, "resistance": {}}
        for group in self.sliders:
            for stat, (slider, min_val, max_val) in self.sliders[group].items():
                val = slider.value()
                scaled = min_val + (val / 1000) * (max_val - min_val)
                weights[group][stat] = scaled
        return weights
