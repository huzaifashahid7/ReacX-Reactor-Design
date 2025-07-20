import streamlit as st

def display_latex():
    with st.expander("📦 CSTR Theory & Formula"):
        st.markdown("""
        In **Continuous Stirred Tank Reactor (CSTR)**, the reactor is assumed to be perfectly mixed.  
        The design equation is:

        $$
        V = \\frac{v_0 \\cdot X}{k \\cdot C_{A0} (1 - X)}
        $$

        Where:  
        - \( V \): Volume of reactor (L)  
        - \( v_0 \): Volumetric flow rate (L/min)  
        - \( X \): Conversion  
        - \( C_{A0} \): Initial concentration (mol/L)  
        - \( k \): Rate constant (1/min)
        """)

    with st.expander("🌀 PFR Theory & Formula"):
        st.markdown("""
        In **Plug Flow Reactor (PFR)**, the fluid flows without mixing in axial direction.  
        The design equation is:

        $$
        V = \\frac{v_0}{k \\cdot C_{A0}} \\cdot \\frac{X}{1 - X}
        $$

        """)

    with st.expander("⏱️ Batch Reactor Theory & Formula"):
        st.markdown("""
        In **Batch Reactor**, no flow enters or leaves during the reaction.  
        The design equation is:

        $$
        t = \\frac{1}{k \\cdot C_{A0}} \\cdot \\ln\\left(\\frac{1}{1 - X}\\right)
        $$

        Where:  
        - \( t \): Time (min)
        """)

    with st.expander("📘 Assumptions & Notes"):
        st.markdown("""
        - Isothermal operation  
        - First-order irreversible reaction: \( A \\rightarrow \text{Products} \)  
        - No side reactions  
        - Constant density and volume  
        - Steady state for flow reactors
        """)
