"""Modul conversions."""
import math


def to_degree(radian: float) -> float:
    """
    Args:
        radian(float): radian value to convert to degree

    Returns:
        float: degree value
    """
    return radian * 180.0 / math.pi


def to_radian(degree: float) -> float:
    """
    Args:
        degree(float): degre value to convert to radian

    Returns:
        float: radian value
    """
    return degree * math.pi / 180.0
