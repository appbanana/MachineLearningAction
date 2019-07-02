from com.jqc.trie.trie import Trie
import unittest

if __name__ == '__main__':
    test = unittest.TestCase()

    trie = Trie()
    trie.add('test', 1)
    trie.add('test12', 2)
    trie.add('catalog', 3)
    trie.add('cast', 4)
    trie.add('你大爷', 5)
    
    test.assertTrue(trie.size() == 5)
    test.assertTrue(trie.get('test') == 1)
    test.assertTrue(trie.get('catalog') == 3)
    test.assertTrue(trie.start_with_string('te'))
    test.assertTrue(trie.start_with_string('tes'))
    test.assertTrue(trie.start_with_string('test'))
    test.assertTrue(trie.start_with_string('你'))
    test.assertTrue(trie.start_with_string('你大爷'))
    test.assertTrue(trie.remove('你大爷') == 5)
    test.assertTrue(trie.remove('test') == 1)
    test.assertTrue(trie.remove('tes') != 1)
    test.assertFalse(trie.contains('你大爷'))
    test.assertTrue(trie.size() == 3)



