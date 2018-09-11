class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
        return self
    def removeNode(self, value):
        runner = self.head
        while(runner.next != None):
            print(runner.value)
            if (runner..next.value == value):
                runner = runner.next
            runner = runner.next
        return self
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
      
print("\n\n\n\n================== START OF THE PROGRAM ================")       
list = SList(5).addNode(7).addNode(9).addNode(1)
list = list.removeNode(7)
list.printAllValues("Attempt 1")

