
from fastapi import APIRouter

router = APIRouter()

# ✅ Define the global items list
items = []  # This must be outside the functions to persist data

@router.get("/items")
def get_items():
    return {"items": items}

@router.post("/items")
def create_item(item: str):
    global items  # ✅ Ensure items is recognized as the global list
    items.append(item)
    print("Current items list:", items)  # Debugging
    return {"message": f"Item '{item}' added successfully", "items": items}

@router.put("/items/{item_id}")
def update_item(item_id: int, updated_item: str):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    items[item_id] = updated_item
    return {"message": f"Item {item_id} updated to '{updated_item}'", "items": items}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    deleted_item = items.pop(item_id)
    return {"message": f"Item '{deleted_item}' deleted successfully", "items": items}

@router.delete("/items")
def delete_all_items():
    global items  # ✅ Ensure items is recognized as the global list
    items.clear()
    return {"message": "All items deleted successfully", "items": items}  # ✅ Fixed line
