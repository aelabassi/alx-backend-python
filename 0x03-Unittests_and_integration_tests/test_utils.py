#!/usr/bin/env python3
""" Unittests for utils """
import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap Class """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map function with exception """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestGetJson Class """
    @parameterized.expand([
        ('http://example.com', {'payload': True}, 'response.json()'),
        ('http://holberton.io', {'payload': False}, 'response.json()'),
    ])
    def test_get_json(self, url, return_value, mock):
        """ Test get_json function """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = return_value
            self.assertEqual(get_json(url), return_value)
            mock_get.assert_called_once()





if __name__ == '__main__':
    unittest.main()
