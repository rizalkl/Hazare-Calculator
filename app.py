import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from functions_hazare import *

# Set page config
st.set_page_config(page_title="Kushal's Hazare Calculator", layout="wide")

# Custom styling
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    .bold-font {
        font-weight: bold;
    }
    .score-input {
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎲 Kushal's Hazare Calculator")

# Layout with two columns
col1, col2 = st.columns([3, 1])

# Calculator and inputs in the first column (col1)
with col1:
    with st.sidebar:
        st.markdown("## 📋 Enter Player Names to Start Playing")
        player_names_input = st.text_area("Player names (comma-separated):", height=100)
        submit_names = st.button("Submit Names")

    if submit_names:
        st.session_state.player_names = [name.strip() for name in player_names_input.split(',') if name.strip()]

    if 'player_names' in st.session_state:
        st.markdown("## 📝 Enter Scores for Each Player")
        scores_inputs = {player: st.text_input(f"{player}'s Scores (comma-separated)", key=player).split(',') for player in st.session_state.player_names}
        if st.button("🏆 Calculate Scores", key='calculate_scores'):
            try:
                validated_scores = [validate_scores(scores_inputs[player]) for player in st.session_state.player_names]
                scores_df = check_winner(st.session_state.player_names, validated_scores)
                st.markdown("## 📊 Total Scores")
                st.dataframe(scores_df.style.apply(lambda x: ['background-color: lightgreen' if x.name == 'Total' else '' for i in x]))
                st.pyplot(plot_scores(scores_df))
            except Exception as e:
                st.error(f"Error: {e}")
with col2:
    # Expander for game rules and descriptions
    with st.expander("📘 View Game Rules and Descriptions", expanded=False):
        st.markdown("### 📖 Game Rules")
        st.markdown('''Hazare is a Nepali card game. Players divide their hands of 13 cards into sets of 3, 3, 3 and 4 which are compared in a similar way to hands at Brag or Teen Patti. However, unlike these other games, Hazari is played for points, each card having a point value. The winner of each comparison collects the played cards, and scores their point value. Hazari means 1000 and the aim of the game is to accumulate a score of 1000 points or more.''')

        st.markdown("### 🎴 Card Combinations")
        st.markdown('''The game of Hazare is based on comparing 3-card combinations using a standard international 52-card pack.The rank of cards in each suit, from highest to lowest, is A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2.The Aces, Kings, Queens, Jacks and Tens are worth 10 points each, and the numeral cards from 2 to 9 are worth 5 points each. The total value of the cards in the pack is 360. Deal and play are counter-clockwise.''')

        st.markdown("### 🃏 Scoring")
        st.markdown('''Each player counts up the value of the cards they have collected (the grand total for all 4 players must be 360), and adds this to their cumulative score. Then if no one has reached 1000, the cards are shuffled and dealt by the next dealer and the game continues.The game ends when one or more players has a score of 1000 points or more. The player with the highest total then wins.''')
