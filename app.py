import streamlit as st
import pandas as pd
from textblob import TextBlob

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Product Customer Feedback Synthesizer",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Product Customer Feedback Synthesizer")
st.caption("AI-powered buyer-friendly review insights")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("reviews.csv")

    df["product_name"] = df["product_name"].fillna("").astype(str)
    df["product_url"] = df["product_url"].fillna("").astype(str)
    df["brand"] = df["brand"].fillna("").astype(str)
    df["review"] = df["review"].fillna("").astype(str)
    df["review_date"] = pd.to_datetime(df["review_date"], errors="coerce")

    return df

df = load_data()

# ---------------- USER INPUT ----------------
st.sidebar.header("📝 Enter Product Details")

product_input = st.sidebar.text_input("Product Name")
brand_input = st.sidebar.text_input("Brand")
url_input = st.sidebar.text_input("Product URL")
review_date_input = st.sidebar.date_input("Review Date", value=None)

# ---------------- SENTIMENT FUNCTION ----------------
def analyze_review(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive", 5
    elif polarity < -0.1:
        return "Negative", 2
    else:
        return "Neutral", 3

# ---------------- ANALYZE ----------------
if st.button("🚀 Analyze Reviews"):

    if not brand_input.strip():
        st.error("Please enter at least a Brand name.")
        st.stop()

    data = df.copy()

    # -------- SMART FALLBACK FILTERING --------

    # Product filter (only if provided)
    if product_input.strip():
        data = data[data["product_name"].str.lower().str.contains(product_input.lower(), na=False)]

    # Brand filter (mandatory)
    data = data[data["brand"].str.lower().str.contains(brand_input.lower(), na=False)]

    # Review date filter (optional)
    if review_date_input:
        data = data[data["review_date"] == pd.to_datetime(review_date_input)]

    # Final fallback: brand-only
    if data.empty:
        st.warning("No exact match found. Showing available brand reviews.")
        data = df[df["brand"].str.lower().str.contains(brand_input.lower(), na=False)]

    if data.empty:
        st.error("No reviews available for this brand.")
        st.stop()

    final_df = data.copy()

    # ---------------- SENTIMENT + STARS ----------------
    final_df[["sentiment", "stars"]] = final_df["review"].apply(
        lambda x: pd.Series(analyze_review(x))
    )

    # ---------------- OUTPUT ----------------
    st.subheader("📦 Product Summary")
    st.write(f"**Product Name:** {product_input if product_input else 'Multiple products'}")
    st.write(f"**Brand:** {brand_input}")
    if url_input:
        st.write(f"**Product URL:** {url_input}")
    if review_date_input:
        st.write(f"**Review Date:** {review_date_input}")

    # ---------------- OVERALL SENTIMENT ----------------
    st.subheader("📊 Overall Sentiment")
    st.bar_chart(final_df["sentiment"].value_counts(normalize=True) * 100)

    # ---------------- NEGATIVE ----------------
    st.subheader("👎 Common Complaints")
    negatives = final_df[final_df["sentiment"] == "Negative"]["review"].head(5)
    if negatives.empty:
        st.write("No major complaints found.")
    else:
        for r in negatives:
            st.write("•", r)

    # ---------------- BUYER RECOMMENDATION ----------------
    st.subheader("💡 Buyer Recommendation")

    pos_ratio = (final_df["sentiment"] == "Positive").mean()

    if pos_ratio >= 0.6:
        st.success("Recommended based on strong positive feedback.")
    elif pos_ratio <= 0.3:
        st.error("Not recommended due to frequent negative feedback.")
    else:
        st.info("Mixed feedback. Purchase depends on expectations.")

    # ---------------- DETAILED TABLE ----------------
    st.subheader("📋 Review Details")
    st.dataframe(
        final_df[["review_date", "review", "sentiment", "stars"]],
        use_container_width=True
    )
