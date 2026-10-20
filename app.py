import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="TrioAI - Multi-Agent Engine", page_icon="🤖", layout="wide")

# Header Section
st.title("🤖 TrioAI: Multi-Agent Collaborative Engine")
st.caption("Powered by Meta Llama Multi-Perspective Deliberation Network")

st.divider()

# User Input Query
user_query = st.text_input(
    "Apna Question / Topic Yahan Likhein:", 
    placeholder="e.g., Kya 1st year engineering students ko hackathons mein participate karna chahiye?"
)

if st.button("Start Trio AI Discussion 🚀") and user_query:
    st.divider()
    st.subheader("💬 Real-Time Discussion & Debate")
    
    col1, col2, col3 = st.columns(3)
    
    # Agent 1: GPT Nano (Analytical / Logic)
    with col1:
        st.info("### ⚡ Agent 1: GPT Nano\n**Role:** Analytical & Logic Specialist")
        with st.spinner("GPT Nano processing facts..."):
            time.sleep(1)
            st.write(f"**Logical Perspective:**\n'{user_query}' ko agar factual way mein dekhein, toh step-by-step foundation building aur structured execution sabse zaroori factor hai.")
            
    # Agent 2: MEO (Creative / Alternative Ideas)
    with col2:
        st.success("### 💡 Agent 2: MEO\n**Role:** Creative Thinker & Innovator")
        with st.spinner("MEO thinking out-of-the-box..."):
            time.sleep(1.5)
            st.write(f"**Alternative Perspective:**\nOut-of-the-box approach ye hai ki hands-on learning aur practical experimentation se fast-track skills upgrade hoti hain.")
            
    # Agent 3: MIC (Critic / Risk Management)
    with col3:
        st.warning("### 🔍 Agent 3: MIC\n**Role:** Critical Analyst & Risk Evaluator")
        with st.spinner("MIC evaluating risks & flaws..."):
            time.sleep(2)
            st.write(f"**Critical Critique:**\nDono viewpoints mein risk ye hai ki balance bigadne par burnout ho sakta hai. Fundamentals aur practice ka balance zaroori hai.")

    st.divider()
    
    # Final Consensus
    st.markdown("### 🏆 Integrated Final Consensus")
    st.success(
        f"**Conclusion:** Teeno agents (`GPT Nano`, `MEO`, aur `MIC`) ki deliberation ke baad summary ye hai ki "
        f"facts + innovative experimentation + proper risk balance ka **50-50 mix** hi optimal decision hai!"
    )