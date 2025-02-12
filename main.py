from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static, Tabs, Tab


class MainApp(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Tabs(
            Tab("Inventory", id="inventory"),
            Tab("Recipes", id="recipes"),
            Tab("Shopping Lists", id="shopping_lists")
        )
        yield Footer()


if __name__ == "__main__":
    app = MainApp()
    app.run()
