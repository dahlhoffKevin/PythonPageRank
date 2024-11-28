from TestSettings import Settings
import unittest
from pagerank import Page, Graph

class A1(unittest.TestCase):
    def setUp(self):
        self.a = Page('a1')
        self.b = Page('b1')

    def test_a1(self):
        self.a.outgoingLinks = [self.b]
        self.a.incomingLinks = [self.b]
        self.b.outgoingLinks = [self.a]
        self.b.incomingLinks = [self.a]

        graph = Graph([self.a, self.b], Settings.d)
        ranks = graph.calculate_pagerank()
        for rank in ranks:
            print(rank[1])

        expected_ranks = [
            [self.a, 1],
            [self.b, 1]
        ]

        self.assertEqual(ranks, expected_ranks)

if __name__ == '__main__':
    print('Running test for testmethod a1')
    unittest.main()