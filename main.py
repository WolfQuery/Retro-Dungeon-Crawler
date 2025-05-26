# Main file
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from GUI.Inventory import InventoryWidget

class MainGame(App):
    def compose(self) -> ComposeResult:
        yield Footer()
        yield Header()
        yield InventoryWidget()

        

if __name__ == "__main__":
    app = MainGame()
    app.run()