import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

"""
# 🛒 Retail Sales Analysis Dashboard
"""

""  # space

# ---- Layout like stock app ----
cols = st.columns([1, 4])
left_cell = cols[0].container()  # left panel will fit content height
right_cell = cols[1].container()  # right panel flexible for charts

# ---- Load data ----
df = pd.read_csv("sales_cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"])

# =========================
# Left control panel
# =========================
with left_cell:
    # Simulated border around left panel
    st.markdown(
        "<div style='border:1px solid #ddd; padding:10px; border-radius:5px;'>",
        unsafe_allow_html=True
    )

    st.subheader("🎛 Filters")

    period = st.selectbox(
        "Time range",
        ["All", "Last 7 days", "Last 1 month", "Last 3 months", "Last 6 months"]
    )

    categories = st.multiselect(
        "Product category",
        options=sorted(df["Product_Category"].unique()),
        default=list(df["Product_Category"].unique())
    )

    genders = st.multiselect(
        "Gender",
        options=sorted(df["Gender"].unique()),
        default=list(df["Gender"].unique())
    )

    qty_min, qty_max = st.slider(
        "Quantity range",
        int(df["Quantity"].min()),
        int(df["Quantity"].max()),
        (int(df["Quantity"].min()), int(df["Quantity"].max()))
    )

    st.markdown("---")
    st.subheader("📈 Trend Options")

    show_categories = st.multiselect(
        "Show categories in trend chart",
        options=sorted(df["Product_Category"].unique()),
        default=list(df["Product_Category"].unique())
    )

    split_by_gender = st.toggle("Split trend by Gender")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Apply filters
# =========================
filtered = df.copy()
max_date = filtered["Date"].max()

if period != "All":
    days_map = {
        "Last 7 days": 7,
        "Last 1 month": 30,
        "Last 3 months": 90,
        "Last 6 months": 180,
    }
    filtered = filtered[
        filtered["Date"] >= max_date - pd.Timedelta(days=days_map[period])
    ]

filtered = filtered[
    (filtered["Product_Category"].isin(categories)) &
    (filtered["Gender"].isin(genders)) &
    (filtered["Quantity"].between(qty_min, qty_max))
]

# =========================
# Right panel (charts)
# =========================
with right_cell:
    st.subheader("📈 Sales Trends & Breakdown")

    # ---- Big Altair trend chart (aligned in right panel) ----
    trend_df = filtered[filtered["Product_Category"].isin(show_categories)]

    if trend_df.empty:
        st.info("No data for the selected filters.")
    else:
        if split_by_gender:
            plot_df = (
                trend_df
                .groupby(["Date", "Product_Category", "Gender"], as_index=False)["Total_Amount"]
                .sum()
            )
            plot_df["Series"] = plot_df["Product_Category"] + " - " + plot_df["Gender"]
            plot_long = plot_df.rename(columns={"Total_Amount": "Sales"})

            chart = (
                alt.Chart(plot_long)
                .mark_line()
                .encode(
                    alt.X("Date:T"),
                    alt.Y("Sales:Q").scale(zero=False),
                    alt.Color("Series:N"),
                    alt.Tooltip(["Date:T", "Series:N", "Sales:Q"]),
                )
                .properties(height=400)
            )
        else:
            plot_df = (
                trend_df
                .groupby(["Date", "Product_Category"], as_index=False)["Total_Amount"]
                .sum()
            )
            plot_long = plot_df.rename(columns={"Total_Amount": "Sales"})

            chart = (
                alt.Chart(plot_long)
                .mark_line()
                .encode(
                    alt.X("Date:T"),
                    alt.Y("Sales:Q").scale(zero=False),
                    alt.Color("Product_Category:N"),
                    alt.Tooltip(["Date:T", "Product_Category:N", "Sales:Q"]),
                )
                .properties(height=400)
            )

        st.altair_chart(chart, use_container_width=True)

    st.markdown("---")

    # ---- KPIs ----
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Revenue", f"R {filtered['Total_Amount'].sum():,.0f}")
    c2.metric("Total Orders", len(filtered))
    c3.metric("Avg Order Value", f"R {filtered['Total_Amount'].mean():,.0f}")

    # ---- Other charts below ----
    cat_sales = filtered.groupby("Product_Category")["Total_Amount"].sum().reset_index()
    bar = alt.Chart(cat_sales).mark_bar().encode(
        x="Product_Category:N",
        y="Total_Amount:Q",
        tooltip=["Product_Category", "Total_Amount"]
    ).properties(title="Sales by Category", height=300)

    gender_sales = filtered.groupby("Gender")["Total_Amount"].sum().reset_index()
    pie = alt.Chart(gender_sales).mark_arc().encode(
        theta="Total_Amount:Q",
        color="Gender:N",
        tooltip=["Gender", "Total_Amount"]
    ).properties(title="Sales by Gender", height=300)

    time_sales = filtered.groupby("Date")["Total_Amount"].sum().reset_index()
    line = alt.Chart(time_sales).mark_line(point=True).encode(
        x="Date:T",
        y="Total_Amount:Q",
        tooltip=["Date", "Total_Amount"]
    ).properties(title="Total Sales Over Time", height=300)

    col1, col2 = st.columns(2)
    col1.altair_chart(bar, use_container_width=True)
    col2.altair_chart(pie, use_container_width=True)
    st.altair_chart(line, use_container_width=True)

# =========================
# Table
# =========================
st.subheader("📄 Filtered Data")
st.dataframe(filtered, use_container_width=True)

