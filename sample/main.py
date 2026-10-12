import sys
from unittest import TestCase
 
class Evaluate(TestCase):
    def test_debugging(self):
        import main  # Imports and runs student's solution
        output = sys.stdout.getvalue()  # Returns output since this function started
        self.assertEqual("Notes from Day 1\nThe print statement is used to output strings\nStrings are strings of characters\nString Concatenation is done with the + sign\nNew lines can be created with a \ and the letter n\n", output, "Make sure you are printing out all 5 lines.")