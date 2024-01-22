from DataStructure.LinkedList.Node import Node


class Linked_list:
    def __init__(self):
        self.head=None

    def insertBegin(self,data):
        newNode=Node(data)
        curNode=self.head

        if self.head ==None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while (current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:

                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

