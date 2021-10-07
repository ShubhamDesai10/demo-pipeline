import unittest
from requestcheck import responseValidation
import getapi

class ConfigTestCase(unittest.TestCase):
    def testResponse(self):
        try:
            response = responseValidation()
            self.assertEqual(response, 200)
        except Exception as e:
            print("Test didn't pass!")
            getapi.deleteApi()
            print("Stack Deleted")
            exit(1)
       


if __name__ == "__main__":
    unittest.main()
