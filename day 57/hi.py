from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
posts = requests.get(blog_url).json()
for post in posts:
    print(post)