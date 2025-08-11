# # import streamlit as st
# # from datetime import datetime
# # import pandas as pd
# # from emotion_analysis import get_emotion
# # from spotify_recommender import get_tracks_for_emotion
# # from deepseek_recommender import get_book_tip  # ✅ NEW IMPORT
# # from puzzle_recommender import get_puzzle_for_mood

# # st.title("🧠 FeelBuddy: Your AI partner 😊")

# # user_input = st.text_area("How are you feeling today?")

# # if st.button("Analyze Mood & Recommend Songs"):
# #     if user_input:
# #         with st.spinner("Analyzing mood..."):
# #             mood, confidence = get_emotion(user_input)
# #             st.success(f"Detected Mood: {mood} ({confidence*100:.1f}%)")

# #             # 🎶 SONG RECOMMENDATIONS
# #             st.markdown("### 🎶 Recommended Songs")
# #             tracks = get_tracks_for_emotion(mood)
# #             for track in tracks:
# #                 st.markdown(f"- [{track['name']} by {track['artist']}]({track['url']})")

# #             # 📚 BOOK RECOMMENDATIONS (static)
# #             # st.markdown("### 📚 Recommended Books")
# #             try:
# #                 books = pd.read_csv("books.csv")
# #                 mood_books = books[books["mood"] == mood].to_dict("records")
# #                 for book in mood_books:
# #                     st.markdown(f"- **{book['title']}** by *{book['author']}*")
# #             except:
# #                 st.info("Book recommendation list not found.")

# #             # 🤖 GEMINI-BASED BOOK SUGGESTION
# #             st.markdown("### 📚 Recommended Books")
# #             book_tip = get_book_tip(mood)
# #             st.info(book_tip)

# #             # 📝 SAVE TO JOURNAL
# #             new_entry = {"date": datetime.now(), "text": user_input, "mood": mood}
# #             try:
# #                 df = pd.read_csv("mood_data.csv")
# #                 df = df.append(new_entry, ignore_index=True)
# #             except:
# #                 df = pd.DataFrame([new_entry])
# #             df.to_csv("mood_data.csv", index=False)
# #                         # 🧩 PUZZLE RECOMMENDATION
# #             st.markdown("### 🧩 Puzzle for Your Mood")
# #             puzzle_link = get_puzzle_for_mood(mood)
# #             st.markdown(f"[Click here to play your puzzle]({puzzle_link})")

# #             # 🔥 STREAK TRACKER
# #             user = "User"  # Replace with real user if implementing login
# #             today = datetime.now().date()

# #             try:
# #                 df_streak = pd.read_csv("streak_data.csv")
# #             except:
# #                 df_streak = pd.DataFrame(columns=["user", "date"])

# #             # Check if today's puzzle already played
# #             already_played = ((df_streak["user"] == user) & (df_streak["date"] == str(today))).any()

# #             if not already_played:
# #                 df_streak = pd.concat([df_streak, pd.DataFrame([{"user": user, "date": str(today)}])], ignore_index=True)
# #                 df_streak.to_csv("streak_data.csv", index=False)
# #                 st.success("🎉 Puzzle logged! Your streak continues!")

# #             # Show current streak
# #             user_data = df_streak[df_streak["user"] == user]
# #             streak = user_data["date"].nunique()
# #             st.markdown(f"🔥 **Current Streak:** {streak} days")

# #             # 🏆 LEADERBOARD
# #             st.markdown("### 🏆 Puzzle Leaderboard")
# #             leaderboard = df_streak.groupby("user")["date"].nunique().reset_index()
# #             leaderboard.columns = ["User", "Streak (Days)"]
# #             leaderboard = leaderboard.sort_values("Streak (Days)", ascending=False)
# #             st.dataframe(leaderboard)



# # # # # 📈 Mood Timeline
# # # # st.markdown("---")
# # # # st.markdown("### 🕒 Mood Timeline")
# # # # try:
# # # #     df = pd.read_csv("mood_data.csv")
# # # #     st.dataframe(df)
# # # # except:
# # # #     st.info("No past entries yet. Start journaling!")
# # # import streamlit as st
# # # from datetime import datetime
# # # import pandas as pd
# # # import requests
# # # from streamlit_lottie import st_lottie

# # # # --- IMPORTS for your app's core logic ---
# # # from emotion_analysis import get_emotion
# # # from spotify_recommender import get_tracks_for_emotion
# # # from deepseek_recommender import get_book_tip
# # # from puzzle_recommender import get_puzzle_for_mood

