import unittest
import production

class TestProdution(unittest.TestCase):

  def test_remove_duplicates(self):
    input = [1,1,2,2]
    output = [1,2]
    self.assertListEqual(output,production.remove_duplicates(input))


if __name__ == '__main__':
    unittest.main()

class TestSquare(unittest.TestCase):
    def test_return_square(self):
        input = [0,1,2,3,4,5,6,7,8,9,10]
        output = [0,1,4,9,16,25,36,49,64,81,100]
        self.assertListEqual(output,production.return_square(input))
