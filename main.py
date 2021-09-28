from flask import Flask, render_template
import requests 
from post import Post

posts = requests.get("https://api.npoint.io/481a7600531b2b6e139d").json()
post_dict = {}
for post in posts:
    new_post = Post(
                    post["id"],post["title"], 
                    post["contents"], post["link"])
    post_dict[int(post["id"])] = new_post
print(post_dict.keys())

app = Flask(__name__)

@app.route('/')
def home():
    posts = [post for post in post_dict.values()]
    return render_template("index.html", posts=posts)

@app.route('/blog/<num>')
def get_blog(num):
    post = post_dict[int(num)] 
    return render_template('post.html',num=num, post=post)


if __name__ == "__main__":
    app.run(debug=True)
