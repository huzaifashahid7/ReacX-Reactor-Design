import streamlit as st

def get_user_inputs():
    st.markdown("##### Choose Reactor Type")
    reactor_type = st.selectbox("Reactor Type", ["CSTR", "PFR", "Batch"])

    st.markdown("##### Enter Input Parameters")

    CA0 = st.number_input("Initial Concentration, Cₐ₀ (mol/L)", min_value=0.0, step=0.1, format="%.2f")
    k = st.number_input("Rate Constant, k (1/min)", min_value=0.0, step=0.1, format="%.3f")
    X = st.slider("Desired Conversion, X", min_value=0.0, max_value=1.0, step=0.01)

    # Specific Inputs based on reactor type
    if reactor_type == "CSTR":
        v0 = st.number_input("Volumetric Flow Rate, v₀ (L/min)", min_value=0.0, step=0.1)
        return {"reactor": "CSTR", "CA0": CA0, "k": k, "X": X, "v0": v0}

    elif reactor_type == "PFR":
        v0 = st.number_input("Volumetric Flow Rate, v₀ (L/min)", min_value=0.0, step=0.1)
        return {"reactor": "PFR", "CA0": CA0, "k": k, "X": X, "v0": v0}

    elif reactor_type == "Batch":
        return {"reactor": "Batch", "CA0": CA0, "k": k, "X": X}

    else:
        return None
