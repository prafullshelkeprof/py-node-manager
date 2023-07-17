import json
from typing import Optional, Union
from models import Node

NODES_FILE = 'static/node-details.json'


def load_nodes() -> dict:
    with open(NODES_FILE, 'r') as file:
        return json.load(file)


def save_nodes(nodes: dict):
    with open(NODES_FILE, 'w') as file:
        json.dump(nodes, file, indent=2)


def find_node(node: dict, node_id: str) -> Optional[dict]:
    if node.get('id') == node_id:
        return node

    if 'children' in node:
        for child in node['children']:
            found_node = find_node(child, node_id)
            if found_node is not None:
                return found_node

    return None


def find_parent(node: dict, node_id: str) -> Optional[dict]:
    if 'children' in node:
        for child in node['children']:
            if child.get('id') == node_id:
                return node
            found_parent = find_parent(child, node_id)
            if found_parent is not None:
                return found_parent
    return None


def update_node_height(node: Node, height: int):
    node['nodeHeight'] = height
    if node['children'] is not None:
        for child in node['children']:
            update_node_height(child, height + 1)
