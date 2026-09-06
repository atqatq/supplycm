# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in supplycm, please report it responsibly.

### How to Report

1. **Do not** open a public GitHub issue.
2. Email the maintainer directly with details of the vulnerability.
3. Include a description of the issue, steps to reproduce, and potential impact.

### Response Timeline

- **Acknowledgment**: Within 48 hours of receiving your report.
- **Initial Assessment**: Within 7 days.
- **Fix Release**: Within 30 days for critical issues, 90 days for others.

## Security Considerations

supplycm is a pure-Python library with no external dependencies. However:

1. **Input validation**: Most algorithms validate inputs, but always sanitize data from untrusted sources before passing it to library functions.
2. **Numerical stability**: Some algorithms may produce unexpected results with extreme or NaN inputs. Always validate output ranges.
3. **No network access**: The library does not make any network calls, reducing attack surface.

## Supported Versions

Only the latest release receives security updates.

| Version | Supported          |
|---------|--------------------|
| 0.1.x   | Yes                |
| < 0.1   | No                 |
