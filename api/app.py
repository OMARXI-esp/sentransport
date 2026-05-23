import json

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r") as f:
    lignes = json.load(f)

@app.route("/")
def accueil():

    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>"]
    })

@app.route("/lignes")
def get_lignes():

    return jsonify(lignes)
	

@app.route("/arrets")
def get_arrets():

    arrets = set()

    for ligne in lignes:

        for arret in ligne["listeArrets"]:

            arrets.add(arret)

    return jsonify(list(arrets))
	
@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):

    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )

    if ligne is None:

        return jsonify({
            "erreur": "Ligne non trouvee"
        }), 404

    return jsonify(ligne)

@app.route("/stats")
def get_stats():

    total_lignes = len(lignes)

    total_arrets = sum(
        ligne["arrets"] for ligne in lignes
    )

    ligne_max = max(
        lignes,
        key=lambda ligne: ligne["arrets"]
    )

    return jsonify({

        "total_lignes": total_lignes,

        "total_arrets": total_arrets,

        "ligne_plus_arrets":
            ligne_max["numero"]

    })
	
@app.route("/lignes/recherche")
def recherche_lignes():

    q = request.args.get("q", "").lower()

    resultats = [

        ligne for ligne in lignes

        if q in ligne["depart"].lower()

        or q in ligne["arrivee"].lower()

    ]

    return jsonify(resultats)
if __name__ == "__main__":

    app.run(debug=True, port=5000)
