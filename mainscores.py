from flask import Flask

app = Flask(__name__)
@app.route("/")
def score_server():
    try:
        with open('score.txt', "r") as file:
            user_score = file.read()
            html = f"""
                <html>
                <head>
                <title>Scores Game</title>
                </head>
                <body>
                <h1>The score is <div id="score">{user_score}</div></h1>
                </body>
                </html>
            """
        return html
    except Exception as e:
        error_html = f"""
            <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
            <h1><div id="score" style="color:red">{str(e)}</div></h1>
            </body>
            </html>
        """
        return error_html
if __name__ == "__main__":
    app.run()