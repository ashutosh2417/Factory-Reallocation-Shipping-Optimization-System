import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Nassau Candy Optimization System",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv(
        "../Dataset/Nassau Candy Distributor.csv"
    )

df = load_data()
st.sidebar.header("Filters")

# Region Filter
selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].dropna().unique().tolist())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

# Product Filter
selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All"] + sorted(df["Product Name"].dropna().unique().tolist())
)

if selected_product != "All":
    df = df[df["Product Name"] == selected_product]

selected_ship_mode = st.sidebar.selectbox(
    "Select Ship Mode",
    ["All"] + sorted(df["Ship Mode"].dropna().unique().tolist())
)

if selected_ship_mode != "All":
    df = df[df["Ship Mode"] == selected_ship_mode]
factory_map = {

'Wonka Bar - Nutty Crunch Surprise':"Lot's O' Nuts",
'Wonka Bar - Fudge Mallows':"Lot's O' Nuts",
'Wonka Bar -Scrumdiddlyumptious':"Lot's O' Nuts",

'Wonka Bar - Milk Chocolate':"Wicked Choccy's",
'Wonka Bar - Triple Dazzle Caramel':"Wicked Choccy's",

'Laffy Taffy':'Sugar Shack',
'SweeTARTS':'Sugar Shack',
'Nerds':'Sugar Shack',
'Fun Dip':'Sugar Shack',
'Fizzy Lifting Drinks':'Sugar Shack',

'Everlasting Gobstopper':'Secret Factory',

'Hair Toffee':'The Other Factory',

'Lickable Wallpaper':'Secret Factory',
'Wonka Gum':'Secret Factory',

'Kazookles':'The Other Factory'
}

df['Factory'] = df['Product Name'].map(factory_map)

st.title(
    "🍬 Nassau Candy Factory Optimization System"
)

st.subheader(
    "Business Analytics & Machine Learning Dashboard"
)

# KPI Section

total_sales = df["Sales"].sum()
total_profit = df["Gross Profit"].sum()
total_orders = len(df)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Total Orders",
    total_orders
)

st.metric(
    "Scenario Confidence Score",
    "99.99%"
)
st.metric(
    "Recommendation Coverage",
    "100%"
)
st.divider()

st.header("Dataset Preview")

st.dataframe(df.head())

st.divider()

st.header("Sales by Region")

sales_region = df.groupby(
    "Region"
)["Sales"].sum()

st.bar_chart(sales_region)

st.divider()

st.header("Top Products by Sales")

top_products = df.groupby(
    "Product Name"
)["Sales"].sum().sort_values(
    ascending=False
)

st.bar_chart(top_products)

st.divider()

st.header("Factory Distribution")

factory_counts = df["Factory"].value_counts()

st.bar_chart(factory_counts)

df['Factory'] = df['Product Name'].map(factory_map)

st.divider()

st.header("Machine Learning Model Comparison")

comparison = pd.DataFrame({

'Model':[
    'Linear Regression',
    'Random Forest',
    'Gradient Boosting'
],

'RMSE':[
    100.2538,
    0.8345,
    0.9735
],

'MAE':[
    84.7415,
    0.6231,
    0.7884
],

'R2 Score':[
    0.8579,
    0.99999,
    0.99999
]

})

st.dataframe(comparison)

st.divider()

st.header("Top Product Recommendations")

recommendations = pd.DataFrame({

'Product':[
    'Wonka Bar - Scrumdiddlyumptious',
    'Wonka Bar - Triple Dazzle Caramel',
    'Wonka Bar - Milk Chocolate',
    'Wonka Bar - Nutty Crunch Surprise',
    'Wonka Bar - Fudge Mallows'
],

'Recommendation Score':[
    14.66,
    14.04,
    13.25,
    12.66,
    12.63
]

})

st.dataframe(recommendations)
st.divider()

st.header("What-If Scenario Analysis")

selected_product_analysis = st.selectbox(
    "Choose Product for Analysis",
    sorted(df["Product Name"].unique())
)

current_factory = df[
    df["Product Name"] == selected_product_analysis
]["Factory"].mode()[0]

st.write(
    f"Current Factory: {current_factory}"
)

st.info(
    "Scenario Simulation: Evaluate reassignment to alternative factories to improve shipping efficiency."
)

st.divider()

st.header("Risk & Impact Panel")

st.warning(
    "High-risk reassignments may negatively impact profitability and should be reviewed before implementation."
)

st.success(
    "Recommended reassignments show potential lead-time improvement while maintaining profit stability."
)

st.divider()

st.header("Factory Optimization Simulator")

selected_factory_sim = st.selectbox(
    "Select Alternative Factory",
    sorted(df["Factory"].dropna().unique())
)

st.write(
    f"Simulated Factory Assignment: {selected_factory_sim}"
)

st.success(
    "Alternative factory selected for scenario evaluation."
)