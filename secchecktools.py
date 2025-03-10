from dotenv import load_dotenv
import os
load_dotenv()
import requests
import json
import time

class api_client():
    def pwned_client(self, pwned_api_url) -> dict[str, str]:
        self.pwned_api_url = pwned_api_url
        
        pwn_api_key = os.getenv("PWN_API_KEY")
        headers: dict[str, str] = {
            "User-Agent" : "pwnedornot",
            "hibp-api-key" : pwn_api_key
        }
        response = requests.get(pwned_api_url, headers=headers)
        data = response.json()
        result: dict[str, str] = json.dumps(data, indent=4)
        print(result)

    def virustotal_client(self, vt_api_url) -> dict[str, str]:
        self.vt_api_url = vt_api_url
        
        vt_api_key = os.getenv("VT_API_KEY")
        headers: dict[str, str] = {
            "accept": "application/json",
            "x-apikey" : vt_api_key
        }
        response: str = requests.get(vt_api_url, headers=headers)
        data: str = response.json()
        result: dict[str, str] = json.dumps(data, indent=4)
        print(result)
        
if __name__ == '__main__':
    pwn_check = api_client().pwned_client    
    # Pass emails from env
    emails = os.environ.get("EMAIL_LIST", "")
    email_list = emails.split(",")
    for email in email_list:
        print(f"Retrieved Data for: {email}")
        pwn_api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=true"
        pwn_check(pwn_api_url)
        time.sleep(10)
    
    vt_check = api_client().virustotal_client
    # Pass domains from env
    domains = os.environ.get("DOMAIN_LIST", "")
    domain_list = domains.split(",")
    for domain in domain_list:
        print(f"Retrieved Data for: {domain}")
        vt_api_url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        vt_check(vt_api_url)
        time.sleep(6)