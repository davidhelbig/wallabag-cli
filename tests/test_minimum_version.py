from src.wallabag import api

from unittest.mock import Mock

response = Mock(spec=api.Response)

def test_version_major():
    api.MINIMUM_API_VERSION_HR = "3.3.0"
    response.response = '"2.0.0"'
    assert not api.is_minimum_version(response)

def test_version_minor():
    api.MINIMUM_API_VERSION_HR = "2.3.0"
    response.response = '"2.1.0"'
    assert not api.is_minimum_version(response)

def test_version_patch():
    api.MINIMUM_API_VERSION_HR = "2.3.1"
    response.response = '"2.3.0"'
    assert not api.is_minimum_version(response)

def test_version_dev():
    api.MINIMUM_API_VERSION_HR = "2.3.1"
    response.response = '"2.3.1-dev"'
    assert not api.is_minimum_version(response)