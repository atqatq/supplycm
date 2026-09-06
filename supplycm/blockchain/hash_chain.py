"""Simple hash chain for supply chain traceability."""
import hashlib
from typing import List, Dict


def hash_chain(records: List[Dict]) -> List[str]:
    """Create a hash chain linking supply chain events.

    Each record hash includes the previous hash, creating an
    immutable chain. Tampering with any record breaks the chain.

    Args:
        records: List of event dicts (e.g., timestamp, location, product).

    Returns:
        List of hash strings, one per record.

    Example:
        >>> hashes = hash_chain([
        ...     {'event': 'manufactured', 'product': 'A'},
        ...     {'event': 'shipped', 'product': 'A'},
        ...     {'event': 'delivered', 'product': 'A'},
        ... ])
        >>> len(hashes) == 3
        True
    """
    hashes = []
    prev_hash = '0' * 64  # Genesis block
    for record in records:
        # Sort keys for deterministic hashing
        record_str = str(sorted(record.items())) + prev_hash
        current_hash = hashlib.sha256(record_str.encode()).hexdigest()
        hashes.append(current_hash)
        prev_hash = current_hash
    return hashes
