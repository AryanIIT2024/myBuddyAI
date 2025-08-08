def get_books_for_emotion(mood):
    books = {
        "happy": [
            {"title": "The Alchemist", "author": "Paulo Coelho"},
            {"title": "Big Magic", "author": "Elizabeth Gilbert"},
        ],
        "sad": [
            {"title": "Reasons to Stay Alive", "author": "Matt Haig"},
            {"title": "Man’s Search for Meaning", "author": "Viktor Frankl"},
        ],
        "anxious": [
            {"title": "Atomic Habits", "author": "James Clear"},
            {"title": "The Power of Now", "author": "Eckhart Tolle"},
        ]
    }
    return books.get(mood.lower(), [])
