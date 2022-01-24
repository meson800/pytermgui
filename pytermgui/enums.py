"""
This module provides commonly used enumerations for the library.
It also has a class implementing Enum-s with default values. All Enums
below subclass it, meaning you can use their `get_default()` methods to get
the globally set default value.

To modify defaults, use the `defaults` dictionary.
"""

# This file is an absolute mess to mypy-correctly type.
# It is still typed well enough for a human to read, but
# I could not make mypy accept it without making the code
# horrible to read and edit.
#
# mypy: ignore-errors

from __future__ import annotations

from typing import Type
from enum import IntEnum, auto as _auto

defaults: dict[IntEnum, Type[IntEnum]] = {}

__all__ = [
    "SizePolicy",
    "CenteringPolicy",
    "SizePolicy",
    "HorizontalAlignment",
    "VerticalAlignment",
]


class DefaultEnum(IntEnum):
    """An Enum class that can return its default value"""

    @classmethod
    def get_default(cls) -> IntEnum | None:
        """Get default value"""

        return defaults.get(cls)


class SizePolicy(DefaultEnum):
    """Values according to which Widget sizes are assigned"""

    FILL = _auto()
    """Inner widget will take up as much width as possible"""

    STATIC = _auto()
    """Inner widget will take up an exact amount of width"""

    RELATIVE = _auto()  # TODO: Implement this
    """Not implemented: Inner widget will take up a percentage of the available width"""


class CenteringPolicy(DefaultEnum):
    """Policies to center `Container` according to"""

    ALL = _auto()
    VERTICAL = _auto()
    HORIZONTAL = _auto()


class HorizontalAlignment(DefaultEnum):
    """Policies to align widgets by.

    These are applied by the parent object, and are
    relative to them."""

    LEFT = 0
    """Align widget to the left edge"""

    CENTER = 1
    """Center widget in the available width"""

    RIGHT = 2
    """Align widget to the right edge"""


class VerticalAlignment(DefaultEnum):
    """Vertical alignment options for widgets."""

    TOP = 0
    """Align widgets to the top"""

    CENTER = 1
    """Align widgets in the center, with equal* padding on the top and bottom

    Note: When the available height is not divisible by 2, the extra line of padding
    is added to the bottom."""

    BOTTOM = 2
    """Align widgets to the bottom"""


class Overflow(DefaultEnum):
    """Overflow policies implemented by Container."""

    HIDE = _auto()
    """Stop gathering lines once there is no room left"""

    SCROLL = _auto()
    """Allow scrolling when there is too many lines"""

    RESIZE = _auto()
    """Resize parent to fit with the new lines"""


defaults[SizePolicy] = SizePolicy.FILL
defaults[CenteringPolicy] = CenteringPolicy.ALL
defaults[HorizontalAlignment] = HorizontalAlignment.CENTER
defaults[VerticalAlignment] = VerticalAlignment.CENTER
defaults[Overflow] = Overflow.SCROLL
