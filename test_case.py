import unittest
import practice


class MyTestCase(unittest.TestCase):
    def test_check_straight_low(self):
        self.assertEqual(practice.check_straight("S2", "S3", "S4"), 4)

    def test_check_straight_high(self):
        self.assertEqual(practice.check_straight("S7", "S8", "S9"), 9)

    def test_check_straight_zero(self):
        self.assertEqual(practice.check_straight("S7", "S8", "S2"), 0)


    def test_check_3ofa_kind(self):
        self.assertEqual(practice.check_3ofa_kind("S7", "S7", "S7"), 7)

    def test_check_3ofa_kind_Ace(self):
        self.assertEqual(practice.check_3ofa_kind("SA", "SA", "SA"), 14)
    def test_check_3ofa_kind_zero(self):
        self.assertEqual(practice.check_3ofa_kind("SA", "SA", "S3"), 0)

    def test_check_royal_flush(self):
        self.assertEqual(practice.check_royal_flush("S10", "SJ", "SQ"), 12)

    def test_check_royal_flush2(self):
        self.assertEqual(practice.check_royal_flush("SQ", "SK", "SA"), 14)

    def test_play_cards(self):
        self.assertEqual(practice.play_cards("S3", "S5", "S6", "S7", "S8", "S9"), 1)

if __name__ == '__main__':
    unittest.main()
