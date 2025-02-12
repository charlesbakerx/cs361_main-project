from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import (Header, Footer,
                             TabbedContent, TabPane, ListView,
                             ListItem, Static, Button, Input)


class MainApp(App):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handler for button presses to add and remove items"""
        if event.button.id == "add_item":
            input_widget = self.query_one("#item_input_field", Input)
            item_name = input_widget.value.strip()
            if item_name:
                self.inventory_list.append(ListItem(Static(item_name)))
                input_widget.value = ""

        elif event.button.id == "remove_item":
            if self.inventory_list.children:
                self.inventory_list.remove_child(
                    self.inventory_list.children[-1])

    def compose(self) -> ComposeResult:
        yield Header()

        with TabbedContent():
            with TabPane("Inventory"):
                self.inventory_list = ListView()
                yield self.inventory_list
                yield Input(placeholder="Enter item name", id="item_input_field")
                yield Button("Add Item", id="add_item")
                yield Button("Remove Selected", id="remove_item")

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
