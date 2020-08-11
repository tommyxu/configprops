#!/usr/bin/env python3

import os
from termcolor import colored
from typing import Any


class ConfigurationProperties:
    def __init__(self, config_props_prefix: str, debug=False):
        self.config_props_prefix = config_props_prefix
        for key, value in self.__class__.__dict__.items():
            if key.startswith(self.config_props_prefix):
                env_value = os.getenv(key)
                if env_value is not None:
                    new_value: Any = None
                    new_value_string = str(env_value)
                    if type(value) == bool:
                        new_value = new_value_string.strip().lower() not in [
                            'false',
                            '0',
                            '',
                        ]
                    elif isinstance(value, int):
                        new_value = int(new_value_string)
                    elif isinstance(value, float):
                        new_value = float(new_value_string)
                    else:
                        new_value = new_value_string
                    setattr(self, key, new_value)

                if env_value is not None and debug:
                    value_text = colored(new_value,
                                         'red') + f'  # default: {value}'
                    print('{config_key}={config_value}'.format(
                        config_key=key, config_value=value_text))
