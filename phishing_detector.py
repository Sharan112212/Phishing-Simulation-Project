import re

def analyze_url(url):
    flags = 0
    
    # Check 1: Is it using HTTPS? (Secure)
    if not url.startswith("https"):
        print("🚩 Warning: Site does not use HTTPS.")
        flags += 1
        
    # Check 2: Are there too many dots? (e.g., login.microsoft.verify.com)
    if url.count('.') > 3:
        print("🚩 Warning: Unusual amount of subdomains.")
        flags += 1
        
    # Check 3: Suspicious Keywords
    keywords = ['login', 'verify', 'update', 'bank', 'secure', 'account']
    for word in keywords:
        if word in url.lower():
            print(f"🚩 Warning: Suspicious keyword detected: {word}")
            flags += 1
            break

    if flags >= 2:
        return "❌ Result: HIGH PROBABILITY OF PHISHING"
    return "✅ Result: URL appears safe."

# Test it
test_url = input("Enter a URL to analyze: ")
print(analyze_url(test_url))