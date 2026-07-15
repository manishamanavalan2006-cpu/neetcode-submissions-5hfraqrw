class MyStack:

    def __init__(self):
        self.queues=[]
        

    def push(self, x: int) -> None:
        self.queues.append(x)

    def pop(self) -> int:
        value=self.queues.pop()
        return value

    def top(self) -> int:
        value=self.queues[-1]
        return value
        

    def empty(self) -> bool:
        return not self.queues
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()