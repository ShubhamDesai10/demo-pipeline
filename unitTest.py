import unittest
from requestcheck import responseValidation

class ConfigTestCase(unittest.TestCase):
    def testResponse(self):
        try:
            response = responseValidation()
            self.assertEqual(response, 200)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
