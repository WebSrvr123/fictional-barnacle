class Stack(list):
    def push(self,f):
        self.append(f)
    def max(self):
        highest = 0
        for i in self:
            if i > highest:
                highest = i
        return highest
