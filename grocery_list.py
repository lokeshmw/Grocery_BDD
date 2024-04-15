class GroceryList:
    def __init__(self):
        self.items = []

    def add_item(self, item_list):
        for i in item_list:
            self.items.append(i)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError(f"{item} is not in the list")

    def check_off_item(self, item):
        if item in self.items:
            # Mark item as purchased
            self.items.remove(item)
        else:
            raise ValueError(f"{item} is not in the list")


grocery_list = GroceryList()