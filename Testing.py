
import unittest
import script

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script.run_guess(answer,guess)
        self.assertTrue()
        pass
 
    unittest.main()