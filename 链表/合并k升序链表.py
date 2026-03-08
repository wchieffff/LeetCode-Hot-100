from typing import List, Optional

class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
class solution:
    def mergeklist(self,listnodes):
        if not listnodes:
            return None
        
        return self.solve(listnodes,0,len(listnodes) - 1)
    def solve(self,listns,left,right):
        if left == right:
            return listns[left]
        
        mid = (left + right) // 2
        l1 = self.solve(listns,left,mid)
        l2 = self.solve(listns,mid + 1,right)

        return self.merge2list(l1,l2)
    def merge2list(self,list1,list2):
        dummy = temp = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 if list1 else list2

        return dummy.next
def creat_list(arr):
    l = len(arr)
    tp = head = ListNode(0)
    for i in range(l):
        tp.next = ListNode(arr[i])
        tp = tp.next
    return head.next
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

if __name__ == "__main__":
    a1,a2,a3 = ([1,3,6],[2,5,7],[33,56,88])
    sol = solution()
    p1 =  creat_list(a1)
    p2 =  creat_list(a2)
    p3 =  creat_list(a3)
    list = [p1,p2,p3]
    head = sol.mergeklist(list)

    print_list(head)