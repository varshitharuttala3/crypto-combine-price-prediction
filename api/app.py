html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Crypto Price Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #141e30, #243b55);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            width: 350px;
            text-align: center;
        }

        h2 {
            margin-bottom: 20px;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #243b55;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background-color: #141e30;
        }

        .result {
            margin-top: 15px;
            font-weight: bold;
            color: #243b55;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>Crypto Price Prediction</h2>
        <form action="/predict" method="post">
            <input type="text" name="feature1" placeholder="Feature 1" required>
            <input type="text" name="feature2" placeholder="Feature 2" required>
            <input type="text" name="feature3" placeholder="Feature 3" required>
            <input type="text" name="feature4" placeholder="Feature 4" required>
            <input type="text" name="feature5" placeholder="Feature 5" required>
            <button type="submit">Predict</button>
        </form>

        <div class="result">
            {{ prediction_text }}
        </div>
    </div>
</body>
</html>
"""
