from flask import Flask, render_template_string

app = Flask(__name__)

# Données des formations
formations = [
    {"id": 1, "titre": "Docker & Kubernetes", "formateur": "Expert Cloud", "duree": "3 jours", "statut": "Disponible"},
    {"id": 2, "titre": "CI/CD avec GitHub Actions", "formateur": "DevOps Engineer", "duree": "2 jours", "statut": "Bientôt"},
    {"id": 3, "titre": "Python pour l'Automatisation", "formateur": "Data Scientist", "duree": "5 jours", "statut": "Disponible"},
    {"id": 4, "titre": "Terraform & IaC", "formateur": "SRE Specialist", "duree": "4 jours", "statut": "Complet"}
]

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formations</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; margin: 0; padding: 20px; color: #333; }
            .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
            header { text-align: center; border-bottom: 2px solid #eee; padding-bottom: 20px; margin-bottom: 30px; }
            h1 { color: #2c3e50; margin: 0; }
            p.subtitle { color: #7f8c8d; font-size: 1.1em; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 15px; text-align: left; border-bottom: 1px solid #eee; }
            th { background-color: #2c3e50; color: white; border-radius: 4px 4px 0 0; }
            tr:hover { background-color: #f9f9f9; }
            .badge { padding: 5px 10px; border-radius: 20px; font-size: 0.85em; font-weight: bold; }
            .dispo { background-color: #d4edda; color: #155724; }
            .bientot { background-color: #fff3cd; color: #856404; }
            .complet { background-color: #f8d7da; color: #721c24; }
            footer { margin-top: 30px; text-align: center; font-size: 0.9em; color: #bdc3c7; }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>🚀 Formations</h1>
                <p class="subtitle">Catalogue des Formations Techniques & DevOps</p>
            </header>
            
            <table>
                <thead>
                    <tr>
                        <th>Formation</th>
                        <th>Formateur</th>
                        <th>Durée</th>
                        <th>Statut</th>
                    </tr>
                </thead>
                <tbody>
                    {% for f in formations %}
                    <tr>
                        <td><strong>{{ f.titre }}</strong></td>
                        <td>{{ f.formateur }}</td>
                        <td>{{ f.duree }}</td>
                        <td>
                            <span class="badge {% if f.statut == 'Disponible' %}dispo{% elif f.statut == 'Bientôt' %}bientot{% else %}complet{% endif %}">
                                {{ f.statut }}
                            </span>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>

            <footer>
                <p>&copy; 2026 Startup Academy - Déployé via Pipeline CI/CD</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, formations=formations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)