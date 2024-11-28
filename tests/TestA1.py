from TestSettings import Settings
import unittest
from pagerank import Page, Graph

class A1(unittest.TestCase):
    def setup(self):
        self.a = Page('a1')
        self.a = Page('b1')

    def test_a1(self):
        self.a.outgoingLinks = [self.b]
        self.a.incomingLinks = [self.b]
        self.b.outgoingLinks = [self.a]
        self.b.incomingLinks = [self.a]

        graph = Graph([self.a, self.b], Settings.d)
        ranks = graph.calculate_pagerank()
        for rank in ranks:
            print(rank[1])
        
        self.assertEqual(ranks == [
            [self.a, 1],
            [self.b, 1]
        ])

print('Running test for testmethod a1')
a1 = A1()
a1.test_a1()