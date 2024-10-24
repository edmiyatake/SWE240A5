class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):

        if self.root == None:
            self.root = Node(val)
            return

        currNode = self.root
        while currNode:
            if currNode.data > val:
                # if currNode is empty, insert into left
                if not currNode.left:
                    currNode.left = Node(val)
                    return
                else:
                    currNode = currNode.left
            else:
                if not currNode.right:
                    currNode.right = Node(val)
                    return
                else:
                    currNode = currNode.right
    
    def printTree(self,node, level=0):
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.data))
            self.printTree(node.right, level + 1)

class heapBuilder:
    def __init__(self,list1):
        self.list1 = list1
        self.root = None
    
    def createMinHeap(self,list1):
        self.minHeapify()
        return self.root

    def createMinHeap(self):
        self.heapSortMin()
        newBST = BST()
        for num in self.list1:
            newBST.insert(num)
        return newBST.root
    
    def createMaxHeap(self):
        self.heapSortMax()
        newBST = BST()
        for num in self.list1:
            newBST.insert(num)
        return newBST.root

    def heapSortMin(self):
        n = len(self.list1)
        for i in range(n//2 - 1, -1 , -1):
            self.minHeapify(self.list1, n, i)
        for i in range(n-1,0,-1):
            self.list1[i], self.list1[0] = self.list1[0],self.list1[i]
            self.minHeapify(self.list1,i,0)
        return self.list1
    
    def heapSortMax(self):
        n = len(self.list1)
        for i in range(n//2 - 1, -1 , -1):
            self.maxHeapify(self.list1, n, i)
        for i in range(n-1,0,-1):
            self.list1[i], self.list1[0] = self.list1[0],self.list1[i]
            self.maxHeapify(self.list1,i,0)
        return self.list1
    
    def minHeapify(self,list1,n,i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and list1[left] < list1[smallest]:
            smallest = left
        if right < n and list1[right] < list1[smallest]:
            smallest = right
        if smallest != i:
            list1[i], list1[smallest] = list1[smallest],list1[i]
            self.minHeapify(list1, n, smallest)
    
    def maxHeapify(self,list1,n,i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and list1[left] > list1[largest]:
            largest = left
        if right < n and list1[right] > list1[largest]:
            largest = right
        if largest != i:
            list1[i], list1[largest] = list1[largest],list1[i]
            self.maxHeapify(list1, n, largest)


test1 = [1,23,12,54,43,32,18,79]
# newBST = BST()
# for num in test1:
#     newBST.insert(num)
# newBST.printTree(newBST.root)

newHeap = heapBuilder(test1)
print(newHeap.createMinHeap())
# print(newHeap.heapSortMin())
# print(newHeap.list1)
# newHeap.heapSortMax()
# print(newHeap.createMaxHeap())

