import unittest
from p1 import lights_on
from p2 import lights_on_individual_brightness


class TestLights(unittest.TestCase):

    def test_p1(self):
        self.assertEqual(lights_on("coding_challenge_input.txt"),
                         998004, "Should be 998004")

    def test_p2(self):
        self.assertEqual(lights_on_individual_brightness(
            "coding_challenge_input.txt"), 1003996, "Should be 1003996.")


if __name__ == '__main__':
    unittest.main()
