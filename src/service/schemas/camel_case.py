"""Base model with camel case configuration."""

from pydantic import BaseModel, ConfigDict


def to_camel(string: str) -> str:
    """Convert snake case to camel case.

    Args:
        string: To be converted string

    Returns:
    -------
        String in camel case
    """
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class CamelModel(BaseModel):
    """New base model with camel case configuration."""

    model_config = config
