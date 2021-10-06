import unittest
from requestcheck import responseValidation

class ConfigTestCase(unittest.TestCase):
    def testResponse(self):
        response = responseValidation()
        self.assertTrue(response == 200)


if __name__ == "__main__":
    unittest.main()
