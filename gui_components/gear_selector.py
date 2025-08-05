from PySide6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QCheckBox, QHBoxLayout, QComboBox, QScrollArea, QLabel, \
    QSpacerItem, QSizePolicy
from gear_data import headgear, chestgear, handgear, leggear
from collections import defaultdict

# Allow users to check and uncheck which gear they have access to currently
class GearSelector(QWidget):
    def __init__(self):
        self.chapter_map = defaultdict(list)
        super().__init__()
        outer_layout = QVBoxLayout(self)
        self.checkboxes = {"head": [], "chest": [], "arms": [], "legs": []}

        # DLC + Chapter selection controls
        top_controls = QHBoxLayout()
        gear_layout = QHBoxLayout()

        self.dlc_checkbox = QCheckBox("DLC Armor")
        self.dlc_checkbox.setChecked(True)
        self.dlc_checkbox.stateChanged.connect(self.toggle_dlc_armor)
        top_controls.addWidget(self.dlc_checkbox)

        # Add fixed 100px spacing between checkbox and dropdown
        spacer = QSpacerItem(100, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        top_controls.addItem(spacer)

        # Chapter label + dropdown
        chapter_label = QLabel("Max Chapter:")
        top_controls.addWidget(chapter_label)

        self.chapter_dropdown = QComboBox()
        self.chapter_dropdown.addItems([f"Chapter {i}" for i in range(1, 6)])
        self.chapter_dropdown.setCurrentIndex(4)
        self.chapter_dropdown.setFixedWidth(300)
        self.chapter_dropdown.currentIndexChanged.connect(self.update_chapter_filter)
        top_controls.addWidget(self.chapter_dropdown)

        # Push everything else to the left
        top_controls.addStretch()

        outer_layout.addLayout(top_controls)

        for slot, gear_dict in zip(["head", "chest", "arms", "legs"], [headgear, chestgear, handgear, leggear]):
            group = QGroupBox(f"{slot.capitalize()} Gear")
            vbox = QVBoxLayout()
            for name, item in gear_dict.items():
                cb = QCheckBox(name)
                cb.setChecked(True)  # default to enabled
                vbox.addWidget(cb)
                self.checkboxes[slot].append((cb, item))
                self.chapter_map[item.chapter].append(cb)
            scroll = QScrollArea()
            inner = QWidget()
            inner.setLayout(vbox)
            scroll.setWidget(inner)
            scroll.setWidgetResizable(True)
            scroll.setFixedHeight(200)
            group.setLayout(QVBoxLayout())
            group.layout().addWidget(scroll)
            gear_layout.addWidget(group)

        outer_layout.addLayout(gear_layout)

    def get_selected_gear(self):
        selected = {}
        for slot, items in self.checkboxes.items():
            selected[slot] = [item for cb, item in items if cb.isChecked()]
        return selected

    def toggle_dlc_armor(self):
        checked = self.dlc_checkbox.isChecked()
        for cb in self.chapter_map[0]:  # DLC gear = chapter 0
            cb.setChecked(checked)

    def update_chapter_filter(self):
        max_chapter = self.chapter_dropdown.currentIndex() + 1
        for chapter, checkboxes in self.chapter_map.items():
            if chapter == 0:
                continue  # DLC handled separately
            for cb in checkboxes:
                cb.setChecked(chapter <= max_chapter)
