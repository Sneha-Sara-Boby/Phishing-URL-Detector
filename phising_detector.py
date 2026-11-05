
import re

def unique_detector(url):
    score = 0
    reason = []

    # Rule 1: Check for IP address instead of domain name
    if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
        score += 3
        reason.append("Uses an IP address instead of domain name")

    # Rule 2: Check for suspicious keywords
    keywords = ['verify', 'secure', 'banking',
                'update', 'login', 'wp-admin']

    if any(key in url.lower() for key in keywords):
        score += 1
        reason.append("Contains suspicious keywords")

    # Rule 3: Check for excessive subdomains
    if url.count(".") > 3:
        score += 2
        reason.append("Too many subdomains")

    # Rule 4: Check for URL length
    if len(url) > 75:
        score += 1
        reason.append("URL is abnormally long")

    # Rule 5: Check for @ symbol
    if "@" in url:
        score += 2
        reason.append("Uses @ symbol to mask destination")

    # Return final assessment
    return {
        "score": score,
        "reason": reason,
        "is_suspicious": score >= 3
    }


# Main program
url = input("Enter a URL: ")

result = unique_detector(url)

print("\n--- Phishing URL Detection Result ---")
print("URL:", url)
print("Suspicious Score:", result["score"])

if result["is_suspicious"]:
    print("Status: Suspicious URL")
else:
    print("Status: Not flagged as suspicious")

print("Reasons:")

if result["reason"]:
    for item in result["reason"]:
        print("-", item)
else:
    print("No suspicious indicators detected.")