# # # # --- Custom CSS for a modern, hackathon-style look ---
# # # st.markdown(
# # #     """
# # #     <style>
# # #     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    
# # #     html, body, .main {
# # #         font-family: 'Poppins', sans-serif;
# # #     }
    
# # #     .main {
# # #         background: radial-gradient(circle, #2c0f4f 0%, #0a0a2a 100%);
# # #         padding: 2rem;
# # #     }
# # #     h1, h2, h3, h4, h5, h6, .st-b5, .st-c7 {
# # #         color: #b0e0e6;
# # #         font-weight: 600;
# # #     }
# # #     .stButton>button {
# # #         background-color: #FF8C00; /* Vibrant orange */
# # #         color: #1a237e; /* Dark blue text */
# # #         font-weight: bold;
# # #         border-radius: 12px;
# # #         border: none;
# # #         padding: 12px 28px;
# # #         transition: all 0.3s ease-in-out;
# # #         box-shadow: 0 0 10px #FF8C00, 0 0 20px #FF8C00;
# # #         font-size: 1rem;
# # #     }
# # #     .stButton>button:hover {
# # #         background-color: #e67e22;
# # #         transform: translateY(-2px);
# # #         box-shadow: 0 0 15px #FF8C00, 0 0 25px #FF8C00;
# # #     }
# # #     .stTextArea label {
# # #         color: #b0e0e6;
# # #         font-weight: 600;
# # #         font-size: 1.1rem;
# # #     }
# # #     .stTextArea textarea {
# # #         background-color: #000000; /* Black background for input */
# # #         color: #ffffff; /* White text color */
# # #         border-radius: 12px;
# # #         border: 2px solid #5c6bc0;
# # #         box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
# # #         padding: 12px;
# # #         transition: all 0.3s ease-in-out;
# # #     }
# # #     .stTextArea textarea:focus {
# # #         border-color: #FF8C00;
# # #         box-shadow: 0 0 0 3px rgba(255, 140, 0, 0.5), inset 0 2px 4px rgba(0, 0, 0, 0.1);
# # #     }
# # #     .stExpander, .stDataFrame, .stInfo, .stSuccess, .stWarning {
# # #         border-radius: 12px;
# # #         padding: 1rem;
# # #         margin-bottom: 1rem;
# # #         box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
# # #         background-color: #ff9900; /* Semi-transparent dark purple */
# # #     }
# # #     .stSuccess {
# # #         color: #90caf9;
# # #         border-left: 5px solid #00ff00;
# # #     }
# # #     .stInfo {
# # #         color: #90caf9;
# # #         border-left: 5px solid #2196f3;
# # #     }
# # #     .stWarning {
# # #         color: #ffb74d;
# # #         border-left: 5px solid #ff9800;
# # #     }
# # #     .header-container {
# # #         display: flex;
# # #         align-items: center;
# # #         justify-content: center;
# # #         gap: 1rem;
# # #         padding: 1rem;
# # #     }
# # #     .block-container {
# # #         padding-top: 1rem;
# # #     }
# # #     .sidebar .sidebar-content {
# # #         background-color: #FF8C00; /* Vibrant orange for the sidebar */
# # #         box-shadow: 0 0 15px rgba(255, 140, 0, 0.4);
# # #     }
# # #     .sidebar-header {
# # #         display: flex;
# # #         align-items: center;
# # #         gap: 1rem;
# # #         padding: 1rem 1rem 0 1rem;
# # #     }
# # #     .sidebar-header h2 {
# # #         color: #1a237e !important;
# # #         font-weight: 700;
# # #         text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
# # #     }
# # #     .sidebar .st-eb {
# # #         color: #1a237e !important; /* Orange sidebar header text */
# # #     }
# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True
# # # )

# # # # --- Helper function for loading Lottie animations ---
# # # def load_lottieurl(url: str):
# # #     """Fetches a Lottie animation from a URL."""
# # #     try:
# # #         r = requests.get(url, timeout=5)
# # #         if r.status_code == 200:
# # #             return r.json()
# # #         return None
# # #     except requests.exceptions.RequestException:
# # #         return None

