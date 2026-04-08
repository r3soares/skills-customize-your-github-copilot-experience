"""
Starter code for FastAPI REST API Assignment

Complete the tasks by implementing the endpoints and models below.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize FastAPI app
app = FastAPI()

# TODO: Define a Pydantic model for your data (e.g., Item, Task)
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: str = None
#     price: float

# TODO: Create an in-memory database (you can use a list or dictionary)
# Example:
# items_db = [
#     {"id": 1, "name": "Item 1", "description": "Description", "price": 9.99}
# ]


# TODO: Implement GET /items/ - retrieve all items
@app.get("/items/")
def get_items() -> List:
    """Retrieve all items from the database"""
    pass


# TODO: Implement GET /items/{item_id} - retrieve a specific item
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    pass


# TODO: Implement POST /items/ - create a new item
@app.post("/items/")
def create_item(item):
    """Create a new item"""
    pass


# TODO: Implement PUT /items/{item_id} - update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item):
    """Update an existing item"""
    pass


# TODO: Implement DELETE /items/{item_id} - delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by ID"""
    pass


if __name__ == "__main__":
    import uvicorn
    # Run the server with: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
