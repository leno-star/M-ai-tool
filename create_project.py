import os

# إنشاء المجلدات الأساسية مباشرة داخل المشروع
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# الملفات ومحتواها
files = {
    "app.py": '''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    script = ""
    if request.method == "POST":
        script = "هذا سكريبت تجريبي بناءً على المنتج."
        with open("scripts.txt", "a", encoding="utf-8") as f:
            f.write(script + "\\n---\\n")
    return render_template("index.html", script=script)

@app.route("/scripts")
def view_scripts():
    try:
        with open("scripts.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = "🚫 لا يوجد سكريبتات محفوظة بعد."
    return render_template("scripts.html", scripts=content)

if __name__ == "__main__":
    app.run(debug=True)
''',

    "requirements.txt": "flask\ngunicorn",
    "Procfile": "web: gunicorn app:app",
    "README.md": "# M-ai-tool\n\nأداة ذكية لتوليد سكريبتات تسويقية.",
    "templates/index.html": "<h1>📸 أداة توليد السكريبتات</h1>",
    "templates/scripts.html": "<h1>📜 السكريبتات المحفوظة</h1>",
    "static/style.css": "body { font-family: Arial; }",
    "scripts.txt": "",
    "subscribers.txt": ""
}

# إنشاء الملفات
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ تم إنشاء مشروع M-ai-tool بنجاح بدون أي تعارض في المجلدات!")