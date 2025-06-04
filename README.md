
# Financial Chatbot Prototype

## Overview
This chatbot answers predefined financial questions using data from the 10-K filings of Microsoft, Apple, and Tesla.

## How to Run
1. Ensure you have Python 3 installed.
2. Place `chatbot.py` and `10K.csv` in the same folder.
3. In your terminal or command prompt, run:
   python chatbot.py

4. The chatbot will ask for your name and respond to queries like:
   - What is Tesla’s revenue?
   - How has Apple’s net income changed?
   - Show Microsoft’s performance
   - What is the total revenue?

5. Type `exit` to end the chat.

## Functionality
- Reads the latest 10-K financials from `10K.csv`
- Supports company-specific and general financial queries
- Responds to 5+ variations of revenue/income/performance questions

## Limitations
- Only responds to predefined, keyword-based queries
- Does not support natural language processing (NLP)
- Only provides financial data for the most recent year (2024)

This is a prototype and does not represent a full AI chatbot with machine learning capabilities.
