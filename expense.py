import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class ExpenseTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Expense Tracker')

        # Create labels, line edits, and buttons for each expense category.
        self.labels = []
        self.line_edits = []

        categories = ['Gas', 'Food', 'Utilities', 'Entertainment', 'Others']  # Add more categories as needed

        self.layout = QVBoxLayout()

        for category in categories:
            label = QLabel(category + ':')
            line_edit = QLineEdit()
            self.labels.append(label)
            self.line_edits.append(line_edit)

            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_expenses)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def save_expenses(self):
        # Retrieve the entered expenses for each category and save them
        expenses = {}
        for label, line_edit in zip(self.labels, self.line_edits):
            category = label.text().split(':')[0]
            expense = line_edit.text()
            expenses[category] = expense

        print("Expenses saved:", expenses)  # For demonstration, you can save this data to a file or database


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()
    sys.exit(app.exec_())