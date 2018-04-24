import unittest
from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assetTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        #d['key'] = 'value'
        #self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d.key, 'value')

if __name__ == '__main__':
    unittest.main()
