def get_puzzle_for_mood(mood):
    # Example mapping of moods to puzzle types
    mapping = {
        "happy": "https://gameofcrowns.sanish.me/",  # Queens-like (Star Battle)
        "sad": "https://www.crazygames.com/game/blockbuster-puzzle",       # Crossclimb
        "anxious": "https://www.tangogame.org/",     # Tango equivalent
        "anger": "https://onlinegameweb.com/game/zip-game",  # Zip style
        "joy": "https://onlinegameweb.com/game/zip-game",


    }
    return mapping.get(mood.lower(), "https://www.wordgames.com")  # Default fallback
