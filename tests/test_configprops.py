#!/usr/bin/env python3

from configprops import ConfigurationProperties
import os


class AppTestConfig(ConfigurationProperties):
    TEST_APP_CONFIG_KEY_TEXT = "Original"
    TEST_APP_CONFIG_KEY_BOOL = True
    TEST_APP_CONFIG_KEY_INT = 32
    TEST_APP_CONFIG_KEY_FLOAT = 3.3
    TEST_APP_CONFIG_KEY_OTHER = 55
    TEST_APP_CONFIG_KEY_EMPTY_TEXT = ""


def test_override():
    os.environ["TEST_APP_CONFIG_KEY_BOOL"] = "0"
    os.environ["TEST_APP_CONFIG_KEY_FLOAT"] = "8.5"
    os.environ["TEST_APP_CONFIG_KEY_INT"] = "185"

    config = AppTestConfig("TEST_APP_CONFIG_", debug=True)
    assert config.TEST_APP_CONFIG_KEY_BOOL == False
    assert config.TEST_APP_CONFIG_KEY_OTHER == 55
    assert config.TEST_APP_CONFIG_KEY_FLOAT == 8.5
    assert config.TEST_APP_CONFIG_KEY_INT == 185

    #  pytest -vs
