# Written by Subrahmanya Ghanta

import openai
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///queries.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class ChatQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    length = db.Column(db.String(20), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)

    def __init__(self, keyword, category, location, date, length, prompt, response):
        self.keyword = keyword
        self.category = category
        self.location = location
        self.date = date
        self.length = length
        self.prompt = prompt
        self.response = response


@app.route('/')
def home():
    return render_template('newsview.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register1')
def register1():
    return render_template('register1.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/generate_news', methods=['POST'])
def generate_news():
    try:
        data = request.get_json()
        keyword = data.get('keyword', 'Nothing')
        category = data.get('category', 'General')
        location = data.get('location', 'Global')
        date = data.get('date', 'Today')
        length = data.get('length', 'Short')

        token_map = {
            "short": 250,
            "medium": 500,
            "long": 700
        }
        max_tokens = token_map.get(length.lower(), 50)

        prompt = (
            f"Generate a {length.lower()} news article and cite new outlets as sources about {category} in {location} on {date} "
            f"with the topic '{keyword}' and make sure the news is realistic if the topic is nothing ask for more information."
        )

        chat_completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )

        news_content = chat_completion['choices'][0]['message']['content'].strip()

       
        new_query = ChatQuery(
            keyword=keyword,
            category=category,
            location=location,
            date=date,
            length=length,
            prompt=prompt,
            response=news_content
        )
        db.session.add(new_query)
        db.session.commit()

        return jsonify({
            "success": True,
            "title": f"{category} News - {keyword}",
            "content": news_content
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })

@app.route('/clear_history', methods=['POST'])
def clear_history():
    try:
        
        ChatQuery.query.delete()
        db.session.commit()
        return jsonify({
            "success": True,
            "message": "History cleared successfully."
        })
    except Exception as e:
        db.session.rollback() 
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        })



@app.route('/query_history', methods=['GET'])
def query_history():
    try:
        queries = ChatQuery.query.all()
        history = [
            {
                "id": query.id,
                "keyword": query.keyword,
                "category": query.category,
                "location": query.location,
                "date": query.date,
                "length": query.length,
                "prompt": query.prompt,
                "response": query.response
            } for query in queries
        ]

        return jsonify({
            "success": True,
            "history": history
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='127.0.0.1', port=8000)

