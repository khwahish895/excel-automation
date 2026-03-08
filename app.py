import streamlit as st
from excel_ops import read_excel, clean_data, save_excel, format_excel
from report_generator import generate_chart
import os

st.set_page_config(page_title="Excel Automation Tool", layout="wide")

st.title("📊 Excel Automation Tool using Python")

uploaded_file = st.file_uploader(
    "Upload an Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = read_excel(uploaded_file)

    st.subheader("📄 Excel Data Preview")
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧹 Clean Data"):
            df = clean_data(df)

            os.makedirs("output", exist_ok=True)
            save_excel(df, "output/final_report.xlsx")
            format_excel("output/final_report.xlsx")

            st.success("Data cleaned and saved as final_report.xlsx")

    with col2:
        if not df.empty:
            selected_column = st.selectbox(
                "Select column for chart",
                df.columns
            )

            if st.button("📈 Generate Chart"):
                generate_chart(df, selected_column)
                st.image("output/chart.png")
                st.success("Chart generated successfully")

    if os.path.exists("output/final_report.xlsx"):
        with open("output/final_report.xlsx", "rb") as file:
            st.download_button(
                label="⬇️ Download Final Excel Report",
                data=file,
                file_name="final_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
