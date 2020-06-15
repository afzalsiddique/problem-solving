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

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def traverse(head):
    cnt=0
    while(head.next!=None):
        head=head.next
        cnt+=1
    #cnt value will (length of the llist - 1)
    return cnt

def getNode(head, positionFromTail):
    cnt = traverse(head)
    newcnt = cnt - positionFromTail
    node = head
    while newcnt!=0:
        node = node.next
        newcnt-=1
    return node.data

# if __name__ == '__main__':


#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)

#     position = int(input())

#     result = getNode(llist.head, position)
    
#     print(result)
