# configprops

## Introduction

This package provides a configuration base class to be extended with list of KEYS (same prefix) that could be overridden by environment variables."

## Examples

```python
#!/usr/bin/env python3

from configprops import ConfigurationProperties
import os


class AppTestConfig(ConfigurationProperties):
    TEST_APP_CONFIG_KEY_TEXT = 'Original'
    TEST_APP_CONFIG_KEY_BOOL = True
    TEST_APP_CONFIG_KEY_INT = 32
    TEST_APP_CONFIG_KEY_FLOAT = 3.3
    TEST_APP_CONFIG_KEY_OTHER = 55


def test_override():
    os.environ['TEST_APP_CONFIG_KEY_BOOL'] = '0'
    os.environ['TEST_APP_CONFIG_KEY_FLOAT'] = '8.5'
    os.environ['TEST_APP_CONFIG_KEY_INT'] = '185'

    config = AppTestConfig('TEST_APP_CONFIG_')

    assert config.TEST_APP_CONFIG_KEY_BOOL == False
    assert config.TEST_APP_CONFIG_KEY_OTHER == 55
    assert config.TEST_APP_CONFIG_KEY_FLOAT == 8.5
    assert config.TEST_APP_CONFIG_KEY_INT == 185

```
