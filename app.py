from flask import Flask, render_template_string

app = Flask(__name__)

# Liste de formations statique
formations = [
    {"titre": "Docker & Kubernetes", "duree": "3 jours"},
    {"titre": "CI/CD avec GitHub Actions", "duree": "2 jours"},
    {"titre": "Terraform Infrastructure as Code", "duree": "4 jours"}
]

@app.route('/')
def home():
    html = """
    <h1>Bienvenue à la Startup Academy</h1>
    <h2>Nos Formations :</h2>
    <ul>
        {% for f in formations %}
            <li><strong>{{ f.titre }}</strong> - {{ f.duree }}</li>
        {% endfor %}
    </ul>
    """
    return render_template_string(html, formations=formations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)