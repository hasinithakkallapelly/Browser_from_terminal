import webbrowser
import sys
from urllib.parse import quote_plus

valid_websites = [
    "reddit.com",
    "stackoverflow.com",
    "medium.com"
]

def create_filter():
    return "(" + " OR ".join(f"site:{site}" for site in valid_websites) + ")"

def create_query():
    return " ".join(sys.argv[1:])

if len(sys.argv) == 1:
    print("Usage: google your search words")
else:
    query = create_query()
    final_query = query + " " + create_filter()
    final_url = "https://www.google.com/search?q=" + quote_plus(final_query)

    webbrowser.get("safari").open(final_url)