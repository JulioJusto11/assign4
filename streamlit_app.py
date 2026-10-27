# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Julio Justo")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4* tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "* Something New"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: MSFT
with tabs[3]:
    st.subheader("MSFT Logo")

    # 1. Define the coordinates to draw the letters
    # Format: (X-coordinates, Y-coordinates)
    m_x, m_y = [0, 0, 0.5, 1, 1], [0, 1, 0.5, 1, 0]
    s_x = [2, 1.2, 1, 1.2, 1.8, 2, 1.8, 1.2]
    s_y = [0.9, 1, 0.8, 0.5, 0.5, 0.2, 0, 0.1]
    f_vert_x, f_vert_y = [2.5, 2.5], [0, 1]
    f_top_x, f_top_y = [2.5, 3.3], [1, 1]
    f_mid_x, f_mid_y = [2.5, 3.1], [0.5, 0.5]
    t_vert_x, t_vert_y = [4.2, 4.2], [0, 1]
    t_top_x, t_top_y = [3.7, 4.7], [1, 1]

    fig, ax = plt.subplots(figsize=(8, 3))

    # Plot each letter line segment
    ax.plot(m_x, m_y, color="#F25022", linewidth=5, solid_capstyle="round")
    ax.plot(s_x, s_y, color="#7FBA00", linewidth=5, solid_capstyle="round")
    ax.plot(
        f_vert_x, f_vert_y, color="00A4EF", linewidth=5, solid_capstyle="round"
    )
    ax.plot(
        f_top_x, f_top_y, color="00A4EF", linewidth=5, solid_capstyle="round"
    )
    ax.plot(
        f_mid_x, f_mid_y, color="00A4EF", linewidth=5, solid_capstyle="round"
    )
    ax.plot(
        t_vert_x, t_vert_y, color="#FFB900", linewidth=5, solid_capstyle="round"
    )
    ax.plot(
        t_top_x, t_top_y, color="#FFB900", linewidth=5, solid_capstyle="round"
    )

    # Styling boundaries and grid
    ax.set_xlim(-0.5, 5.2)
    ax.set_ylim(-0.2, 1.2)
    ax.grid(True, linestyle="--", alpha=0.5)

    # 3. Render inside the tab
    st.pyplot(fig)
