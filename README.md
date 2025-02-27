# SSRF Detection Tool

## Overview
This tool automates the detection of Server-Side Request Forgery (SSRF) vulnerabilities by injecting common SSRF payloads into a specified parameter and analyzing responses.

## Features
- Tests multiple SSRF payloads targeting internal services.
- Identifies possible SSRF vulnerabilities based on HTTP responses.
- Easy-to-use command-line interface.

## Installation
```bash
pip install requests
```

## Usage
```bash
python ssrf_detector.py -u <TARGET_URL> -p <PARAMETER>
```

### Example
```bash
python ssrf_detector.py -u "http://example.com/api" -p url
```

## License
MIT License

## 📜 Disclaimer
This tool is for educational and ethical testing purposes only. **Do not use it on unauthorized systems.**

## 👨‍💻 Author
**Jatin** - Bug Bounty Hunter | Cybersecurity Enthusiast 🚀


## Donate a Coffee:
Paypal: pardeshijatin1998@gmail.com
