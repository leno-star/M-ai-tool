print("مرحبًا بك في مولد السكربتات!")
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <title>مولّد السكربتات</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f1f2f6;
            text-align: center;
            padding: 50px;
            direction: rtl;
        }
        h1 {
            color: #2d3436;
            margin-bottom: 20px;
        }
        form {
            margin-top: 30px;
        }
        input[type="text"] {
            padding: 10px;
            width: 70%;
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
            display: none;
        }
    </style>
</head>
<body>
    <h1>موقع توليد السكربتات ✔</h1>
    <p>أدخل اسم المنتج لتحصل على سكربت تسويقي جاهز:</p>

    <form id="scriptForm">
        <input type="text" id="productInput" placeholder="اكتب اسم المنتج هنا..." required />
        <br>
        <button type="submit">توليد السكربت</button>
    </form>

    <div class="output" id="scriptOutput">
        <h3>السكربت الناتج:</h3>
        <p id="resultText">📌 السكربت رح يظهر هون بعد التوليد.</p>
    </div>

    <script>
        document.getElementById('scriptForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const product = document.getElementById('productInput').value.trim();
            if (product) {
                document.getElementById('resultText').textContent = `هل تبحث عن ${product} مثالي؟ موقعنا يقدّم لك المنتج الأروع بأسلوب ذكي وسعر خرافي! 🚀`;
                document.getElementById('scriptOutput').style.display = 'block';
            }
        });
    </script>
</body>
</html>