#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# class SinglyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, node_data):
#         node = SinglyLinkedListNode(node_data)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node


#         self.tail = node

# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))

#         node = node.next

#         if node:
#             fptr.write(sep)

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
        current = head
        while(current.next!=None):
            if current.data==current.next.data:
                current.next=current.next.next
            else:
                current=current.next
        return head

# if __name__ == '__main__':


#     llist_count = 5

#     llist = SinglyLinkedList()
#     mylist = [1,2,2,2,2,2,3]
#     for item in mylist:
#         llist.insert_node(item)

#     llist1 = removeDuplicates(llist.head)

#     while(llist1!=None):
#         print(llist1.data, end=" ")
#         llist1=llist1.next

    
