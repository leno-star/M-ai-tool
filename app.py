from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>مولد السكربتات</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f1f2f6;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #2d3436;
        }
        form {
            margin-top: 30px;
        }
        input[type="text"] {
            padding: 10px;
            width: 70%%;
            border-radius: 8px;
            border: 1px solid #b2bec3;
            font-size: 16px;
        }
        button {
            margin-top: 20px;
            padding: 10px 25px;
            background-color: #0984e3;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }
        .output {
            margin-top: 30px;
            padding: 20px;
            background-color: #dfe6e9;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <h1>✅ مولد السكربتات التسويقية</h1>
    <p>أدخل اسم المنتج لتحصل على سكربت تسويقي جاهز:</p>
    <form method="POST">
        <input type="text" name="product" placeholder="اكتب اسم المنتج هنا..." required />
        <br>
        <button type="submit">توليد السكربت</button>
    </form>

    {% if result %}
    <div class="output">
        <h3>السكربت الناتج:</h3>
        <p>{{ result }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        product = request.form.get("product", "").strip()
        if product:
            result = f"هل تبحث عن {product} المثالي؟ موقعنا يقدّم لك المنتج الأروع بأسلوب ذكي وسعر خرافي! 🚀"
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(debug=True)
