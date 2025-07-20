import streamlit as st
import plotly.graph_objects as go
import numpy as np
import math

def show_plot(inputs, results):
    reactor = inputs["reactor"]
    CA0 = inputs["CA0"]
    k = inputs["k"]
    X_target = inputs["X"]

    if reactor in ["CSTR", "PFR"]:
        v0 = inputs["v0"]

    fig = go.Figure()

    if reactor == "CSTR":
        X = np.linspace(0.01, 0.99, 100)
        V = v0 * (X / (k * CA0 * (1 - X)))
        fig.add_trace(go.Scatter(x=X, y=V, mode='lines', name='CSTR Design Curve'))
        fig.update_layout(
            title="CSTR: Conversion vs Volume",
            xaxis_title="Conversion (X)",
            yaxis_title="Volume (L)",
            template="plotly_white"
        )

    elif reactor == "PFR":
        X = np.linspace(0.01, 0.99, 100)
        V = (v0 / (k * CA0)) * (X / (1 - X))
        fig.add_trace(go.Scatter(x=X, y=V, mode='lines', name='PFR Design Curve'))
        fig.update_layout(
            title="PFR: Conversion vs Volume",
            xaxis_title="Conversion (X)",
            yaxis_title="Volume (L)",
            template="plotly_white"
        )

    elif reactor == "Batch":
        X = np.linspace(0.01, 0.99, 100)
        t = (1 / (k * CA0)) * np.log(1 / (1 - X))
        fig.add_trace(go.Scatter(x=t, y=X, mode='lines', name='Batch Reactor'))
        fig.update_layout(
            title="Batch Reactor: Time vs Conversion",
            xaxis_title="Time (min)",
            yaxis_title="Conversion (X)",
            template="plotly_white"
        )

    st.plotly_chart(fig, use_container_width=True)