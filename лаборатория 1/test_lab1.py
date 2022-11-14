import unittest
import Lab1

class testkvadratik(unittest.TestCase):
    def test_kubick(self):
        self.assertEqual(Lab1.cubick("001"), 2)
        self.assertEqual(Lab1.cubick("100100"), 0)
        self.assertEqual(Lab1.cubick("001001"), 2)

        
        
        if __name__ == '__main__':
            unittest.main()
