class ListNode:
    def __init__(self, key: int, value: int):
        self.key: int = key
        self.value: int = value
        self.next: ListNode = None
        self.prev: ListNode = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.node_map: dict[int, ListNode] = {}

        self.head: ListNode = ListNode(-1, -1)
        self.tail: ListNode = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node = self.node_map[key]
            self.remove(old_node)
        node = ListNode(key, value)
        self.node_map[key] = node
        self.insert(node)

        if len(self.node_map) > self.capacity:
            rem_node = self.head.next
            self.remove(rem_node)

            del self.node_map[rem_node.key]

        
    def insert(self, node: ListNode) -> None:
        end_node: ListNode = self.tail.prev
        end_node.next = node
        node.prev = end_node

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