# # # # Load Lottie animations from public URLs
# # # lottie_brain_scan = load_lottieurl("https://lottie.host/80a06801-b3b0-449e-b700-0e12360f7798/n5x6V2oP5Q.json")
# # # lottie_welcome = load_lottieurl("https://lottie.host/8340d892-749e-4e6c-a579-a78b5e28a5ec/808l0y1z69.json")
# # # lottie_party = load_lottieurl("https://lottie.host/54045f44-6a0b-411a-8c74-c37667a42c4b/O8c0eYd6hQ.json")
# # # lottie_streak = load_lottieurl("https://lottie.host/9892c577-980b-4eb1-b25b-010b42f65a44/5z94c25f4Q.json")
# # # lottie_dashboard = load_lottieurl("https://lottie.host/a823e481-f763-47a3-b6d4-d53b53f60b93/o48s4hO2cW.json")


# # # # --- Set Page Config (must be the first Streamlit command) ---
# # # st.set_page_config(
# # #     page_title="FeelBuddy",
# # #     page_icon="🧠",
# # #     layout="centered"
# # # )

# # # # --- Header Section with Logo and Title (Centered) ---
# # # with st.container():
# # #     st.markdown("<div class='header-container'>", unsafe_allow_html=True)
# # #     if lottie_welcome:
# # #         st_lottie(lottie_welcome, height=100, key="welcome_animation")
# # #     st.markdown("<h1 style='color: #b0e0e6; margin: 0;'>🧠 FeelBuddy: Your AI Partner 😊</h1>", unsafe_allow_html=True)
# # #     st.markdown("</div>", unsafe_allow_html=True)

# # # # --- Main Interaction Area ---
# # # st.markdown("---")
# # # st.header("How are you feeling today?")
# # # user_input = st.text_area(
# # #     "Share your thoughts and feelings here...",
# # #     placeholder="e.g., 'I had a really good day, I feel so energized and happy!'",
# # #     height=150
# # # )

# # # if st.button("Analyze Mood & Get Recommendations", use_container_width=True):
# # #     if user_input:
# # #         # Use a custom animated spinner
# # #         with st.container():
# # #             st.markdown("### Analyzing your mood... 🚀")
# # #             if lottie_brain_scan:
# # #                 st_lottie(lottie_brain_scan, height=200, key="brain_scan_animation")

# # #             # --- Original analysis logic ---
# # #             mood, confidence = get_emotion(user_input)

# # #             mood_emojis = {"joy": "😊", "sadness": "😢", "anger": "😡", "fear": "😨", "surprise": "😮"}
# # #             st.success(f"**Detected Mood: {mood.capitalize()} {mood_emojis.get(mood, '')}** (Confidence: {confidence*100:.1f}%)")

# # #             # --- Recommendations Section using columns ---
# # #             st.markdown("---")
# # #             st.subheader("Your Personalized Recommendations")
            
# # #             rec_col1, rec_col2 = st.columns(2)

# # #             with rec_col1:
# # #                 st.markdown("### 🎶 Recommended Songs")
# # #                 tracks = get_tracks_for_emotion(mood)
# # #                 for track in tracks:
# # #                     # Safely check for the keys before creating the links
# # #                     if 'name' in track and 'artist' in track and 'url' in track:
# # #                         web_link = f"[{track['name']}]({track['url']})"
# # #                         app_link = ""
# # #                         if 'uri' in track:
# # #                             app_link = f" ( [Open in Spotify App]({track['uri']}) )"
# # #                         st.markdown(f"- **{web_link}** by *{track['artist']}*{app_link}")

# # #             with rec_col2:
# # #                 st.markdown("### 📚 Recommended Books")
# # #                 book_tip = get_book_tip(mood)
# # #                 st.info(book_tip)
            
# # #             st.markdown("---")

# # #             # --- Puzzle and Streak Tracker ---
# # #             st.markdown("### 🧩 Your Daily Puzzle & Streak")
# # #             puzzle_col, streak_col = st.columns([2, 1])
# # #             with puzzle_col:
# # #                 puzzle_link = get_puzzle_for_mood(mood)
# # #                 st.markdown(f"**Feeling focused?** [Click here to play your puzzle]({puzzle_link})")
            
# # #             with streak_col:
# # #                 # 🔥 STREAK TRACKER
# # #                 user = "User"  # Replace with real user if implementing login
# # #                 today = datetime.now().date()

# # #                 try:
# # #                     df_streak = pd.read_csv("streak_data.csv")
# # #                 except:
# # #                     df_streak = pd.DataFrame(columns=["user", "date"])

# # #                 # Check if today's puzzle already played
# # #                 already_played = ((df_streak["user"] == user) & (df_streak["date"] == str(today))).any()

