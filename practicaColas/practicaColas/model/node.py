from .ticket import Ticket

class Node:
    def __init__(self, data: Ticket, priority: int) -> None:
        self.data = data
        self.priority = priority
        self.next = None