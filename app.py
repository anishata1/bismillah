from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)


@app.route("/static/bismillah.webp")
def bismillah_image():
    return send_from_directory(
        "static",
        "bismillah.webp",
        mimetype="image/webp"
    )


HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Bismillah</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px;

            background:
                radial-gradient(
                    circle at 15% 20%,
                    rgba(30, 100, 140, 0.35),
                    transparent 35%
                ),
                radial-gradient(
                    circle at 85% 80%,
                    rgba(20, 80, 120, 0.30),
                    transparent 35%
                ),
                linear-gradient(
                    135deg,
                    #dceff5,
                    #f8fbfc,
                    #c9e2ed
                );

            font-family: Georgia, "Times New Roman", serif;
        }

        .container {
            width: 100%;
            max-width: 650px;
            text-align: center;
        }

        .title {
            color: #102d5c;
            font-size: 38px;
            margin-bottom: 25px;
        }

        .card {
            padding: 18px;
            background: rgba(255, 255, 255, 0.80);
            border-radius: 20px;

            box-shadow:
                0 20px 50px rgba(0, 40, 80, 0.25),
                0 5px 15px rgba(0, 0, 0, 0.10);

            backdrop-filter: blur(10px);
        }

        .image {
            display: block;
            width: 100%;
            height: auto;
            border-radius: 12px;

            box-shadow:
                0 8px 25px rgba(0, 0, 0, 0.20);
        }

        .caption {
            margin-top: 20px;
            color: #17365d;
            font-size: 18px;
        }

        .footer {
            margin-top: 18px;
            color: #49677d;
            font-size: 14px;
        }

        @media (max-width: 600px) {
            body {
                padding: 15px;
            }

            .title {
                font-size: 28px;
            }

            .card {
                padding: 10px;
            }
        }
    </style>
</head>

<body>

    <div class="container">

        <div class="title">
            بِسْمِ اللَّهِ
        </div>

        <div class="card">

            <img
                src="/static/bismillah.webp"
                alt="Bismillah Arabic Calligraphy"
                class="image"
            >

            <div class="caption">
                In the name of Allah, the Most Gracious, the Most Merciful
            </div>

        </div>

        <div class="footer">
            Bismillah Calligraphy
        </div>

    </div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
