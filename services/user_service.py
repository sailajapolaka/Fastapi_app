from fastapi import HTTPException
from models.models import Item

class ItemService:
    def __init__(self):
        self.items = []

    def create_item(self, item: Item):
        self.items.append(item.name)
        return {"message": "Item added successfully", "items": self.items}

    def update_item(self, item_id: int, updated_item: Item):
        if item_id < 0 or item_id >= len(self.items):
            raise HTTPException(status_code=404, detail="Item not found")
        self.items[item_id] = updated_item.name
        return {"message": "Item updated successfully", "items": self.items}

    def delete_item(self, item_id: int):
        if item_id < 0 or item_id >= len(self.items):
            raise HTTPException(status_code=404, detail="Item not found")
        deleted_item = self.items.pop(item_id)
        return {"message": f"Item '{deleted_item}' deleted successfully", "items": self.items}
def delete_all_items(self):
        self.items.clear()
        return {"message": "All items deleted successfully", "items": self.items}