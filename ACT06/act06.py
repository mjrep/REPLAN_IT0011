class Item:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ₱{self.price:.2f}"


class ItemManagement:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if any(existing_item.id == item.id for existing_item in self.items):
            raise ValueError("Item with the same ID already exists.")
        if item.price < 0:
            raise ValueError("Price cannot be negative.")
        self.items.append(item)
        print("Item added successfully.")

    def get_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        raise ValueError("Item not found.")

    def update_item(self, item_id, name=None, description=None, price=None):
        item = self.get_item(item_id)
        if name:
            item.name = name
        if description:
            item.description = description
        if price:
            if price < 0:
                raise ValueError("Price cannot be negative.")
            item.price = price
        print("Item updated successfully.")

    def delete_item(self, item_id):
        item = self.get_item(item_id)
        self.items.remove(item)
        print("Item deleted successfully.")

    def list_items(self):
        if not self.items:
            print("No items available.")
        for item in self.items:
            print(item)


def main():
    manager = ItemManagement()

    while True:
        print("\nItem Management Application")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List All Items")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                item = Item(id, name, description, price)
                manager.add_item(item)

            elif choice == "2":
                item_id = int(input("Enter item ID: "))
                item = manager.get_item(item_id)
                print(item)

            elif choice == "3":
                item_id = int(input("Enter item ID: "))
                name = input("Enter new name: ")
                description = input("Enter new description: ")
                price_input = input("Enter new price: ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name, description, price)

            elif choice == "4":
                item_id = int(input("Enter item ID: "))
                manager.delete_item(item_id)

            elif choice == "5":
                manager.list_items()

            elif choice == "6":
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
