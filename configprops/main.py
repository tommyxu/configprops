#!/usr/bin/env python3

import os

from termcolor import colored

from dotenv import load_dotenv


class ConfigurationProperties:
    def __init__(self, config_props_prefix: str, debug=True):
        self.config_props_prefix = config_props_prefix
        load_dotenv()
        for key, value in self.__class__.__dict__.items():
            if key.startswith(self.config_props_prefix):
                env_value = os.getenv(key)
                value_text = value
                if env_value != None:
                    if isinstance(value, int):
                        env_value = int(env_value)
                    setattr(self, key, env_value)
                    value_text = colored(
                        env_value, 'red') + '  # default: {}'.format(value)
                if debug:
                    print('{config_key}={config_value}'.format(
                        config_key=key, config_value=value_text))
