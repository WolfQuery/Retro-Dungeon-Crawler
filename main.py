# Main file
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Label

class IDK(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode.")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Button(
            label="Button",
            variant="error",
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        yield Button(label="Button 2", variant="warning")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    

if __name__ == "__main__":
    app = IDK()
    app.run()