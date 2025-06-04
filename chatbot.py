
import pandas as pd

# Load and prepare data
df = pd.read_csv('10K_Processed.csv')
df = df.sort_values(by=['Company', 'Year'])
df['Revenue Growth (%)'] = df.groupby('Company')['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby('Company')['Net Income'].pct_change() * 100

# Latest year metrics
latest_df = df.groupby('Company').tail(1).round(2)
latest_data = latest_df.set_index('Company').to_dict(orient='index')
companies = [company.lower() for company in latest_data.keys()]

# Chatbot logic
def financial_chatbot(query):
    query = query.lower()

    # Company-specific questions
    for company in companies:
        if company in query:
            data = latest_data[company.capitalize()]
            if "revenue" in query and "growth" in query:
                return f"{company.capitalize()} revenue grew {data['Revenue Growth (%)']:.2f}% in {int(data['Year'])}."
            elif "revenue" in query:
                return f"{company.capitalize()} total revenue was ${data['Total Revenue']}M in {int(data['Year'])}."
            elif "net income" in query and "growth" in query:
                return f"{company.capitalize()} net income changed {data['Net Income Growth (%)']:.2f}% in {int(data['Year'])}."
            elif "net income" in query:
                return f"{company.capitalize()} net income was ${data['Net Income']}M in {int(data['Year'])}."
            elif "summary" in query or "performance" in query:
                return (
                    f"{company.capitalize()} ({int(data['Year'])})\n"
                    f"- Revenue: ${data['Total Revenue']}M\n"
                    f"- Net Income: ${data['Net Income']}M\n"
                    f"- Revenue Growth: {data['Revenue Growth (%)']:.2f}%\n"
                    f"- Net Income Growth: {data['Net Income Growth (%)']:.2f}%"
                )

    # General queries
    if "total revenue" in query:
        return "\n".join([
            f"{comp}: ${info['Total Revenue']}M in {int(info['Year'])}"
            for comp, info in latest_data.items()
        ])
    elif "net income" in query and "growth" not in query:
        return "\n".join([
            f"{comp}: ${info['Net Income']}M in {int(info['Year'])}"
            for comp, info in latest_data.items()
        ])
    elif "revenue growth" in query:
        return "\n".join([
            f"{comp}: {info['Revenue Growth (%)']:.2f}% in {int(info['Year'])}"
            for comp, info in latest_data.items()
        ])
    elif "net income growth" in query:
        return "\n".join([
            f"{comp}: {info['Net Income Growth (%)']:.2f}% in {int(info['Year'])}"
            for comp, info in latest_data.items()
        ])
    elif "latest year" in query or "most recent year" in query:
        return "The most recent financial year in the dataset is 2024."
    else:
        return (
            "Sorry, I can only answer questions related to:\n"
            "- Revenue, Net Income, or their Growth\n"
            "- Specific companies (Apple, Microsoft, Tesla)\n"
            "- Performance summaries\n"
            "Please rephrase your query or mention a company."
        )

# Main chatbot loop
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot Prototype!")
    name = input("Hi there! What’s your name? ")
    print(f"\nNice to meet you, {name}! You can now ask me questions about Microsoft, Apple, or Tesla's finances.")
    print("Type your question below. Type 'exit' when you're done.\n")

    while True:
        user_input = input(f"{name}: ")
        if user_input.lower() in ['exit', 'quit']:
            print(f"\nGoodbye, {name}! Thanks for chatting with the Financial Bot.")
            break
        response = financial_chatbot(user_input)
        print("Bot:", response)
