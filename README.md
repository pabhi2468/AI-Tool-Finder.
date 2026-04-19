# 🔍 AI Tool Finder

AI Tool Finder is a web-based application that leverages OpenAI's API to help users discover and explore AI-powered tools across various domains like image generation, audio editing, video editing, coding, and more. Simply type what you're looking for (e.g., "AI image generator" or "code assistant"), and get a curated, well-formatted list of tools — complete with descriptions, features, and links.

---

## 🖼️ Preview

![AI Tool Finder Screenshot](./preview.png)

---

## ✨ Features

- 🔎 **Natural Language Search** — Just type what you need, no filters or dropdowns.
- 🧠 **Powered by OpenAI** — Uses GPT-based responses to return tool recommendations.
- 🌐 **Responsive UI** — Built with HTML/CSS and designed for dark mode.
- ⚡ **Real-time Loading** — Includes a loading spinner and search feedback.
- 🧩 **Expandable** — Easily extend with categories, filters, or analytics.

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS (Dark Mode + Responsive)
- **Backend:** Python (Flask)
- **API:** OpenAI GPT API (v1.x)
- **Icons & Styling:** FontAwesome, Google Fonts, Custom Dark Theme

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-tool-finder.git
cd ai-tool-finder
```

### 2. Install dependencies
Make sure you have Python installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set up OpenAI API Key
Replace the placeholder `OPEN AI API KEY` in `app.py` with your actual OpenAI API key. Alternatively, set it as an environment variable:
```bash
export OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the application
Start the Flask development server:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000`.

---

## 📂 Project Structure

```
ai-tool-finder/
├── app.py                # Flask backend
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── static/               # Static assets (CSS, JS)
│   ├── style.css         # Stylesheet
│   └── script.js         # JavaScript logic
├── templates/            # HTML templates
│   └── index.html        # Main UI
└── preview.png           # Screenshot of the application
```

---

## 🧪 Example Usage

1. Open the application in your browser.
2. Enter a query like "AI image generator" in the search box.
3. View the curated list of AI tools with descriptions, features, and links.

---

## 🛡️ License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

---
