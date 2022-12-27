import unittest
from translator import englishToFrench, frenchToEnglish
  
class TestStringMethods(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(englishToFrench('What is your name?'),'Quel est ton nom?')
        self.assertEqual(englishToFrench('How are you?'),'Comment ca va?')
        self.assertEqual(frenchToEnglish('Quel est ton nom?'),'What is your name?')
        self.assertEqual(frenchToEnglish('Comment ca va?'),'How are you?')
        self.assertEqual(englishToFrench(''),'')
        self.assertEqual(frenchToEnglish(''),'')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
  
if __name__ == '__main__':
    unittest.main()

