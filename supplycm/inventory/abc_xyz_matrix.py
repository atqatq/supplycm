"""Combined ABC-XYZ classification."""
from typing import List, Tuple


def abc_xyz_matrix(abc_classes: List[Tuple[str, str]],
                   xyz_classes: List[Tuple[str, str]]) -> List[Tuple[str, str, str]]:
    """Combine ABC and XYZ classifications into 9 categories (AX, AY, AZ, BX, ...).

    Example:
        >>> abc_xyz_matrix([('a','A'),('b','B')], [('a','X'),('b','Y')])
        [('a', 'A', 'X', 'AX'), ('b', 'B', 'Y', 'BY')]
    """
    abc_dict = dict(abc_classes)
    xyz_dict = dict(xyz_classes)
    items = set(abc_dict) | set(xyz_dict)
    result = []
    for item in items:
        abc = abc_dict.get(item, 'C')
        xyz = xyz_dict.get(item, 'Z')
        result.append((item, abc, xyz, abc + xyz))
    return sorted(result)
