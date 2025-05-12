from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    comment = ""
    if request.method == "POST":
        comment = request.form["comment"]
    return render_template_string('''
        <h2>Deixe um comentário:</h2>
        <form method="post">
            <input type="text" name="comment">
            <input type="submit" value="Enviar">
        </form>
        <p><strong>Comentário recebido:</strong> {{ comment | safe }}</p>
    ''', comment=comment)

if __name__ == "__main__":
    app.run(debug=True)
