from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import (Header, Footer,
                             TabbedContent, TabPane, ListView,
                             Static)


class MainApp(App):

    def compose(self) -> ComposeResult:
        yield Header()

        with TabbedContent():
            with TabPane("Inventory"):
                self.inventory_list = ListView()
                yield self.inventory_list
            with TabPane("Recipe Book"):
                with Horizontal():
                    self.recipe_list = ListView()
                    self.recipe_preview = Static(
                        "This is the recipe preview pane", classes="content")
                    yield self.recipe_list
                    yield self.recipe_preview

            with TabPane("Shopping Lists"):
                with Horizontal():
                    self.shopping_list = ListView()
                    self.shopping_list_items = Static(
                        "This is the items preview pane", classes="content")
                    yield self.shopping_list
                    yield self.shopping_list_items

        yield Footer()


if __name__ == "__main__":
    app = MainApp()
    app.run()
