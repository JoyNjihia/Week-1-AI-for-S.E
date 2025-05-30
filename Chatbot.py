
# 🌟 JoyaBot: Your Calm and Conscious Crypto Advisor 💫

# Predefined Crypto Dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    },
    "Celo": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7.5/10
    }
}

# 👋 Chatbot Intro
print("Karibu! 🌸 I’m JoyaBot — your calm and conscious crypto sidekick! 💫")
print("Ask me anything about trending or sustainable cryptocurrencies. Let’s grow your financial garden. 🌿💰\n")

# 🧠 Chatbot Loop
while True:
    user_query = input("You: ").lower()

    if "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"JoyaBot 💹: These coins are trending up: {', '.join(trending)}! 🚀\n")

    elif "sustainable" in user_query or "eco" in user_query:
        sustainable = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"JoyaBot 🌱: {sustainable} is the most eco-friendly coin! Good for the planet 🌍 and your portfolio.\n")

    elif "long-term" in user_query or "growth" in user_query:
        recommended = [
            coin for coin in crypto_db
            if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 7/10
        ]
        if recommended:
            print(f"JoyaBot 🚀: Consider {recommended[0]} for long-term growth — it's trending up and planet-friendly! 🌎💸\n")
        else:
            print("JoyaBot 🤔: No ideal long-term coin found right now. Try again later.\n")

    elif "cheap" in user_query or "affordable" in user_query:
        affordable = [coin for coin in crypto_db if crypto_db[coin]["market_cap"] == "medium"]
        if affordable:
            print(f"JoyaBot 💰: On a budget? You might want to look at {affordable[0]} — it’s affordable and promising! 🌟\n")

    elif "bye" in user_query or "exit" in user_query:
        print("JoyaBot 👋: Asante for chatting with me! Stay wise, stay sustainable. 🌺 Kwaheri!\n")
        break

    else:
        print("JoyaBot 🤖: Samahani, I didn’t catch that. Try asking about ‘trending’, ‘sustainable’, or ‘growth’ cryptos.\n")
