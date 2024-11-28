from TestSettings import Settings
from pagerank import Page, Graph
import unittest

class A4(unittest.TestCase):
    def setup(self):
        self.a = Page('a')
        self.b = Page('b')
        self.c = Page('c')

    def test_a4(self):
        self.a.outgoingLinks = [self.b]
        self.b.incomingLinks = [self.a]
        self.b.outgoingLinks = [self.c]
        self.c.incomingLinks = [self.b]

        graph = Graph([self.a, self.b, self.c], Settings.d)
        ranks = graph.calculate_pagerank()
        for rank in ranks:
            print(rank[1])
        assert (ranks == [
            [self.a, 0.15000000000000002],
            [self.b, 0.2775],
            [self.c, 0.385875]
        ])

print('Running test for testmethod a4')
a4 = A4()
a4.test_a4()