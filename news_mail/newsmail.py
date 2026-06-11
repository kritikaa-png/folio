import feedparser
import smtplib
import os
from email.mime.text import MIMEText

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

feeds = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss"
}

html = """
<html>
<body>
<h2>📰 Daily News Digest</h2>
"""

for source, url in feeds.items():

    feed = feedparser.parse(url)

    html += f"<h3>{source}</h3><ul>"

    for article in feed.entries[:3]:

        title = article.title
        link = article.link

        published = getattr(
            article,
            "published",
            "Time unavailable"
        )

        html += f"""
        <li>
            <a href="{link}">
                {title}
            </a><br>
            <small>{published}</small>
        </li>
        """

    html += "</ul>"

html += """
<hr>
<p>Generated automatically using Python & GitHub Actions.</p>
</body>
</html>
"""

msg = MIMEText(html, "html")
msg["Subject"] = "Daily News Digest"
msg["From"] = EMAIL
msg["To"] = EMAIL

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORD)

server.sendmail(
    EMAIL,
    EMAIL,
    msg.as_string()
)

server.quit()

print("News email sent successfully!")