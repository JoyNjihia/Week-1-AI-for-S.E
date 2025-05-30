# Week-1-AI-for-S.E

# 💫 JoyaBot – Your Calm & Conscious Crypto Advisor

### Theme: "Your First AI-Powered Financial Sidekick!" 🌟

---

## 👋 Introduction

**JoyaBot** is a rule-based chatbot built using Python. It offers crypto investment advice with a strong focus on both **profitability** and **sustainability**.
Whether you're curious about trending coins or want eco-friendly options, JoyaBot is your kind and conscious financial sidekick. 🌿

---

## 💡 Features

✅ Answers questions about:
- Trending cryptocurrencies 📈  
- The most sustainable crypto projects 🌱  
- Coins for long-term growth 🚀  
- Affordable crypto options 💰  

✅ Custom conversation tone: Friendly + Swahili warmth 🇰🇪  
✅ Simple if-else logic for decision-making  
✅ Personalized for the PLP Week 1 Assignment  

---

## 🛠️ Tools Used

- **Language:** Python  
- **IDE:** Google Colab / Jupyter Notebook  
- **Libraries:** None needed – pure Python logic  
- **Data:** Predefined dictionary with sample crypto info  

---

## 🧠 How It Works

JoyaBot uses `if-else` rules to interpret user queries and respond accordingly. It checks for key terms like `trending`, `sustainable`, `growth`, or `affordable`,
then fetches insights from a small dataset of coins. It mimics decision-making like AI by using rule-based logic to make informed suggestions.

---

## 🔍 Sample Crypto Data

```python
crypto_db = {
    "Bitcoin": { "price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3/10 },
    "Ethereum": { "price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6/10 },
    "Cardano": { "price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8/10 },
    "Celo": { "price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 7.5/10 }
}
