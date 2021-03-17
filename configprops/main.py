#!/usr/bin/env python3

import os
from typing import Any, List, Tuple
from collections import namedtuple
from prettytable import PrettyTable
from dotenv import load_dotenv

Prop = namedtuple("Prop", ["name", "value", "default_value", "overridden"])


class ConfigurationProperties:
    def __init__(self, config_props_prefix: str, dot_env=False, *, debug=False):
        if dot_env:
            load_dotenv(verbose=debug)

        self.config_props_prefix = config_props_prefix
        self.config_props: List[Prop] = []

        for key, old_value in self.__class__.__dict__.items():
            if key.startswith(self.config_props_prefix):
                env_value = os.getenv(key)
                if env_value is not None:
                    new_value: Any = None
                    new_value_string = str(env_value)
                    if type(old_value) == bool:
                        new_value = new_value_string.strip().lower() not in [
                            "false",
                            "0",
                            "",
                        ]
                    elif isinstance(old_value, int):
                        new_value = int(new_value_string)
                    elif isinstance(old_value, float):
                        new_value = float(new_value_string)
                    else:
                        new_value = new_value_string
                    setattr(self, key, new_value)

                    self.config_props.append(
                        Prop(key, new_value, old_value, True)
                    )  # type: ignore
                else:
                    self.config_props.append(
                        Prop(key, old_value, old_value, False)
                    )  # type: ignore

    def get_config_summary(self) -> PrettyTable:
        pt = PrettyTable()
        pt.field_names = ["<*>", "Key", "Value", "Default"]
        pt.align["Key"] = "l"
        for prop in self.config_props:
            pt.add_row(
                [
                    "*" if prop.overridden else "",
                    prop.name,
                    prop.value,
                    prop.default_value,
                ]
            )
        return pt
