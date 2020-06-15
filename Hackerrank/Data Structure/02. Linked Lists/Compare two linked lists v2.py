#!/bin/python3

# import os
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



# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(head1, head2):
    
    if head1==None and head2==None:
        return 1
    elif head1!=None and head2!=None:
        while head1.data==head2.data:
            if head1.next!=None and head2.next!=None:
                head1=head1.next
                head2=head2.next
            else:
                break
        if head1.next==None and head2.next==None:#last elements checking
            if head1.data==head2.data:#l1:{1,2,3} l2:{1,2,3} (3,3) are being checked
                return 1
            else:#l1:{1,2,3} l2:{1,2,4} (3,4) are being checked
                return 0
        else:#non-last elements checking and lists with uneven lengths checking
        #l1:{1,2,3,4,5} l2:{1,2,8,4} (3,8) are being checked
        #l1:{1,2} l2:{1} (2,None) are being checked
            return 0
    else: #one of the lists is empty
        return 0

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     tests = int(input())

#     for tests_itr in range(tests):
#         llist1_count = int(input())

#         llist1 = SinglyLinkedList()

#         for _ in range(llist1_count):
#             llist1_item = int(input())
#             llist1.insert_node(llist1_item)
            
#         llist2_count = int(input())

#         llist2 = SinglyLinkedList()

#         for _ in range(llist2_count):
#             llist2_item = int(input())
#             llist2.insert_node(llist2_item)

#         result = compare_lists(llist1.head, llist2.head)

#         fptr.write(str(int(result)) + '\n')

#     fptr.close()
