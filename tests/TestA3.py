from TestSettings import Settings
from pagerank import Page, Graph
import unittest

class A3(unittest.TestCase):
    def setup(self):
        self.a = Page('a')
        self.b = Page('b')
        self.c = Page('c')

    def test_a3(self):
        self.a.outgoingLinks = [self.b, self.c]
        self.a.incomingLinks = [self.b]
        self.b.outgoingLinks = [self.a, self.c]
        self.b.incomingLinks = [self.a]
        self.c.incomingLinks = [self.a, self.b]

        graph = Graph([self.a, self.b, self.c], Settings.d)
        ranks = graph.calculate_pagerank()
        for rank in ranks:
            print(rank[1])
        assert (ranks == [
            [self.a, 0.575],
            [self.b, 0.39437500000000003],
            [self.c, 0.561984375]
        ])

print('Running test for testmethod a3')
a3 = A3()
a3.test_a3()