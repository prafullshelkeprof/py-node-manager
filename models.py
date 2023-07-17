from pydantic import BaseModel
from typing import List, Optional


class Node(BaseModel):
    name: str
    id: str
    nodeHeight: int
    nodeType: str
    parentName: Optional[str]
    parentId: Optional[str]
    children: Optional[List['Node']] = []
    departmentName: Optional[List['str']] = []
    preferredLang: Optional[List['str']] = []


class NewNode(BaseModel):
    name: str
    nodeType: str
    departmentName: Optional[List['str']] = []
    preferredLang: Optional[List['str']] = []


class ChangeParentRequest(BaseModel):
    new_parent_id: str
