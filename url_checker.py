import re

url = input("Enter URL: ")

if not url.startswith("https://"):
    print("⚠️ Warning: URL does not use HTTPS")
else:
    print("✅ HTTPS detected")

if re.search(r"@|--|%", url):
    print("⚠️ Suspicious characters found")
