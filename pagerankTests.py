from pagerank import Page, Graph

d = 0.85

def test_a1():
    a = Page('a1')
    b = Page('b1')

    a.outgoingLinks = [b]
    a.incomingLinks = [b]
    b.outgoingLinks = [a]
    b.incomingLinks = [a]

    graph = Graph([a, b], d)
    ranks = graph.calculate_pagerank()
    for rank in ranks:
        print(rank[1])
    assert (ranks == [
        [a, 1],
        [b, 1]
    ])

print('Running test for testmethod a1')
test_a1()


def test_a2():
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
    ranks = graph.calculate_pagerank()
    for rank in ranks:
        print(rank[1])
    assert (ranks == [
        [a, 1],
        [b, 1],
        [c, 1]
    ])

print('Running test for testmethod a2')
test_a2()

def test_a3():
    a = Page('a')
    b = Page('b')
    c = Page('c')

    a.outgoingLinks = [b, c]
    a.incomingLinks = [b]
    b.outgoingLinks = [a, c]
    b.incomingLinks = [a]
    c.incomingLinks = [a, b]

    graph = Graph([a, b, c], d)
    ranks = graph.calculate_pagerank()
    for rank in ranks:
        print(rank[1])
    assert (ranks == [
        [a, 0.575],
        [b, 0.39437500000000003],
        [c, 0.561984375]
    ])

print('Running test for testmethod a3')
test_a3()

def test_a4():
    a = Page('a')
    b = Page('b')
    c = Page('c')

    a.outgoingLinks = [b]
    b.incomingLinks = [a]
    b.outgoingLinks = [c]
    c.incomingLinks = [b]

    graph = Graph([a, b, c], d)
    ranks = graph.calculate_pagerank()
    for rank in ranks:
        print(rank[1])
    assert (ranks == [
        [a, 0.15000000000000002],
        [b, 0.2775],
        [c, 0.385875]
    ])

print('Running test for testmethod a4')
test_a4()