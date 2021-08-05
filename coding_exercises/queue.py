class Queue:

    def __init__(self):
        self.l = []

    def push(self,num):
        self.l.append(num)

    def pop(self):
        num = self.l[0]
        self.l = self.l[1:]
        return num

    def print(self):
        for x in range(len(self.l)):
            print(self.l[x])
        

q = Queue()
q.push(4)
q.push(5)
q.push(6)
q.push(8)
q.push(9)
q.print()
print(" ",q.pop())
print(" ",q.pop())
q.print()


