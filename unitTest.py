import unittest
from requestcheck import responseValidation
import getapi

class ConfigTestCase(unittest.TestCase):
    def testResponse(self):
        response = responseValidation()
        self.assertEqual(response, 200)
       


if __name__ == "__main__":
    unittest.main()
