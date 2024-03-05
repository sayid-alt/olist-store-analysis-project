import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

with st.sidebar:
    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY")

    st.write("Start time:", start_time)
