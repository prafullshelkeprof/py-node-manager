# Node Operations API

This is a FastAPI-based API that allows performing operations on a tree-like structure of nodes. The API provides endpoints to get all nodes, get a specific node by ID, add a new node under a parent node, and change the parent of a node.

## Getting Started

To set up and run the API locally, follow these steps:

1. Install dependencies:
   - Create a new Python 3.7+ virtual environment.
   - Activate the virtual environment.
   - Install the required packages by running `pip install -r requirements.txt`.

2. Run the API:
   - Run the FastAPI application using `uvicorn`:
     ```
     uvicorn main:app --reload
     ```
     This will start the API on `http://localhost:8000`.

3. API Endpoints:
   - **GET /get_all_nodes**: Returns all nodes in the tree structure.
   - **GET /nodes/{node_id}**: Returns a specific node by its ID.
   - **POST /add_new_node**: Adds a new node under a parent node.
   - **POST /change_parent/{node_id}**: Changes the parent of a node.

## API Endpoints

### GET /get_all_nodes

Returns all nodes in the tree structure.

**Example Request:**
```
GET /get_all_nodes
```

**Example Response:**
```json
{
  "message": [
    {
      "name": "Node 1",
      "id": "123",
      "nodeHeight": 0,
      "nodeType": "root",
      "children": [
        {
          "name": "Node 1.1",
          "id": "456",
          "nodeHeight": 1,
          "nodeType": "manager",
          "parentId": "123",
          "departmentName": ["department_1"],
          "children": []
        }
      ]
    }
  ]
}
```

### GET /nodes/{node_id}

Returns a specific node by its ID.

**Example Request:**
```
GET /nodes/123
```

**Example Response:**
```json
{
  "message": {
    "name": "Node 1",
    "id": "123",
    "nodeHeight": 0,
    "nodeType": "root",
    "children": [
      {
        "name": "Node 1.1",
        "id": "456",
        "nodeHeight": 1,
        "nodeType": "dev",
        "parentId": "123",
        "preferredLang": ["Python", "JavaScript"],
        "children": []
      }
    ]
  }
}
```

### POST /add_new_node

Adds a new node under a parent node.

**Example Request:**
```
POST /add_new_node
```
**Request Body:**
```json
{
  "parent_id": "123",
  "new_node": {
    "name": "Node 1.2",
    "nodeType": "dev",
    "departmentName": ["department_1"],
    "preferredLang": ["Python", "JavaScript"]
  }
}
```

**Example Response:**
```json
{
  "message": "Node added successfully"
}
```

### POST /change_parent/{node_id}

Changes the parent of a node.

**Request Parameters:**
- `node_id` (path parameter): The ID of the node to change the parent of.
- Request Body (JSON):
  ```json
  {
    "new_parent_id": "123"
  }
  ```

**Example Request:**
```
POST /change_parent/456
```
**Request Body:**
```json
{
  "new_parent_id": "789"
}
```

**Example Response:**
```json
{
  "message": "Parent node changed successfully"
}
```

## Future Development

## API Endpoints

### DELETE /delete_node/{node_id}

Delete current node from the tree.

### POST /promote_node/{node_id}

Change current node type from dev to manager or from manager to ceo.

**Request Body:**
```json
{
  "new_node_type": "manager|dev"
}
```