import requests 
from flask import Flask, render_template, request, jsonify # Importation de jsonify
import json # Non utilisé ici, mais souvent utile pour gérer des données

app = Flask(__name__)

# --- Fonction Utilitaires pour l'API ---
def get_pokemon_data(pokemon_name):
    """
    Récupère toutes les données nécessaires (types, talents, stats, sprite, numéro) 
    pour un Pokémon donné à partir de la PokéAPI.
    """
    search_name = pokemon_name.lower().strip()
    pokeapi_url = f"https://pokeapi.co/api/v2/pokemon/{search_name}"
    response = requests.get(pokeapi_url)

    if response.status_code == 200:
        data = response.json()
        
        # 1. Numéro de Pokédex
        pokedex_number = data.get('id', '??')

        # 2. Types
        types_list = [t['type']['name'] for t in data.get('types', [])]

        # 3. Talents (Abilities)
        abilities_list = [a['ability']['name'].replace('-', ' ').capitalize() for a in data.get('abilities', [])]

        # 4. Sprite
        sprite_url = data['sprites'].get('front_default')

        # 5. Statistiques de base
        stats_list = []
        for stat in data.get('stats', []):
            stat_name = stat['stat']['name'].replace('-', ' ').capitalize()
            stats_list.append({
                'nom': stat_name,
                'valeur': stat['base_stat']
            })
            
        return {
            'pokemon_name': data['name'].capitalize(),
            'sprite': sprite_url,
            'pokedex_number': pokedex_number, 
            'types': types_list,             
            'abilities': abilities_list,     
            'stats_pokemon': stats_list
        }
    else:
        return {'error': f"Pokémon '{pokemon_name}' non trouvé (Statut: {response.status_code})"}

# --- Routes Flask ---

@app.route('/')
def bonjour_page():
    """Page d'accueil simple."""
    return render_template('bonjour.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon_page():
    """Route pour la recherche et l'affichage des données Pokémon."""
    pokemon_data = None
    pokemon_name = "Hoopa-Unbound" # Nom par défaut pour un premier affichage

    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
        
    if pokemon_name:
        pokemon_data = get_pokemon_data(pokemon_name)
    
    # Rendu du template
    if pokemon_data and 'error' in pokemon_data:
        # Afficher le message d'erreur
        return render_template('pokemon_info.html', 
                               pokemon_name=pokemon_name.capitalize(), 
                               error=pokemon_data['error'],
                               # On passe des listes vides pour éviter les erreurs Jinja dans le template
                               stats_pokemon=[], types=[], abilities=[])
    elif pokemon_data:
        # Afficher les données du Pokémon
        return render_template('pokemon_info.html', **pokemon_data)
    else:
        # Afficher l'état initial (ou un Pokémon par défaut si la recherche est vide)
        return render_template('pokemon_info.html', pokemon_name='Recherchez un Pokémon', error=None)

@app.route('/cat_facts')
def cat_facts():
    """Route pour la page principale des faits sur les chats."""
    return render_template('cat_facts.html')

@app.route('/autre_api')
def autre_api():
    """Route pour une autre API hypothétique."""
    return render_template('autre_api.html')


# --- NOUVELLES ROUTES API (Pour les appels AJAX depuis cat_facts.html) ---

@app.route('/api/catfact')
def api_cat_fact():
    """Endpoint d'API pour récupérer un fait sur les chats (appelé par JavaScript)."""
    try:
        response = requests.get('https://catfact.ninja/fact')
        response.raise_for_status()
        data = response.json()
        
        # Retourner le fait au format JSON
        return jsonify(data) 
    
    except requests.exceptions.RequestException as e:
        # Gérer les erreurs de connexion ou de l'API externe
        return jsonify({'error': 'Erreur de récupération de l\'API Cat Facts', 'fact': 'API indisponible.'}), 500

@app.route('/api/bonjour')
def api_bonjour():
    """Endpoint d'API pour la réponse au bouton 'salut' (appelé par JavaScript)."""
    return jsonify({
        'response': "Salut ! Tu as bien fait de ne pas me laisser un vent. Bienvenue sur la page des chats."
    })


if __name__ == '__main__':
    app.run(debug=True)