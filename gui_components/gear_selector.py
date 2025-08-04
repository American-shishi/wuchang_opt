from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QCheckBox, QHBoxLayout, QLabel, QScrollArea
from gear_data import headgear, chestgear, armgear, leggear

class GearSelector(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        self.checkboxes = {"head": [], "chest": [], "arms": [], "legs": []}

        for slot, gear_dict in zip(["head", "chest", "arms", "legs"], [headgear, chestgear, armgear, leggear]):
            group = QGroupBox(f"{slot.capitalize()} Gear")
            vbox = QVBoxLayout()
            for name, item in gear_dict.items():
                cb = QCheckBox(name)
                cb.setChecked(True)  # default to enabled
                vbox.addWidget(cb)
                self.checkboxes[slot].append((cb, item))
            scroll = QScrollArea()
            inner = QWidget()
            inner.setLayout(vbox)
            scroll.setWidget(inner)
            scroll.setWidgetResizable(True)
            scroll.setFixedHeight(200)
            group.setLayout(QVBoxLayout())
            group.layout().addWidget(scroll)
            layout.addWidget(group)

    def get_selected_gear(self):
        selected = {}
        for slot, items in self.checkboxes.items():
            selected[slot] = [item for cb, item in items if cb.isChecked()]
        return selected