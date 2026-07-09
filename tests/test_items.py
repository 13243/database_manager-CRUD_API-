from app.schemas import Item

def test_create_item(client):
    response = client.post(
        "/items/",
        json={"name": "Laptop", "description": "Gaming laptop", "price": 1500.99}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 1500.99
    assert "id" in data

def test_read_items(client):
    # Create one first
    client.post("/items/", json={"name": "Mouse", "description": "Wireless", "price": 29.99})
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["name"] == "Mouse"

def test_read_single_item(client):
    create_resp = client.post("/items/", json={"name": "Keyboard", "description": "Mechanical", "price": 89.99})
    item_id = create_resp.json()["id"]
    
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Keyboard"

def test_read_item_not_found(client):
    response = client.get("/items/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_update_item(client):
    create_resp = client.post("/items/", json={"name": "Monitor", "description": "4K", "price": 450.0})
    item_id = create_resp.json()["id"]
    
    response = client.put(
        f"/items/{item_id}",
        json={"name": "Monitor Ultra HD", "description": "4K 144Hz", "price": 550.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Monitor Ultra HD"
    assert data["price"] == 550.0

def test_delete_item(client):
    create_resp = client.post("/items/", json={"name": "Tablet", "description": "10 inch", "price": 300.0})
    item_id = create_resp.json()["id"]
    
    delete_resp = client.delete(f"/items/{item_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["id"] == item_id
    
    # Verify it's gone
    get_resp = client.get(f"/items/{item_id}")
    assert get_resp.status_code == 404
