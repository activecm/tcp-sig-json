#
# Unit Test Validate TCP Signature json file before pull request.
#

# Imports
import json
import unittest


class TestTcpJsonFile(unittest.TestCase):

    def test_validateDict(self):
        '''Validate JSON data is accessible.'''
        jsonFile = open('tcp-sig.json')
        tcp_sig = json.load(jsonFile)
        self.assertIs(type(tcp_sig), dict)

    def test_validateKeys(self):
        '''Validate JSON data is accessible.'''
        jsonFile = open('tcp-sig.json')
        tcp_sig = json.load(jsonFile)
        json_keys = list(tcp_sig['signature_list'][0].keys())
        self.assertEqual(sorted(json_keys), sorted(['acid', 'platform', 'tcp_flag', 'tcp_sig', 'comments']))

    def test_validateACID(self):
        '''Validate every ACID key is unique.'''
        jsonFile = open('tcp-sig.json')
        tcp_sig = json.load(jsonFile)
        acid_list = [sig['acid'] for sig in tcp_sig['signature_list']]
        self.assertTrue(len(acid_list) == len(set(acid_list)))




if __name__ == "__main__":
    unittest.main()