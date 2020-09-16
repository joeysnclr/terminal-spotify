import math
from Component import Component


class TextLines(Component):

    def __init__(self, name, lines):
        super().__init__(name)
        self.addShortcut("n", self.nextPage)
        self.addShortcut("N", self.prevPage)
        self.lines = lines
        self.currLines = []
        self.currPage = 1

    def initPaging(self, lines):
        self.perPage = lines
        self.pages = math.ceil(len(self.lines) / self.perPage)
        if self.currPage > self.pages or self.currPage < 1:
            self.currPage = 1
        startIndex = (self.currPage - 1) * self.perPage
        endIndex = self.currPage * self.perPage
        currLines = self.lines[startIndex:endIndex]
        self.currLines = currLines

    def output(self, lines):
        self.initPaging(lines)
        outputLines = self.currLines
        while len(outputLines) < lines:
            outputLines.append("")
        return outputLines

    def changePage(self, n):
        nextPage = self.currPage + n
        if nextPage < 1 or nextPage > self.pages:
            return
        self.currPage = nextPage

    def nextPage(self):
        self.changePage(1)

    def prevPage(self):
        self.changePage(-1)

