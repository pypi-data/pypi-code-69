import unittest

from numpy import testing

from reinvent_chemistry import Similarity, Conversions
from unittest_reinvent.chemistry.fixtures import aspirin, celecoxib


class Test_similarity(unittest.TestCase):

    def setUp(self):
        self.similarity = Similarity()
        self.chemistry = Conversions()
        self.aspirin_fp = self.chemistry.smiles_to_fingerprints([aspirin])
        self.celecoxib_fp = self.chemistry.smiles_to_fingerprints([celecoxib])

    def test_calculate_tanimoto(self):
        score = self.similarity.calculate_tanimoto(self.celecoxib_fp, self.aspirin_fp)

        testing.assert_almost_equal(score, 0.1455, 3)

    def test_calculate_jaccard_distance(self):
        score = self.similarity.calculate_jaccard_distance(self.celecoxib_fp, self.aspirin_fp)

        testing.assert_almost_equal(score, 0.8545, 3)
