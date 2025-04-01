import pandas as pd
import streamlit as st

DATA_URL = "https://gist.githubusercontent.com/slopp/ce3b90b9168f2f921784de84fa445651/raw/4ecf3041f0ed4913e7c230758733948bc561f434/penguins.csv"

st.write("# 👋 Hello PyCon AT!")


st.write("# 💾 Dataset")
df = pd.read_csv(DATA_URL).loc[:, ["species", "bill_length_mm", "bill_depth_mm", "sex", "year"]]
st.dataframe(df.tail())

st.write("# 🤘 Filters")

cols = st.columns(2)

with cols[0]:
    selected_species = st.selectbox(
        label="Select Species",
        options=df.species.unique(),
    )

with cols[1]:
    selected_year = st.slider(
        label="Select Year",
        min_value=df.year.min(),
        max_value=df.year.max(),
    )

df = df.loc[df.species == selected_species].loc[df.year == selected_year]
df

st.write("# 📊 Charts")
st.scatter_chart(df, x="bill_length_mm", y="bill_depth_mm", color="sex")

if st.download_button(
    label="Download Dataset",
    data=df.to_csv(index=False),
    file_name="penguins.csv",
):
    st.balloons()
