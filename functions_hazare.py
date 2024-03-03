import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Function to check the winner and calculate scores
def check_winner(players, scores):
    players_scores = dict(zip(players, scores))

    # Create a DataFrame to store the recorded scores for all players
    df_scores = pd.DataFrame(players_scores)

    # Calculate the total scores for each player and add them to the DataFrame
    df_scores.loc['Total'] = df_scores.sum()

    # Determine the highest total score and the winner
    highest_score = df_scores.loc['Total'].max()
    winner = df_scores.loc['Total'].idxmax()

    # Check if any round does not sum to 360
    df_scores['Total_each_round'] = df_scores.drop('Total', axis=0).sum(axis=1)
    invalid_rounds = df_scores[df_scores['Total_each_round'] != 360].index[:-1]

    if len(invalid_rounds) > 0:
        st.warning(f"Warning: Row(s) {', '.join(map(str, invalid_rounds))} do not sum up to 360. They must equal 360.")

    if highest_score < 1000:
        points_away = 1000 - highest_score
        st.write(f"No winner yet. The highest score is {winner} with {highest_score} points, {points_away} points away from 1000. Aba sabai milera rokney ho!")
    else:
        st.success(f"The winner is: Player {winner}. Dherai Dherai Badhai Cha Hamro Paisa Jeeteko Ma.")

    return df_scores

# Function to validate scores input
def validate_scores(scores):
    try:
        return [int(score) for score in scores if score]
    except ValueError:
        raise ValueError("Please enter valid integer scores.")

# Function to plot the bar chart
def plot_scores(scores_df):
    last_row_first_five_columns = scores_df.iloc[-1:].iloc[:, :5]
    ax = last_row_first_five_columns.T.plot(kind='bar', legend=False, figsize=(8, 5), color='moccasin', edgecolor='black')
    for i, value in enumerate(last_row_first_five_columns.values[0]):
        ax.text(i, value, str(value), ha='center', va='bottom', fontsize=12, fontweight='bold')
    plt.title('Total Scores for the Last Round')
    plt.ylabel('Total Score')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return plt