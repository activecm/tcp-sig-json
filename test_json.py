#
# Unit Test Validate TCP Signature json file before pull request.
#

# Imports
import json
import unittest




class TestTcpJsonFile(unittest.TestCase):

    def validateDict(self):
        '''Validate JSON data is accessible.'''
        try:
            jsonFile = open('tcp-sig.json')
            tcp_sig = json.load(jsonFile)
            self.assertIs(type(tcp_sig), dict)
        except ValueError as err:
            return False

    def validateKeys(self):
        '''Validate JSON data is accessible.'''
        try:
            jsonFile = open('tcp-sig.json')
            tcp_sig = json.load(jsonFile)
            json_keys = list(['signature_list'][0].keys())
            self.assertEqual(json_keys, ['acid', 'platform', 'tcp_flag', 'tcp_sig', 'comments'])
        except ValueError as err:
            return False



if __name__ == "__main__":
    unittest.main()