# # #                 if not already_played:
# # #                     df_streak = pd.concat([df_streak, pd.DataFrame([{"user": user, "date": str(today)}])], ignore_index=True)
# # #                     df_streak.to_csv("streak_data.csv", index=False)
# # #                     with st.expander("🎉 Streak Logged!", expanded=True):
# # #                          if lottie_streak:
# # #                              st_lottie(lottie_streak, height=100)

# # #                 # Show current streak
# # #                 user_data = df_streak[df_streak["user"] == user]
# # #                 streak = user_data["date"].nunique()
# # #                 st.markdown(f"🔥 **Current Streak:** {streak} days")
            
# # #             # Final success animation
# # #             if lottie_party:
# # #                 st_lottie(lottie_party, height=150, key="party_animation")

# # #     else:
# # #         st.warning("Please tell me how you're feeling first!")

# # # # --- Sidebar for additional content ---
# # # st.sidebar.markdown(f"<h2 style='color: #ff8c00;'>FeelBuddy Dashboard</h2>", unsafe_allow_html=True)
# # # st.sidebar.markdown(
# # #     """
# # #     <style>
# # #         .sidebar-header {
# # #             display: flex;
# # #             align-items: center;
# # #             gap: 1rem;
# # #             padding: 1rem 1rem 0 1rem;
# # #         }
# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True
# # # )

# # # st.sidebar.write("")
# # # st.sidebar.write("")
# # # if lottie_dashboard:
# # #     st.sidebar.markdown(
# # #         f"<div class='sidebar-header'>{st_lottie(lottie_dashboard, height=50, key='dashboard_animation')}</div>",
# # #         unsafe_allow_html=True
# # #     )

# # # # Mood Timeline
# # # with st.sidebar.expander("🕒 Mood Timeline", expanded=False):
# # #     # Your original code to read and display mood data
# # #     try:
# # #         df = pd.read_csv("mood_data.csv")
# # #         st.dataframe(df)
# # #     except:
# # #         st.info("No past entries yet. Start journaling!")

# # # # Leaderboard
# # # with st.sidebar.expander("🏆 Puzzle Leaderboard", expanded=False):
# # #     # Your original code to display leaderboard
# # #     try:
# # #         df_streak = pd.read_csv("streak_data.csv")
# # #         leaderboard = df_streak.groupby("user")["date"].nunique().reset_index()
# # #         leaderboard.columns = ["User", "Streak (Days)"]
# # #         leaderboard = leaderboard.sort_values("Streak (Days)", ascending=False)
# # #         st.dataframe(leaderboard)
# # #     except:
# # #         st.info("No leaderboard data yet.")

# # # st.sidebar.markdown("---")
# # # st.sidebar.info("Developed by team coding ninja's")
# import streamlit as st
# from datetime import datetime
# import pandas as pd
# from emotion_analysis import get_emotion
# from spotify_recommender import get_tracks_for_emotion
# from deepseek_recommender import get_book_tip  # ✅ NEW IMPORT
# from puzzle_recommender import get_puzzle_for_mood

# st.set_page_config(page_title="FeelBuddy", page_icon="🧠", layout="centered")

# st.title("🧠 FeelBuddy: Your AI partner 😊")

# user_input = st.text_area("How are you feeling today?")

# if st.button("Analyze Mood & Recommend Songs"):
#     if user_input:
#         with st.spinner("Analyzing mood..."):
#             mood, confidence = get_emotion(user_input)
#             st.success(f"Detected Mood: {mood} ({confidence*100:.1f}%)")

#             # 🎶 POSITIVE-ONLY SONG RECOMMENDATIONS
#             positive_mood_map = {
#                 "sad": "motivational",
#                 "fear": "spiritual",
#                 "angry": "calm",
#                 "happy": "radiant",
#                 "neutral": "happy"
#             }
#             positive_emotion = positive_mood_map.get(mood, "happy")

#             st.markdown("### 🎶 Recommended Songs")
#             tracks = get_tracks_for_emotion(positive_emotion)
#             if tracks:
#                 for track in tracks:
#                     st.markdown(f"- [{track['name']} by {track['artist']}]({track['url']})")
#             else:
#                 st.info("No songs found for this mood.")

           

#             # 🤖 AI-BASED BOOK SUGGESTION
#             st.markdown("### 📚 Recommended Books")
#             book_tip = get_book_tip(mood)
#             st.info(book_tip)

