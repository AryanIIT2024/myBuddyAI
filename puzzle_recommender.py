def get_puzzle_for_mood(mood):
    # Example mapping of moods to puzzle types
    mapping = {
        "happy": "https://gameofcrowns.sanish.me/",  # Queens-like (Star Battle)
        "sad": "https://crossclimb-game.com/",       # Crossclimb
        "anxious": "https://www.tangogame.org/",     # Tango equivalent
        "anger": "https://www.zipunlimitedgame.com",  # Zip style
        "joy": "https://www.zipunlimitedgame.com",


    }
    return mapping.get(mood.lower(), "https://www.wordgames.com")  # Default fallback
