import requests
from sent_email import send_email

# Get Topic
topic = "Data engineer project"
language = "en"

api_key = "6d93aeca3b6e47359757fb74f60f9b20"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&" \
    "apiKey=6d93aeca3b6e47359757fb74f60f9b20&" \
    f"language={language}"

# Make request
request = requests.get(url)

# Get dict with data
content = request.json()

# Access articles titles and descriptions
message = "Subject: Today's news about" + " " + topic + "\n"

# if content.get("articles") is not None:
for article in content.get("articles")[:20]:
    if (article.get("title") is not None) and (article.get("description") is not None):
        message += article.get("title") + "\n" + article.get(
            "description") + "\n" + article.get("url") + 2*"\n"

message = message.encode("utf-8")
send_email(message=message)
