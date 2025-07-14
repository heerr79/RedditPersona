import os
import re
from datetime import datetime
from textblob import TextBlob
from dotenv import load_dotenv
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username(url):
    return url.strip("/").split("/")[-1]

def sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def analyze_user(username):
    redditor = reddit.redditor(username)
    posts, comments = [], []
    top_subs = {}
    activity_hours = []
    self_desc = []
    tones = []
    total_posts = 0
    total_comments = 0

    try:
        for post in redditor.submissions.new(limit=30):
            content = f"{post.title} {post.selftext}"
            url = f"https://reddit.com{post.permalink}"
            posts.append((content, url))
            total_posts += 1
            top_subs[post.subreddit.display_name] = top_subs.get(post.subreddit.display_name, 0) + 1
            tones.append(sentiment_score(content))
            activity_hours.append(datetime.fromtimestamp(post.created_utc).hour)
            if re.search(r"\b(I am|I'm|My name is|I work as|I live in)\b", content, re.I):
                self_desc.append((content.strip()[:100] + "...", url))

        for comment in redditor.comments.new(limit=50):
            url = f"https://reddit.com{comment.permalink}"
            comments.append((comment.body, url))
            total_comments += 1
            top_subs[comment.subreddit.display_name] = top_subs.get(comment.subreddit.display_name, 0) + 1
            tones.append(sentiment_score(comment.body))
            activity_hours.append(datetime.fromtimestamp(comment.created_utc).hour)
            if re.search(r"\b(I am|I'm|My name is|I work as|I live in)\b", comment.body, re.I):
                self_desc.append((comment.body.strip()[:100] + "...", url))
    except Exception as e:
        print(f"Error: {e}")
        return

    avg_tone = sum(tones) / len(tones) if tones else 0
    tone_label = "Positive" if avg_tone > 0.2 else "Neutral" if avg_tone >= -0.2 else "Negative"
    top_subs_sorted = sorted(top_subs.items(), key=lambda x: x[1], reverse=True)[:5]
    active_hour = max(set(activity_hours), key=activity_hours.count) if activity_hours else "Unknown"

    persona_text = f"""
=========================
🧑 Reddit User Persona
=========================
👤 Username: u/{username}

📚 Top Subreddits (Interests):
{', '.join([f"{s[0]} ({s[1]} posts)" for s in top_subs_sorted])}

📊 Activity Type:
Posts: {total_posts}, Comments: {total_comments}

🕓 Most Active Hour: {active_hour}:00

🎭 Overall Tone: {tone_label}

🗣️ Self-Descriptions Found:
"""
    for desc, url in self_desc:
        persona_text += f'\n- "{desc}"\n  → Source: {url}'

    with open(f"{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(persona_text.strip())

    print(f"\n✅ Persona file generated: {username}_persona.txt")

if __name__ == "__main__":
    url = input("Enter Reddit user profile URL: ").strip()
    username = extract_username(url)
    analyze_user(username)
