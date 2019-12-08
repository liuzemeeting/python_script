# 继承 逻辑门与门电路


class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLable(self):
        return self.label

    def getoutput(self):
        return self.output