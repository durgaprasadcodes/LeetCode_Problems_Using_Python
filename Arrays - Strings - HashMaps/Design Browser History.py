class History:
    def __init__(self,val):
        self.val = val
        self.prev = []
        self.next = []
class BrowserHistory:

    def __init__(self, homepage: str):
        self.tab = History(homepage)

    def visit(self, url: str) -> None:
        self.tab.prev.append(self.tab.val)
        self.tab.val = url
        self.tab.next = []
    def back(self, steps: int) -> str:
        while self.tab.prev and steps:
            self.tab.next.append(self.tab.val)
            self.tab.val = self.tab.prev.pop()
            steps-=1
        return self.tab.val
    def forward(self, steps: int) -> str:
        while self.tab.next and steps:
            self.tab.prev.append(self.tab.val)
            self.tab.val = self.tab.next.pop()
            steps-=1
        return self.tab.val