
# Financial Chatbot Prototype

## Overview
This is a simplified AI-powered chatbot designed to answer predefined financial queries using data from the 10-K filings of Microsoft, Apple, and Tesla.

The chatbot provides quick responses to revenue, net income, and growth-related questions based on the most recent financial data (2024), helping users interact with structured financial insights.

---

## How to Run

1. Ensure you have **Python 3.x** installed on your system.
2. Place `chatbot.py` and `Processed_Financials.csv` in the same directory.
3. Open a terminal in that directory and run:

```bash
python chatbot.py
```

4. The chatbot will ask for your name and then allow you to ask financial questions.
5. Type `"exit"` when you're done chatting.

---

## Supported Queries (Examples)

You can ask:

- "What is the total revenue?"
- "What is Tesla's net income?"
- "Show Apple’s performance summary"
- "How has Microsoft’s revenue changed?"
- "What is the revenue growth?"
- "Tell me about the most recent financial year"
- "Give me the net income growth of Tesla"
- "What year is this financial data from?"

---

## Functionality

- Responds to both **general** and **company-specific** financial questions.
- Uses structured `Processed_Financials.csv` data to return:
  - Total Revenue
  - Net Income
  - Revenue Growth (%)
  - Net Income Growth (%)
  - Performance summary by company
- Friendly user interaction: greets user by name and exits politely.

---

## Limitations

- Only supports **predefined financial queries** (no NLP).
- Based on **static financial data** from 2024.
- Cannot process real-time or external inputs.
- Prototype implementation only; not intended for production use.

---

## Author
This chatbot was developed as part of a BCG X simulation project on AI-driven financial insights.
