from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import (Header, Footer, ListView,
                             ListItem, Static, Button, DataTable)

class NavigationBar(Horizontal):
    """The main navigation bar that houses the Inventory, Recipe Book, and Shopping Lists tabs aligned to the left along with
    the Add, Edit, and Delete Buttons aligned to the right."""

    def compose(self) -> ComposeResult:
        # Left-aligned tabs in a container
        with Horizontal():
            yield Button("Inventory", id="inventory_tab")
            yield Button("Recipe Book", id="recipe_book_tab")
            yield Button("Shopping Lists", id="shopping_lists_tab")

        # Right-aligned buttons in a container
        with Horizontal():
            yield Button("Add", id="add_button")
            yield Button("Edit", id="edit_button")
            yield Button("Delete", id="delete_button")


class InventoryPanel(DataTable):
    """The panel that houses the Inventory content."""
    inventory_data = [
        ("Name", "Quantity", "Unit", "Expiration Date", "Category"),  # Headers
        ("Apples", 1, "lbs", "", "Food"),
        ("Rice", 4, "lbs", "", "Food"),
        ("Chicken", 2, "lbs", "2025-03-20", "Food")
    ]

    def compose(self) -> ComposeResult:
        yield DataTable()
        self.add_columns(*self.inventory_data[0])
        self.add_rows(self.inventory_data[1:])

class RecipeBookPanel(Horizontal):
    """The panel that houses the Recipe Book content."""

    def compose(self):
        # Left side: Data table
        with Vertical():  # Wrap the DataTable in a Vertical container to preserve structure
            self.data_table = DataTable()
            yield self.data_table

        # Right side: List of ingredients and instructions
        with Vertical():  # Stack ingredients and instructions on top of each other
            self.ingredients = ListView()
            self.instructions = Static(
                """Instructions:
1. Marinate Chicken: In a bowl, mix the chicken with 2 tablespoons soy sauce and cornstarch. Let it sit for 10-15 minutes.
2. Prepare Sauce: In a small bowl, combine 3 tablespoons soy sauce, oyster sauce, sesame oil, sugar, and water. Set aside.
3. Cook Chicken: Heat 1 tablespoon of vegetable oil in a large skillet or wok over medium-high heat. Add the marinated chicken and stir-fry until cooked through (about 5-7 minutes). Remove the chicken and set aside.
4. Cook Vegetables: Add the remaining 1 tablespoon of oil to the skillet. Add garlic and ginger, cooking until fragrant (about 30 seconds).
"""
            )
            self.instructions.styles.border = ("solid", "red")  # Optional: Border to visually distinguish
            yield self.ingredients
            yield self.instructions

    def on_mount(self):
        self.data_table.add_columns("Name", "Description")  # Add table columns
        self.data_table.add_rows([
            ("Grilled Cheese Sandwich", "A classic grilled cheese with melted cheese between two buttery"
                                        " toasted bread slices."),
            ("Chicken Stir-Fry", "Sauteed chicken and colorful veggies in a savory soy based sauce.")
        ])

        ingredients_items = [
            "1 lb chicken breast, cut into bite-sized pieces",
            "2 tablespoons soy sauce",
            "1 tablespoon cornstarch",
            "2 tablespoons vegetable oil",
            "1 cup broccoli florets",
            "1 cup bell peppers, sliced (any color)",
            "1 cup carrots, thinly sliced",
            "2 cloves garlic, minced",
            "1 tablespoon ginger, grated",
            "3 tablespoons soy sauce (for sauce)",
            "1 tablespoon oyster sauce (optional)",
            "1 teaspoon sesame oil",
            "1 teaspoon sugar",
            "1/4 cup water",
        ]

        for ingredient in ingredients_items:
            self.ingredients.append(Static(ingredient))


class ShoppingListsPanel(Horizontal):
    """The panel that houses the Shopping Lists content."""

    def compose(self) -> ComposeResult:
        # Left side: List of shopping lists
        with Vertical():
            # Header for the lists
            yield Static("Name")

            # ListView for the lists
            self.shopping_lists = ListView()
            yield self.shopping_lists

        # Right side: DataTable for items in shopping list
        with Vertical():
            self.data_table = DataTable()
            yield self.data_table

    def on_mount(self):
        shopping_list_items = ["Walmart", "Target"]
        for item in shopping_list_items:
            self.shopping_lists.append(ListItem(Static(item)))

        self.data_table.add_columns("Name", "Quantity", "Unit")
        self.data_table.add_rows([("Milk", 1, "gal"), ("Bread", 1, "loaf")])

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
        with Container(id="content"):
            self.inventory_panel = InventoryPanel(id="inventory_panel")
            self.recipe_panel = RecipeBookPanel(id="recipe_panel")
            self.shopping_panel = ShoppingListsPanel(id="shopping_panel")
            self.recipe_panel.styles.display = "none"
            self.shopping_panel.styles.display = "none"
            yield self.inventory_panel
            yield self.recipe_panel
            yield self.shopping_panel
        yield Footer()


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler for button presses. Handles tab switching for the navigation bar."""
        button_id = event.button.id
        container = self.query_one("#content")

        for panel in container.children:
            panel.styles.display = "none"

        # Display the selected panel based on button ID
        if button_id == "inventory_tab":
            container.query_one("#inventory_panel").styles.display = "block"
        elif button_id == "recipe_book_tab":
            container.query_one("#recipe_panel").styles.display = "block"
        elif button_id == "shopping_lists_tab":
            container.query_one("#shopping_panel").styles.display = "block"


if __name__ == "__main__":
    app = MainApp()
    app.run()