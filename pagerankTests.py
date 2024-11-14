from pagerank import Page, Graph

d = 0.85

def a1():
    a = Page('a1')
    b = Page('b1')

    a.outgoingLinks = [b]
    a.incomingLinks = [b]
    b.outgoingLinks = [a]
    b.incomingLinks = [a]

    graph = Graph([a, b], d)
    pagesAndPagerank = graph.calculate_pagerank()
    for page in pagesAndPagerank:
        print(page[1])

print('Tests for a1')
a1()


def a2():
    a = Page('a')
    b = Page('b')
    c = Page('c')

    a.outgoingLinks = [c]
    a.incomingLinks = [b]
    b.outgoingLinks = [a]
    b.incomingLinks = [c]
    c.outgoingLinks = [b]
    c.incomingLinks = [a]

    graph = Graph([a, b, c], d)
    pagesAndPagerank = graph.calculate_pagerank()
    for page in pagesAndPagerank:
        print(page[1])

print('Tests for a2')
a2()

def a3():
    a = Page('a')
    b = Page('b')
    c = Page('c')

    a.outgoingLinks = [b, c]
    a.incomingLinks = [b]
    b.outgoingLinks = [a, c]
    b.incomingLinks = [a]
    c.incomingLinks = [a, b]

    graph = Graph([a, b, c], d)
    pagesAndPagerank = graph.calculate_pagerank()
    for page in pagesAndPagerank:
        print(page[1])

print('Tests for a3')
a3()

def a4():
    a = Page('a')
    b = Page('b')
    c = Page('c')

    a.outgoingLinks = [b]
    b.incomingLinks = [a]
    b.outgoingLinks = [c]
    c.incomingLinks = [b]

    graph = Graph([a, b, c], d)
    pagesAndPagerank = graph.calculate_pagerank()
    for page in pagesAndPagerank:
        print(page[1])

print('Tests for a4')
a4()