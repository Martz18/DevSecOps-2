from app import get_pokemon_data

def test_get_pokemon_data_valid():
    pokemon_data = get_pokemon_data("Hoopa-Unbound")
    assert pokemon_data is not None
    assert pokemon_data['pokemon_name'] == "Hoopa-unbound"
    assert 'pokedex_number' in pokemon_data
    assert 'abilities' in pokemon_data
    assert isinstance(pokemon_data['pokedex_number'], int)

def test_get_pokemon_name_false():
    pokemon_data = get_pokemon_data("False_Pokemon")
    assert pokemon_data == {'error': "Pokémon 'False_Pokemon' non trouvé (Statut: 404)"}