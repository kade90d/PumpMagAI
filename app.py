from flask import Flask, render_template, request, send_file
from app.fetch_news import fetch_news_articles
from app.generate_articles import generate_feature_articles
from app.create_visuals import create_visuals
from app.layout_magazine import layout_magazine
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("magazine_template.html")

@app.route('/generate', methods=['POST'])
def generate_magazine():
    topics = request.form.getlist('topics')
    news = fetch_news_articles()
    articles = generate_feature_articles(topics)
    visuals = create_visuals(topics)
    magazine_path = layout_magazine(news, articles, visuals)
    return send_file(magazine_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)