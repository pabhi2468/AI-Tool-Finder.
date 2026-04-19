from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'), override=True)

app = Flask(__name__, template_folder="templates")

# ✅ Get OpenAI API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("WARNING: OPENAI_API_KEY not found in environment or .env file!")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '')

    try:
        current_api_key = os.getenv("OPENAI_API_KEY")
        if not current_api_key:
            return jsonify({"tools": "Error: OpenAI API Key is missing. Please check your .env file."})

        client = OpenAI(api_key=current_api_key)

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an AI tool finder. Based on the user's query, return a helpful and structured list of relevant AI tools in clean HTML format. For each tool, include a clickable name linking to the official site, a short description, and a list of 3-5 key features using HTML tags only (h3, a, p, ul, li)."},
                {"role": "user", "content": query}
            ]
        )

        # Extract response
        tools = response.choices[0].message.content

    except Exception as e:
        tools = f"Error: {str(e)}"

    return jsonify({"tools": tools})

if __name__ == '__main__':
    app.run(debug=True)
