import requests
from sent_email import send_email

api_key = "6d93aeca3b6e47359757fb74f60f9b20"
url = "https://newsapi.org/v2/everything?q=tesla" \
    "&from=2023-06-03&sortBy=publishedAt&apiKey" \
    "=6d93aeca3b6e47359757fb74f60f9b20"

# Make request
request = requests.get(url)

# Get dict with data
content = request.json()

# Access articles titles and descriptions
message = ""
for article in content.get("articles"):
    if article.get("title") and article.get("description") is not None:
        message += article.get("title") + "\n" + article.get("description") + 2*"\n"

message = message.encode("utf-8")
send_email(message=message)


