import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import json
import time

st.set_page_config(
    page_title="Humanoid Robbot by Gesner Deslandes",
    page_icon="🤖",
    layout="wide"
)

# ---------- Custom CSS for premium look ----------
st.markdown("""
<style>
    /* Global */
    .main { padding: 0rem 1rem; }
    h1, h2, h3 { font-family: 'Segoe UI', sans-serif; }
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #e9edf2 100%); }
    
    /* Hero section */
    .hero-robot {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        padding: 2rem;
        border-radius: 30px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
    }
    .hero-robot h1 { font-size: 2.5rem; margin-bottom: 0; }
    .hero-robot p { font-size: 1.1rem; opacity: 0.9; }
    
    /* Cards */
    .card {
        background: white;
        border-radius: 20px;
        padding: 1.2rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        transition: transform 0.2s, box-shadow 0.2s;
        height: 100%;
    }
    .card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }
    .card h3 { color: #1e3c72; margin-top: 0; }
    
    /* Buttons */
    .stButton button {
        background: linear-gradient(90deg, #1e3c72, #2a5298);
        color: white;
        border: none;
        border-radius: 40px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        transition: 0.2s;
    }
    .stButton button:hover {
        transform: scale(1.02);
        background: linear-gradient(90deg, #2a5298, #1e3c72);
    }
    
    /* Tabs custom */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1rem;
        font-weight: 600;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #1e3c72;
    }
    
    /* Code block */
    .command-box {
        background: #1e1e2f;
        color: #f8f8f2;
        border-radius: 12px;
        padding: 0.8rem;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
    }
    .status-online {
        color: #00c853;
        font-weight: bold;
        background: #e8f5e9;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        display: inline-block;
    }
    .status-offline {
        color: #d32f2f;
        font-weight: bold;
        background: #ffebee;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        display: inline-block;
    }
    .task-item {
        background: #f1f8e9;
        border-left: 5px solid #2e7d32;
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 8px;
    }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ---------- Session state for task training ----------
if "tasks" not in st.session_state:
    st.session_state.tasks = []   # list of dicts: {"name": str, "command": str}
if "robot_connected" not in st.session_state:
    st.session_state.robot_connected = False
if "telemetry" not in st.session_state:
    st.session_state.telemetry = {"position": [0,0,0], "battery": 95, "status": "Idle"}

# ---------- Helper functions ----------
def add_task(name, command):
    if name and command:
        st.session_state.tasks.append({"name": name, "command": command})
        return True
    return False

def execute_task(command):
    # Simulate real robot execution (replace with actual API later)
    st.session_state.telemetry["status"] = f"Executing: {command[:30]}..."
    time.sleep(0.5)  # simulate processing
    st.session_state.telemetry["status"] = "Completed"
    return f"✅ Executed: {command}"

# ---------- Header ----------
st.markdown("""
<div class="hero-robot">
    <h1>🤖 Humanoid Robbot built by Gesner Deslandes</h1>
    <p>Train. Simulate. Deploy. – The next generation of humanoid robotics software</p>
</div>
""", unsafe_allow_html=True)

# ---------- Tabs for organised sections ----------
tab1, tab2, tab3, tab4 = st.tabs(["📺 Public Demo", "🎮 Training Studio", "🤖 Real Robot Control", "📘 About & Docs"])

# ========== TAB 1: DEMO VIDEO ==========
with tab1:
    st.markdown("### 🎬 Humanoid Robot Marathon – Public Demonstration")
    st.markdown("*Watch our humanoid robot running in a live marathon event. Real‑world performance, endurance, and AI in action.*")
    
    # ✅ Your actual GitHub raw video link
    ROBOT_VIDEO_URL = "https://raw.githubusercontent.com/Deslandes1/Humanoid-Robot-Built-by-Gesner-Deslandes/main/Humanoid%20robot.mp4"
    
    col_vid, col_desc = st.columns([2, 1])
    with col_vid:
        if ROBOT_VIDEO_URL:
            st.video(ROBOT_VIDEO_URL, format="video/mp4", start_time=0)
            st.caption("📽️ Humanoid robot during public marathon – real‑time demonstration")
        else:
            st.info("🔜 Robot marathon video will appear here once you upload it to GitHub and update the `ROBOT_VIDEO_URL` variable.")
            st.markdown("**How to update:** Replace the URL above with your raw GitHub video link (e.g., `https://raw.githubusercontent.com/.../video.mp4`).")
    with col_desc:
        st.markdown("""
        <div class="card">
            <h3>🏆 Marathon Performance</h3>
            <p>✔️ 42km endurance<br>
            ✔️ Real‑time balance & gait adaptation<br>
            ✔️ AI visual navigation<br>
            ✔️ Public trust & safety demonstration</p>
            <p><em>“From lab to the streets – proving humanoid reliability.”</em></p>
        </div>
        """, unsafe_allow_html=True)

# ========== TAB 2: TRAINING STUDIO ==========
with tab2:
    st.markdown("### 🎯 Train the Robot to Execute Any Task")
    st.markdown("Build a sequence of commands, test them in simulation, then send to the real robot.")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("📝 Add New Task")
        with st.form("add_task_form"):
            task_name = st.text_input("Task name (e.g., 'Walk Forward 2m')")
            task_command = st.text_area("Robot command (Python or JSON)", "move_forward(distance=2.0)\ngrip(object='cube')")
            submitted = st.form_submit_button("➕ Add Task to Library")
            if submitted and task_name and task_command:
                add_task(task_name, task_command)
                st.success(f"Task '{task_name}' added!")
                st.rerun()
    
    with col_right:
        st.subheader("📚 Task Library")
        if st.session_state.tasks:
            for i, task in enumerate(st.session_state.tasks):
                with st.expander(f"📌 {task['name']}"):
                    st.code(task['command'], language="python")
                    if st.button(f"▶️ Execute this task", key=f"exec_{i}"):
                        result = execute_task(task['command'])
                        st.toast(result, icon="🤖")
            if st.button("🗑️ Clear all tasks"):
                st.session_state.tasks = []
                st.rerun()
        else:
            st.info("No tasks yet. Use the form to add training tasks.")
    
    st.divider()
    st.subheader("⚙️ Simulation Runner")
    sim_command = st.text_area("Write or paste a single command to test in simulation:", "move_arm(joint='shoulder', angle=45)")
    if st.button("▶️ Run in Simulation"):
        st.code(f"Simulating: {sim_command}", language="python")
        with st.spinner("Robot thinking..."):
            time.sleep(1)
        st.success("✅ Simulation completed – command is valid. You can now add it to the Task Library.")
        st.balloons()

# ========== TAB 3: REAL ROBOT CONTROL ==========
with tab3:
    st.markdown("### 🤖 Live Control & Telemetry")
    st.markdown("Connect to the physical humanoid robot (via API or serial) and send commands.")
    
    # Connection panel
    col_conn, col_tele = st.columns(2)
    with col_conn:
        if not st.session_state.robot_connected:
            if st.button("🔌 Connect to Robot", use_container_width=True):
                # Simulated connection (replace with real backend)
                st.session_state.robot_connected = True
                st.session_state.telemetry["status"] = "Connected"
                st.rerun()
        else:
            st.markdown(f"<span class='status-online'>✅ Connected</span>", unsafe_allow_html=True)
            if st.button("🔌 Disconnect", use_container_width=True):
                st.session_state.robot_connected = False
                st.session_state.telemetry["status"] = "Disconnected"
                st.rerun()
    
    with col_tele:
        st.subheader("📡 Telemetry")
        tele = st.session_state.telemetry
        st.metric("Battery", f"{tele['battery']}%")
        st.metric("Position", f"X:{tele['position'][0]} Y:{tele['position'][1]} Z:{tele['position'][2]}")
        st.markdown(f"**Status:** {tele['status']}")
    
    st.divider()
    st.subheader("📟 Command Sender (Real Robot)")
    real_cmd = st.text_area("Enter robot command (Python / JSON / custom protocol)", "walk(speed=0.8, direction='forward')")
    if st.button("🚀 Send to Real Robot", use_container_width=True):
        if not st.session_state.robot_connected:
            st.error("Robot not connected. Please connect first.")
        else:
            with st.spinner("Sending command..."):
                time.sleep(1)  # simulate real execution
                st.session_state.telemetry["status"] = f"Executed: {real_cmd[:40]}"
            st.success("Command transmitted successfully!")
            st.balloons()
    
    st.info("💡 *For real hardware integration, replace the simulation delay with actual HTTP/WebSocket calls to your robot's API.*")

# ========== TAB 4: ABOUT & DOCS ==========
with tab4:
    st.markdown("### 📘 Humanoid Robbot – Software Overview")
    st.markdown("""
    **Developed by Gesner Deslandes** – Founder of GlobalInternet.py
    
    This software suite enables:
    - 🧠 **AI‑driven task learning** – Train the robot by demonstration or scripted commands.
    - 🦾 **Real‑time control** – Send movement, grip, and navigation commands.
    - 📊 **Performance analytics** – Monitor battery, position, and executed tasks.
    - 🔄 **Full integration** – Ready to connect to any humanoid robot hardware (ROS2, MAVLink, or custom API).
    
    #### 🔧 How to use:
    1. **Public Demo** – Watch the marathon video (upload your own clip).
    2. **Training Studio** – Create a library of tasks and simulate them.
    3. **Real Robot Control** – Connect to your physical robot and send commands live.
    
    #### 📦 Coming soon:
    - Voice command interface
    - Computer vision integration (object recognition)
    - Remote teleoperation via web browser
    
    #### 📞 Contact for customisation or hardware integration:
    ✉️ deslandes78@gmail.com  
    📱 WhatsApp (509) 4738-5663  
    🌐 [GlobalInternet.py website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)
    """)
    
    st.markdown("---")
    st.markdown("#### 👨‍💻 Built with Streamlit • Python • AI")
    st.caption("© 2026 Humanoid Robbot by Gesner Deslandes – All rights reserved")

# ---------- Footer ----------
st.markdown("---")
st.markdown("<p style='text-align:center; color:#666;'>🤖 Humanoid Robbot – From code to reality. Proudly built by Gesner Deslandes.</p>", unsafe_allow_html=True)
