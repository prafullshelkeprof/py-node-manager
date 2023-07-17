from fastapi import APIRouter
from node_operations import load_nodes, save_nodes, find_node, find_parent
from models import ChangeParentRequest

router = APIRouter()


@router.post("/change_parent/{node_id}")
async def change_parent(node_id: str, request: ChangeParentRequest):
    nodes = load_nodes()
    node = find_node(nodes, node_id)
    new_parent = find_node(nodes, request.new_parent_id)

    if node is not None and new_parent is not None:
        old_parent = find_parent(nodes, node_id)
        if old_parent is not None:
            old_parent["children"].remove(node)
        new_parent.setdefault("children", []).append(node)
        parent_height = new_parent.get('nodeHeight')
        print(parent_height + 1)
        print(node.get('nodeHeight'))
        node['nodeHeight'] = parent_height + 1
        print(node.get('nodeHeight'))
        save_nodes(nodes)
        return {"message": "Parent node changed successfully"}
    else:
        return {"message": "Node or new parent not found"}
