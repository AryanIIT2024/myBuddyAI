import streamlit as st
from datetime import datetime
import pandas as pd
from emotion_analysis import get_emotion
from spotify_recommender import get_tracks_for_emotion
from deepseek_recommender import get_book_tip  # ✅ NEW IMPORT
from puzzle_recommender import get_puzzle_for_mood

st.title("🧠 FeelBuddy: Your AI partner 😊")

user_input = st.text_area("How are you feeling today?")

if st.button("Analyze Mood & Recommend Songs"):
    if user_input:
        with st.spinner("Analyzing mood..."):
            mood, confidence = get_emotion(user_input)
            st.success(f"Detected Mood: {mood} ({confidence*100:.1f}%)")

            # 🎶 SONG RECOMMENDATIONS
            st.markdown("### 🎶 Recommended Songs")
            tracks = get_tracks_for_emotion(mood)
            for track in tracks:
                st.markdown(f"- [{track['name']} by {track['artist']}]({track['url']})")

            # 📚 BOOK RECOMMENDATIONS (static)
            # st.markdown("### 📚 Recommended Books")
            try:
                books = pd.read_csv("books.csv")
                mood_books = books[books["mood"] == mood].to_dict("records")
                for book in mood_books:
                    st.markdown(f"- **{book['title']}** by *{book['author']}*")
            except:
                st.info("Book recommendation list not found.")

            # 🤖 GEMINI-BASED BOOK SUGGESTION
            st.markdown("### 📚 Recommended Books")
            book_tip = get_book_tip(mood)
            st.info(book_tip)

            # 📝 SAVE TO JOURNAL
            new_entry = {"date": datetime.now(), "text": user_input, "mood": mood}
            try:
                df = pd.read_csv("mood_data.csv")
                df = df.append(new_entry, ignore_index=True)
            except:
                df = pd.DataFrame([new_entry])
            df.to_csv("mood_data.csv", index=False)
                        # 🧩 PUZZLE RECOMMENDATION
            st.markdown("### 🧩 Puzzle for Your Mood")
            puzzle_link = get_puzzle_for_mood(mood)
            st.markdown(f"[Click here to play your puzzle]({puzzle_link})")

            # 🔥 STREAK TRACKER
            user = "User"  # Replace with real user if implementing login
            today = datetime.now().date()

            try:
                df_streak = pd.read_csv("streak_data.csv")
            except:
                df_streak = pd.DataFrame(columns=["user", "date"])

            # Check if today's puzzle already played
            already_played = ((df_streak["user"] == user) & (df_streak["date"] == str(today))).any()

            if not already_played:
                df_streak = pd.concat([df_streak, pd.DataFrame([{"user": user, "date": str(today)}])], ignore_index=True)
                df_streak.to_csv("streak_data.csv", index=False)
                st.success("🎉 Puzzle logged! Your streak continues!")

            # Show current streak
            user_data = df_streak[df_streak["user"] == user]
            streak = user_data["date"].nunique()
            st.markdown(f"🔥 **Current Streak:** {streak} days")

            # 🏆 LEADERBOARD
            st.markdown("### 🏆 Puzzle Leaderboard")
            leaderboard = df_streak.groupby("user")["date"].nunique().reset_index()
            leaderboard.columns = ["User", "Streak (Days)"]
            leaderboard = leaderboard.sort_values("Streak (Days)", ascending=False)
            st.dataframe(leaderboard)



# 📈 Mood Timeline
st.markdown("---")
st.markdown("### 🕒 Mood Timeline")
try:
    df = pd.read_csv("mood_data.csv")
    st.dataframe(df)
except:
    st.info("No past entries yet. Start journaling!")

