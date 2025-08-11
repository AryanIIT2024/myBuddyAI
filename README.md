🧠 FeelBuddy: Your AI Companion 😊
FeelBuddy is a powerful, interactive web application built with Streamlit that serves as your personal AI companion. It analyzes your mood from a text entry and provides personalized recommendations for songs, books, and puzzles to match or improve your emotional state. Designed with a vibrant, hackathon-friendly UI, this app offers a unique and engaging user experience.

✨ Features
Mood Analysis: Utilizes a custom emotion_analysis module to detect the user's mood from free-form text.

Personalized Recommendations:

🎶 Song Recommendations: Fetches a list of songs from a Spotify recommender based on the detected mood.

📚 Book Recommendations: Provides book suggestions, powered by a DeepSeek recommender.

🧩 Puzzle Recommendations: Offers a puzzle link tailored to the user's mood.

Journaling & Streak Tracker: Saves mood entries to a CSV file and tracks the user's daily usage streak.

Leaderboard: Displays a simple leaderboard of users based on their puzzle streaks.

Dynamic UI/UX: Features a vibrant, cyberpunk-inspired theme with custom CSS, Lottie animations for a lively feel, and a responsive layout for all devices.

🚀 Setup and Installation
Prerequisites
Python 3.7 or higher

Installation
Clone the Repository: If your project is in a repository, clone it. Otherwise, ensure all the necessary files (app.py, emotion_analysis.py, spotify_recommender.py, etc.) are in the same directory.

Install Libraries: Open your terminal or command prompt and run the following command to install the required Python libraries:

pip install streamlit pandas requests streamlit-lottie

(Note: You will also need to have emotion_analysis, spotify_recommender, deepseek_recommender, and puzzle_recommender modules in your project directory for the app to function correctly.)

▶️ How to Run the App
Once all the dependencies are installed and your Python files are in place, you can run the app with this single command from your terminal:

streamlit run app.py

The application will automatically open in your default web browser.

💻 Usage
Enter your feelings: On the main page, type how you are feeling in the text box.

Analyze Mood: Click the vibrant orange "Analyze Mood & Get Recommendations" button. The app will display a loading animation while it processes your input.

View Results: Once the analysis is complete, you'll see your detected mood along with a list of personalized songs, a book tip, and a puzzle recommendation.

Track Progress: Use the orange sidebar to view your Mood Timeline and the Puzzle Leaderboard.

🎨 UI/UX Design
The application's design is optimized for a modern, high-energy feel. Key design choices include:

Dark Theme: A radial dark blue and purple gradient background for an immersive, futuristic look.

Vibrant Accents: Electric orange buttons and glowing hover effects draw the user's attention to key interactive elements.

Lottie Animations: Custom animations are used to indicate loading states and celebrate user achievements, providing a more engaging experience than static spinners.

Responsive Layout: The UI is designed to look great on both desktop and mobile devices.

Feel free to customize the CSS styles and animations to give the app your personal touch!
