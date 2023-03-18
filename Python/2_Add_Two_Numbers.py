class Solution:
	# Function to reverse a list
	def reverse(self, head):
		if head is None or head.next is None:
			return head
		prev = None
		next = None
		curr = head
		while curr is not None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		head = prev
		return head

	# Function to add two numbers represented by linked list.

	def addTwoNumbers(self, first, second):

		# reverse the two lists
		curr1 = self.reverse(first)
		curr2 = self.reverse(second)

		# res is head node of the resultant list
		sum = 0
		carry = 0
		res = None
		prev = None

		# while both lists have atleast one node
		while curr1 is not None or curr2 is not None:

			# Calculating the sum of the last digits
			sum = carry + (curr1.data if curr1 else 0) + \
				(curr2.data if curr2 else 0)

			# update carry for next calculation
			carry = (1 if sum >= 10 else 0)

			# update sum if it is greater than 10
			sum = sum % 10

			# Create a new node with sum as data
			temp = Node(sum)

			# if this is the first node then set it as head of the resultant list
			if res is None:
				res = temp

			# If this is not the first node then connect it to the rest.
			else:
				prev.next = temp

			# Set prev for next insertion
			prev = temp

			# Move first and second pointers to next nodes
			if curr1:
				curr1 = curr1.next
			if curr2:
				curr2 = curr2.next

		# if carry from previous sums is remaining
		if carry > 0:
			temp.next = Node(carry)

		# Reverse the resultant answer
		ans = self.reverse(res)
		return ans


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, val):
		if self.head is None:
			self.head = Node(val)
			self.tail = self.head
		else:
			self.tail.next = Node(val)
			self.tail = self.tail.next

# Utility function to print the list


def printList(n):
	while n:
		print(n.data, end = ' ')
		n = n.next
	print()


# Driver Code
if __name__ == "__main__":

	arr1 = []
	LL1 = LinkedList()
	for i in arr1:
		LL1.insert(i)
	print("First list is", end = " ")
	printList(LL1.head)

	arr2 = [5,6]
	LL2 = LinkedList()
	for i in arr2:
		LL2.insert(i)
	print("Second list is", end = " ")
	printList(LL2.head)

	# Function Call
	res = Solution().addTwoNumbers(LL1.head, LL2.head)
	print("Resultant list is", end = " ")
	printList(res)











# class Solution(object):
#     def findMiddle(self, input_list):
#         middle = float(len(input_list))/2
#         if middle % 2 != 0:
#             return input_list[int(middle - .5)]
#         else:
#             return (input_list[int(middle)], input_list[int(middle-1)])
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         sorted_list = sorted(nums1 + nums2)
#         print(sorted_list)
#         # meadian formula (n+1)/2
#         mid = len(sorted_list)/2
#         middle_values = self.findMiddle(sorted_list)
#         if type(middle_values) == int:
#             return middle_values
#         else:
#             sum_tuple = list(middle_values)
#             return sum(sum_tuple)/2
        