#             # 📝 SAVE TO JOURNAL
#             new_entry = {"date": datetime.now(), "text": user_input, "mood": mood}
#             try:
#                 df = pd.read_csv("mood_data.csv")
#                 df = df.append(new_entry, ignore_index=True)
#             except:
#                 df = pd.DataFrame([new_entry])
#             df.to_csv("mood_data.csv", index=False)

#             # 🧩 PUZZLE RECOMMENDATION
#             st.markdown("### 🧩 Puzzle for Your Mood")
#             puzzle_link = get_puzzle_for_mood(mood)
#             st.markdown(f"[Click here to play your puzzle]({puzzle_link})")

#             # 🔥 STREAK TRACKER
#             user = "User"  # Replace with actual username if login implemented
#             today = datetime.now().date()

#             try:
#                 df_streak = pd.read_csv("streak_data.csv")
#             except:
#                 df_streak = pd.DataFrame(columns=["user", "date"])

#             already_played = ((df_streak["user"] == user) & (df_streak["date"] == str(today))).any()

#             if not already_played:
#                 df_streak = pd.concat(
#                     [df_streak, pd.DataFrame([{"user": user, "date": str(today)}])],
#                     ignore_index=True
#                 )
#                 df_streak.to_csv("streak_data.csv", index=False)
#                 st.success("🎉 Puzzle logged! Your streak continues!")

#             # Show current streak
#             user_data = df_streak[df_streak["user"] == user]
#             streak = user_data["date"].nunique()
#             st.markdown(f"🔥 **Current Streak:** {streak} days")

#             # 🏆 LEADERBOARD
#             st.markdown("### 🏆 Puzzle Leaderboard")
#             leaderboard = df_streak.groupby("user")["date"].nunique().reset_index()
#             leaderboard.columns = ["User", "Streak (Days)"]
#             leaderboard = leaderboard.sort_values("Streak (Days)", ascending=False)
#             st.dataframe(leaderboard)

import streamlit as st
from datetime import datetime
import pandas as pd
from emotion_analysis import get_emotion
from spotify_recommender import get_tracks_for_emotion
from deepseek_recommender import get_book_tip
from puzzle_recommender import get_puzzle_for_mood

# ------------------ STREAMLIT CONFIG ------------------
st.set_page_config(page_title="FeelBuddy", page_icon="🧠", layout="centered")
st.title("🧠 FeelBuddy: Your AI Partner 😊")

# ------------------ USER INPUT ------------------
user_input = st.text_area("How are you feeling today?")

if st.button("Analyze Mood & Recommend Songs"):
    if user_input:
        with st.spinner("Analyzing mood..."):
            mood, confidence = get_emotion(user_input)
            st.success(f"Detected Mood: {mood} ({confidence*100:.1f}%)")

            # 🎶 SONG RECOMMENDATIONS (Positive Mood Version)
            st.markdown("### 🎶 Recommended Songs for Your Mood")
            tracks = get_tracks_for_emotion(mood)
            if tracks:
                for track in tracks:
                    st.markdown(f"- [{track['name']} by {track['artist']}]({track['url']})")
            else:
                st.info("No songs found for this mood.")

            # 📚 BOOK SUGGESTION
            st.markdown("### 📚 Recommended Books")
            book_tip = get_book_tip(mood)
            st.info(book_tip)

            # 📝 MOOD JOURNAL
            new_entry = {"date": datetime.now(), "text": user_input, "mood": mood}
            try:
                df = pd.read_csv("mood_data.csv")
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
            except FileNotFoundError:
                df = pd.DataFrame([new_entry])
            df.to_csv("mood_data.csv", index=False)

            # 🧩 PUZZLE RECOMMENDATION
            st.markdown("### 🧩 Puzzle for Your Mood")
            puzzle_link = get_puzzle_for_mood(mood)
            st.markdown(f"[Click here to play your puzzle]({puzzle_link})")

            # 🔥 STREAK TRACKER
            user = "User"  # Replace with actual username if login implemented
            today = datetime.now().date()
            try:
                df_streak = pd.read_csv("streak_data.csv")
            except FileNotFoundError:
                df_streak = pd.DataFrame(columns=["user", "date"])

            already_played = ((df_streak["user"] == user) & (df_streak["date"] == str(today))).any()
            if not already_played:
                df_streak = pd.concat(
                    [df_streak, pd.DataFrame([{"user": user, "date": str(today)}])],
                    ignore_index=True
                )
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
