"""Verify integrity of a hash chain."""
import hashlib
from typing import List, Dict


def verify_chain(records: List[Dict], hashes: List[str]) -> bool:
    """Verify that a hash chain is valid (not tampered with).

    Args:
        records: Original event records.
        hashes: Hash chain to verify.

    Returns:
        True if chain is valid, False otherwise.

    Example:
        >>> from supplycm.blockchain.hash_chain import hash_chain
        >>> records = [{'event': 'created'}, {'event': 'shipped'}]
        >>> hashes = hash_chain(records)
        >>> verify_chain(records, hashes)
        True
    """
    if len(records) != len(hashes):
        return False
    prev_hash = '0' * 64
    for record, expected_hash in zip(records, hashes):
        record_str = str(sorted(record.items())) + prev_hash
        actual_hash = hashlib.sha256(record_str.encode()).hexdigest()
        if actual_hash != expected_hash:
            return False
        prev_hash = expected_hash
    return True
