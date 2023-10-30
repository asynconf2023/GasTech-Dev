from flask import Flask, render_template, request
import Algo
from flaskwebgui import FlaskUI
app = Flask(__name__)
resultat = 0
# Listes d'options pour chaque menu déroulant
options_voiture = ["Citadine", "Cabriolet", "Berline", "SUV"]
options_energie = ["Essence", "Diesel", "Electrique", "Hybride"]
options_kilometrage = ["5000 - 10000 km", "10000 - 15000 km", "15000 - 20000 km", "20000 - 25000 km", "25000 - 30000 km"]
options_annee = ["1960-1970", "1970 - 1990", "1990 - 2000", "2000 - 2010" , "Après 2010"]
option_passager = ["1", "2", "3", "4"]
# Route principale de l'application
@app.route('/', methods=['GET', 'POST'])
def index():
    global resultat
    voiture_selected = None
    energie_selected = None
    kilometrage_selected = None
    annee_selected = None
    if request.method == 'POST':
        # Récupérer ce que l'utilisateur a envoyer
        voiture_selected = request.form['voiture']
        energie_selected = request.form['energie']
        kilometrage_selected = request.form['kilometrage']
        annee_selected = request.form['annee']
        options_passager = request.form['passager']
        print(voiture_selected)
        print(energie_selected)
        print(kilometrage_selected)
        print(options_passager)
        print(annee_selected)
        print(Algo.AddPassager(options_passager, annee_selected, voiture_selected, energie_selected, kilometrage_selected))
        resultat = Algo.AddPassager(options_passager, annee_selected, voiture_selected, energie_selected, kilometrage_selected)
        if resultat == None:
            resultat = 0
        # Vous pouvez maintenant utiliser ces variables pour effectuer des calculs ou d'autres actions
    return render_template('index.html', options_voiture=options_voiture, options_energie=options_energie,
                           options_kilometrage=options_kilometrage, options_annee=options_annee,
                           voiture_selected=voiture_selected, energie_selected=energie_selected,
                           kilometrage_selected=kilometrage_selected, annee_selected=annee_selected, option_passager=option_passager, resultat = resultat)

if __name__ == '__main__':
    app.run(debug=True)
