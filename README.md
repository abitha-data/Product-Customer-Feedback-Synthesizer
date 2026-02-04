## 🛒 Product Customer Feedback Synthesizer

An AI-powered web application that analyzes customer reviews and generates clear, buyer-friendly insights to help users make confident purchase decisions.

### 📌 Project Overview

Before purchasing products online, users often read reviews from multiple platforms.
However, this process is:

Time-consuming

Scattered across sources

Influenced by extreme opinions

Difficult to summarize into actionable insights

This project solves that problem by using NLP-based sentiment analysis to synthesize customer feedback into structured insights such as overall sentiment, common complaints, and buyer recommendations.

### 🎯 Key Features

Accepts free-text user input (no dropdown dependency)

Works even if exact product match is not found

Automatically performs:

Sentiment analysis (Positive / Neutral / Negative)

Star rating inference

Buyer recommendation generation

Clean, intuitive Streamlit UI

Uses CSV-based offline dataset (safe for evaluation)

### 🧠 Tech Stack Used

| Layer         | Technology                       |
| ------------- | -------------------------------- |
| Frontend      | Streamlit                        |
| Backend       | Python                           |
| NLP           | TextBlob                         |
| Data Handling | Pandas                           |
| Dataset       | CSV (preloaded customer reviews) |
| Deployment    | Streamlit Cloud (recommended)    |
