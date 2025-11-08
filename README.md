# 🧠 E-Commerce Customer Behavior Analysis

## 📋 Project Overview
This project analyzes e-commerce transaction data using the RFM (Recency, Frequency, Monetary) model to understand customer purchase patterns and segment them into meaningful clusters.

An interactive Streamlit dashboard visualizes customer segments, insights, and patterns.

---

## 🛠 Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn (for K-Means Clustering)
- Streamlit (for dashboard visualization)
- Jupyter Notebook (for analysis)

---

## 📊 Key Insights
| Cluster | Recency | Frequency | Monetary | Interpretation |
|----------|----------|------------|-----------|----------------|
| 0 | 15.7 | 22.0 | 12,453.2 | Loyal customers |
| 1 | 248.6 | 1.6 | 478.1 | Lost / Dormant customers |
| 2 | 7.4 | 82.7 | 127,338.3 | VIP / High-value customers |
| 3 | 43.9 | 3.7 | 1,349.7 | Potential loyalists |

---

## 📁 Project Structure
Ecommerce_Customer_Behavior/
├─ data/ # Raw data (ignored in GitHub)
├─ notebooks/ # Jupyter notebooks for EDA & clustering
├─ dashboard/ # Streamlit app for visualization
├─ reports/ # Output RFM summary
├─ requirements.txt # Dependencies
└─ README.md # Project description

---

## 🚀 Run Locally
```bash
pip install -r requirements.txt
cd dashboard
streamlit run app.py
