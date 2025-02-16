from datetime import datetime

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import (Header, Footer,
                             TabbedContent, TabPane, ListView,
                             ListItem, Static, Button, Input)

class NavigationBar(Horizontal):
    """The main navigation bar that houses the Inventory, Recipe Book, and Shopping Lists tabs aligned to the left along with
    the Add, Edit, and Delete Buttons aligned to the right."""
    def compose(self) -> ComposeResult:
        yield Static()

class InventoryPanel(Static):
    """The panel that houses the Inventory content."""
    def compose(self) -> ComposeResult:
        yield Static()

class RecipeBookPanel(Static):
    """The panel that houses the Recipe Book content."""
    def compose(self) -> ComposeResult:
        yield Static()

class ShoppingListsPanel(Static):
    """The panel that houses the Shopping Lists content."""
    def compose(self) -> ComposeResult:
        yield Static()

class AddItem(Static):
    """The sub-menu to add an item."""
    def compose(self) -> ComposeResult:
        yield Static()

class EditItem(Static):
    """The sub-menu to edit an item."""
    def compose(self) -> ComposeResult:
        yield Static()

class DeleteItem(Static):
    """The sub-menu to delete an item."""
    def compose(self) -> ComposeResult:
        yield Static()

class AddRecipe(Static):
    """The sub-menu to add a recipe."""
    def compose(self) -> ComposeResult:
        yield Static()

class EditRecipe(Static):
    """The sub-menu to edit a recipe."""
    def compose(self) -> ComposeResult:
        yield Static()

class DeleteRecipe(Static):
    """The sub-menu to delete a recipe."""
    def compose(self) -> ComposeResult:
        yield Static()

class WarningDialog(Static):
    def compose(self) -> ComposeResult:
        yield Static()

class HelpMenu(Static):
    def compose(self) -> ComposeResult:
        yield Static()

class MainApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield NavigationBar()
        yield Footer()


if __name__ == "__main__":
    app = MainApp()
    app.run()