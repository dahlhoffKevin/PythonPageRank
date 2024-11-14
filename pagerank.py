class Page():
    def __init__(self, name):
        self.name = name
        self.pagerank = 1
        self.outgoingLinks = []
        self.incomingLinks = []

    def calculateNewPagerank(self, d) -> None:
        pr_sum = 0

        for pin in self.incomingLinks:
            pr_sum += pin.pagerank / len(pin.outgoingLinks)
        self.pagerank = 1 - d + d * pr_sum
        return self.pagerank

class Graph():
    def __init__(self, pages: list[Page], dumpingFactor):
        self.pages = pages
        self.damp = dumpingFactor

    def calculate_pagerank(self) -> list:
        pagerank = []
        for page in self.pages:
            pagerank.append([page, page.calculateNewPagerank(self.damp)])
        return pagerank

def main():
    d = 0.85

    a = Page('A3')
    b = Page('B3')
    c = Page('C3')

    a.outgoingLinks = [b, c]
    a.incomingLinks = [b]
    b.outgoingLinks = [a, c]
    b.incomingLinks = [a]
    c.incomingLinks = [a, b]

    graph = Graph([a, b, c], d)
    pagesAndPagerank = graph.calculate_pagerank()
    for page in pagesAndPagerank:
        print(page[1])

if __name__ == '__main__':
    main()