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

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock):
        """Test that the list of repos is what you expect"""
        payload = [
            {"name": "Google"}, {"name": "Twitter"},
        ]
        mock.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub:
            mock_pub.return_value = "http://test.com"
            test_class = GithubOrgClient("google")
            repos_pub = test_class.public_repos()
            checks = [org["name"] for org in payload]
            self.assertEqual(repos_pub, checks)
            mock_pub.assert_called_once()
            mock.assert_called_once()

        @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ])
        def test_has_license(self, repo, license_key, expected):
            """ unit-test for GithubOrgClient.has_license """
            result = GithubOrgClient.has_license(repo, license_key)
            self.assertEqual(result, expected)
