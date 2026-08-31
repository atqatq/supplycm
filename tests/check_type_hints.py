"""Check that all public functions have type hints.

Verifies that every public function in the supplycm package has
type annotations for parameters and return values.

Usage:
    python tests/check_type_hints.py
"""
import ast
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def check_module(filepath):
    """Check a single Python file for type hints."""
    source = filepath.read_text()
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    issues = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Skip private functions
            if node.name.startswith('_'):
                continue
            # Check return annotation
            if node.returns is None:
                issues.append(f"{filepath.name}:{node.lineno}: {node.name}() missing return type hint")
            # Check argument annotations
            for arg in node.args.args:
                if arg.arg == 'self':
                    continue
                if arg.annotation is None:
                    issues.append(f"{filepath.name}:{node.lineno}: {node.name}() arg '{arg.arg}' missing type hint")
    return issues


def main():
    """Check all modules in the supplycm package."""
    pkg_root = Path(__file__).parent.parent / 'supplycm'
    all_issues = []
    files_checked = 0

    for pyfile in sorted(pkg_root.rglob('*.py')):
        if pyfile.name == '__init__.py':
            continue
        files_checked += 1
        issues = check_module(pyfile)
        all_issues.extend(issues)

    print(f"Checked {files_checked} files")
    if all_issues:
        print(f"Found {len(all_issues)} type hint issues:")
        for issue in all_issues[:20]:
            print(f"  {issue}")
        if len(all_issues) > 20:
            print(f"  ... and {len(all_issues) - 20} more")
        return False
    else:
        print("All public functions have type hints.")
        return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
