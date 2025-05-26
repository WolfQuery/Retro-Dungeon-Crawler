# Main inventory GUI
from textual.app import App, ComposeResult
from textual.widgets import Static

class InventoryWidget(Static):
    def on_mount(self) -> None:
        # Set up the widget content.
        self.update("Inventory:\n• Sword\n• Potion\n• Shield")
        # Initially hidden: using a simple flag via the widget’s class or style.
        self.styles.display = "none"  # "none" hides the widget