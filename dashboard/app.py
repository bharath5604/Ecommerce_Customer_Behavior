# ============================================================
# Streamlit Dashboard for E-Commerce Customer Insights
# ============================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="E-Commerce RFM Dashboard", layout="wide")
st.title("📊 E-Commerce Customer Behavior Dashboard")

# -----------------------------
# Load RFM summary data
# -----------------------------
try:
    df = pd.read_csv('reports/rfm_summary.csv')
    st.success("✅ RFM data loaded successfully!")
except FileNotFoundError:
    st.error("⚠️ RFM summary file not found! Please run the analysis notebooks first.")
    st.stop()

# -----------------------------
# Sidebar controls
# -----------------------------
st.sidebar.header("Filter Options")
clusters = sorted(df['Cluster'].unique())
selected_cluster = st.sidebar.selectbox("Select Cluster", ['All'] + [str(c) for c in clusters])

# Filter data based on cluster selection
if selected_cluster == 'All':
    cluster_data = df.copy()
else:
    cluster_data = df[df['Cluster'] == int(selected_cluster)]

# -----------------------------
# Summary table
# -----------------------------
st.subheader(f"📋 Cluster {selected_cluster} Summary")
st.write(cluster_data.describe().T)

# -----------------------------
# Visual 1: Cluster distribution (always show all clusters)
# -----------------------------
st.subheader("🧩 Cluster Distribution (All Customers)")
fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(x='Cluster', data=df, hue='Cluster', palette='viridis', legend=False, ax=ax)
for container in ax.containers:
    ax.bar_label(container)
ax.set_title('Number of Customers per Cluster')
st.pyplot(fig)

# -----------------------------
# Visual 2: Pairplot (filtered)
# -----------------------------
st.subheader("📈 RFM Relationship Overview (Filtered)")
if len(cluster_data) > 1:
    fig2 = sns.pairplot(cluster_data, hue='Cluster', vars=['Recency','Frequency','Monetary'])
    st.pyplot(fig2)
else:
    st.info("Select 'All' or a larger cluster to see pairplot relationships.")

# -----------------------------
# Visual 3: Heatmap (filtered)
# -----------------------------
st.subheader("🔥 Average RFM per Cluster (Filtered)")
avg_rfm = cluster_data.groupby('Cluster')[['Recency','Frequency','Monetary']].mean().round(1)
fig3, ax3 = plt.subplots(figsize=(6,4))
sns.heatmap(avg_rfm, annot=True, cmap='coolwarm', fmt='.1f', ax=ax3)
ax3.set_title('Cluster Profile Heatmap')
st.pyplot(fig3)

# -----------------------------
# Insights
# -----------------------------
st.subheader("💡 Insights & Recommendations")
st.markdown("""
- **Low Recency + High Frequency + High Monetary** → Loyal & High-Value Customers 🏆  
- **High Recency + Low Frequency + Low Monetary** → Lost or Dormant Customers ⚠️  
- **Moderate Recency + Medium Frequency** → Regular Buyers to Retain 💼  
- **High Monetary + Low Frequency** → Occasional Big Spenders 💰  
""")
