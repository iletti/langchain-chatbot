import json
import os

# Path to your Ghost JSON export file
json_path = "ilari-schmidt.ghost.2025-04-06-14-03-25.json"

# Create a folder to store extracted blog posts
output_folder = "blog_posts"
os.makedirs(output_folder, exist_ok=True)

# Load the JSON data
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# The posts are typically nested under the "db" key.
posts = data["db"][0]["data"]["posts"]

for post in posts:
    # Use the post title for the filename (sanitize it)
    title = post.get("title", "untitled")
    safe_title = "".join(c if c.isalnum() or c in " _-" else "_" for c in title)
    filename = f"{safe_title}.txt"
    
    # Get the post content – use the plaintext field, and default to an empty string if it's None
    content = post.get("plaintext") or ""
    
    # Write the content to a text file
    file_path = os.path.join(output_folder, filename)
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(content)

print(f"Extracted {len(posts)} posts into the '{output_folder}' folder.")
