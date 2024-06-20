"""Base model with camel case configuration.

As python uses snake case for variable names and REST Services
generally expect camel case, this module provides a base class that
converts the variables to camel case upon sending the data to the
respective service.

"""

from pydantic import BaseModel, ConfigDict


def to_camel(string: str) -> str:
    """Convert snake case to camel case.

    Args:
        string (str): To be converted string

    Returns:
        str: String in camel case
    """
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class CamelModel(BaseModel):
    """New base model with camel case configuration."""

    model_config = config
