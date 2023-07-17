from fastapi import APIRouter
from node_operations import load_nodes, save_nodes, find_node
from models import Node, NewNode
import uuid


router = APIRouter()


@router.get("/get_all_nodes")
async def get_nodes():
    nodes = load_nodes()
    return {"message": nodes}


@router.get("/nodes/{node_id}")
async def get_node(node_id: str):
    nodes = load_nodes()
    node = find_node(nodes, node_id)

    if node is not None:
        return {"message": node}

    return {"message": "Node not found"}


@router.post("/add_new_node")
async def add_node(parent_id: str, new_node: NewNode):
    nodes = load_nodes()
    print('add new node')
    parent_node = find_node(nodes, parent_id)
    print('parent new node')
    if parent_node:
        full_node = Node(
            name=new_node.name,
            id=str(uuid.uuid4()),
            nodeHeight=parent_node.get('nodeHeight') + 1,
            nodeType=new_node.nodeType,
            parentName=parent_node.get('name'),
            parentId=parent_node.get('id'),
            children=[],
        )
        print('full node new')
        for attribute, value in new_node.model_dump().items():
            setattr(full_node, attribute, value)
        parent_node.setdefault("children", []).append(full_node.model_dump())
        save_nodes(nodes)
        return {"message": "Node added successfully"}
    else:
        return {"message": "Parent node not found"}
