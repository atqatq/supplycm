"""Simple smart contract validation for supply chain rules."""
from typing import Dict, List


def smart_contract_check(transaction: Dict, rules: List[Dict]) -> Dict:
    """Validate a transaction against supply chain rules.

    Args:
        transaction: Dict with transaction details.
        rules: List of rule dicts with 'field', 'operator', 'value'.

    Returns:
        Dict with 'valid' (bool) and 'violations' (list).

    Example:
        >>> result = smart_contract_check(
        ...     {'temperature': 5, 'humidity': 60},
        ...     [{'field': 'temperature', 'operator': '<=', 'value': 8},
        ...      {'field': 'humidity', 'operator': '>=', 'value': 40}])
        >>> result['valid']
        True
    """
    violations = []
    for rule in rules:
        field = rule['field']
        op = rule['operator']
        value = rule['value']
        actual = transaction.get(field)
        if actual is None:
            violations.append(f'Missing field: {field}')
            continue
        if op == '<=' and not (actual <= value):
            violations.append(f'{field}={actual} exceeds {value}')
        elif op == '>=' and not (actual >= value):
            violations.append(f'{field}={actual} below {value}')
        elif op == '==' and not (actual == value):
            violations.append(f'{field}={actual} not equal to {value}')
        elif op == '<' and not (actual < value):
            violations.append(f'{field}={actual} not less than {value}')
        elif op == '>' and not (actual > value):
            violations.append(f'{field}={actual} not greater than {value}')
    return {'valid': len(violations) == 0, 'violations': violations}
