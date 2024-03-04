# Hazare-Calculator
Hazare is a Nepali card game. Players divide their hands of 13 cards into sets of 3, 3, 3 and 4 which are compared in a similar way to hands at Brag or Teen Patti. However, unlike these other games, Hazari is played for points, each card having a point value. The winner of each comparison collects the played cards, and scores their point value. Hazari means 1000 and the aim of the game is to accumulate a score of 1000 points or more. 

Title: Kushal's Hazare Calculator - Streamlit App Design Document

Author: Kushal Rizal

Date: 03-01-2024

1. Overview

Brief Description: A Streamlit-based web application designed to calculate scores for the Hazare card game.
Purpose: To provide an easy-to-use interface for players to track scores in the Hazare game and determine the winner.

2. Features

Player Name Input: Users can enter the names of players.
Score Input: Dynamic input fields for entering scores for each player.
Score Calculation: Calculates total scores, checks for invalid rounds, and determines if a winner has been reached.
Interactive Scoreboard: Displays total scores in a table format.
Game Rules: An expandable section that outlines the rules of Hazare.
Responsive Design: Adjusts layout based on the number of players.

3. User Interface Design

Layout: Two-column layout with score inputs on the left and game rules on the right.
Sidebar: Used for entering player names.
Main Area:
Score Inputs: Text fields for each player's scores.
Calculate Button: To trigger score calculation.
Score Display: Dataframe/table to show the calculated scores.
Game Rules: Expander on the right column with detailed game rules.

4. Technology Stack

Frontend: Streamlit
Backend: Python
Libraries: pandas for data manipulation, matplotlib for plotting.

5. Implementation Details

Functions:
check_winner: For calculating total scores and determining the winner.
validate_scores: For validating score inputs.
plot_scores: For creating a bar chart of scores.
Error Handling: User-friendly error messages for invalid inputs.
Session State: To remember the state of the app (entered scores and player names).

6. Future Enhancements

Interactive Chart: Implementing Plotly or Altair for interactive score visualization.
Mobile Optimization: Ensuring usability on mobile devices.
User Feedback: Adding a mechanism for user feedback.
Historical Scoreboard: Tracking scores over multiple games.
7. Notes

The app is designed to be intuitive and user-friendly, catering to both new and experienced players of Hazare.
Regular updates and refinements to be made based on user feedback.

