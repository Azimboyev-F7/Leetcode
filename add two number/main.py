# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy = ListNode(0)  # Yordamchi tugun
        current = dummy  # current pointer
        carry = 0  # Qo‘shimcha raqam (carry)

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # l1 mavjud bo‘lsa, uning qiymati olinadi
            val2 = l2.val if l2 else 0  # l2 mavjud bo‘lsa, uning qiymati olinadi
            total = val1 + val2 + carry  # Jami yig‘indi hisoblanadi
            carry = total // 10  # Agar yig‘indi 10 yoki undan katta bo‘lsa, ko‘tarma (carry) hosil bo‘ladi

            current.next = ListNode(total % 10)  # Natijani yangi tugunga bog‘laymiz
            current = current.next  # current pointer keyingi tugunga o‘tadi

            if l1: l1 = l1.next  # l1 keyingisiga o‘tkaziladi
            if l2: l2 = l2.next  # l2 keyingisiga o‘tkaziladi

        return dummy.next