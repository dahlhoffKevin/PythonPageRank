from TestSettings import Settings
from pagerank import Page, Graph
import unittest

class A2(unittest.TestCase):
    def setUp(self):
        self.a = Page('a')
        self.b = Page('b')
        self.c = Page('c')

    def test_a2(self):
        self.a.outgoingLinks = [self.c]
        self.a.incomingLinks = [self.b]
        self.b.outgoingLinks = [self.a]
        self.b.incomingLinks = [self.c]
        self.c.outgoingLinks = [self.b]
        self.c.incomingLinks = [self.a]

        graph = Graph([self.a, self.b, self.c], Settings.d)
        ranks = graph.calculate_pagerank()
        for rank in ranks:
            print(rank[1])

        expected_ranks = [
            [self.a, 1],
            [self.b, 1],
            [self.c, 1]
        ]

        self.assertEqual(ranks, expected_ranks)

if __name__ == '__main__':
    print('Running test for testmethod a2')
    unittest.main()