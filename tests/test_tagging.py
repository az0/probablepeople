from probablepeople import tag
import unittest

class TestTagging(unittest.TestCase) :

    def test_basic(self) :
        name_type, tagged = tag("Bob Belcher")
        assert name_type == 'Person'
        self.assertEqual("Bob", tagged['GivenName'])
        self.assertEqual("Belcher", tagged['Surname'])
    
