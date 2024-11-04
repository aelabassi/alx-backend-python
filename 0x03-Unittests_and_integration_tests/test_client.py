#!/usr/bin/env python3
""" Unittests for client """
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient Class """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos(self):
        """Test that the list of repos is what you expect"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {
                "repos_url": "http://test.com",
            }
            mock.return_value = payload
            test_class = GithubOrgClient("google")
            repos_pub = test_class._public_repos_url
            self.assertEqual(repos_pub, payload["repos_url"])
