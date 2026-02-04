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

### 📌 Problem Statement

Customers often read reviews from multiple platforms before purchasing a product. This process is:

Time-consuming

Fragmented across sources

Biased due to extreme opinions

Difficult to summarize into actionable insights

This application synthesizes customer feedback and provides clear, structured, buyer-centric insights to support better purchase decisions.

### ⚙️ Features

Publicly accessible web application

User can:

Enter Product Name

Enter Product URL

Enter Review Date

Automatically generates:

Sentiment (Positive / Neutral / Negative)

Star ratings (1–5)

Common complaints

Buyer recommendation

Displays review details in tabular format

### 🧾 Dataset


| Column Name    | Description          |
| -------------- | -------------------- |
| `product_name` | Name of the product  |
| `product_url`  | Product link         |
| `brand`        | Brand name           |
| `review`       | Customer review text |
| `review_date`  | Date of the review   |



### 🧠 Tech Stack Used

| Layer         | Technology                       |
| ------------- | -------------------------------- |
| Frontend      | Streamlit                        |
| Backend       | Python                           |
| NLP           | TextBlob                         |
| Data Handling | Pandas                           |
| Dataset       | CSV (preloaded customer reviews) |
| Deployment    | Streamlit Cloud (recommended)    |

### 🖥️ Application Flow

User enters:

Product name

Brand name

Product URL (optional)

Review date (optional)

Application searches for relevant reviews using smart fallback logic:

Product + Brand + Date

Product + Brand

Brand only

NLP sentiment analysis is applied

Buyer-centric insights are generated

Results are displayed instantly

### 🚀 Deployment Details

Deployed using Streamlit Cloud

Accessible via a public URL

No login or installation required

Judges can test directly from a browser

### 🎯 Key Features

Accepts free-text user input (no dropdown dependency)

Works even if exact product match is not found

Automatically performs:

Sentiment analysis (Positive / Neutral / Negative)

Star rating inference

Buyer recommendation generation

Clean, intuitive Streamlit UI

Uses CSV-based offline dataset (safe for evaluation)

### ▶️ How to Run Locally

1️⃣ Install dependencies

        pip install streamlit pandas textblob

2️⃣ Run the app
          
       streamlit run app.py

3️⃣ Open in browser 

      http://localhost:8501

### 📁 Project Folder Structure

       
product-feedback-synthesizer/
│
├── app.py              # Streamlit main app
├── data/
│   └── reviews.csv     # Review dataset
├── requirements.txt    # Dependencies
├── README.md           # Project details
└── .gitignore          # Ignore temp files
