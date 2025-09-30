"""Combine ABC value with XYZ variability classification."""
from typing import List, Tuple


def demand_class_abc_xyz(abc: List[Tuple[str, str]],
                          xyz: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """Combine into 9-class matrix (AX, AY, AZ, BX, ...).

    Example:
        >>> result = demand_class_abc_xyz([('a', 'A'), ('b', 'B')],
        ...                               [('a', 'X'), ('b', 'Y')])
        >>> result[0] == ('a', 'AX')
        True
    """
    abc_dict = dict(abc)
    xyz_dict = dict(xyz)
    result = []
    for item in sorted(set(abc_dict) | set(xyz_dict)):
        result.append((item, abc_dict.get(item, 'C') + xyz_dict.get(item, 'Z')))
    return result
