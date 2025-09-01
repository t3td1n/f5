
import streamlit as st
import random

# Initialize session state
if "player" not in st.session_state:
    st.session_state.player = {
        "name": "Hero",
        "level": 1,
        "xp": 0,
        "hp": 100,
        "max_hp": 100,
        "sprite": "🧙‍♂️"
    }
if "quest_index" not in st.session_state:
    st.session_state.quest_index = 0
if "boss_mode" not in st.session_state:
    st.session_state.boss_mode = False

# Define quests with difficulty and XP
quests = [
    {"title": "Intro to Load Balancing", "question": "What is the main purpose of a load balancer?", "answer": "Distribute traffic", "difficulty": "easy"},
    {"title": "SSL Offloading", "question": "What does SSL offloading do?", "answer": "Handles encryption", "difficulty": "medium"},
    {"title": "iRules Basics", "question": "What language is used in iRules?", "answer": "TCL", "difficulty": "hard"},
]

boss_quests = [
    {"title": "Boss: F5 Master", "steps": [
        {"question": "What is the default port for HTTPS?", "answer": "443"},
        {"question": "What is a virtual server in F5?", "answer": "Traffic endpoint"},
        {"question": "What is persistence in load balancing?", "answer": "Session stickiness"}
    ]}
]

difficulty_xp = {"easy": 10, "medium": 20, "hard": 30}

# Display player info
st.title("F5 101 RPG Quest")
st.markdown(f"### {st.session_state.player['sprite']} {st.session_state.player['name']} - Level {st.session_state.player['level']}")
st.progress(st.session_state.player["hp"] / st.session_state.player["max_hp"])
st.markdown(f"**XP:** {st.session_state.player['xp']}")

# Quest logic
if not st.session_state.boss_mode and st.session_state.quest_index < len(quests):
    quest = quests[st.session_state.quest_index]
    st.header(f"Quest: {quest['title']} ({quest['difficulty'].capitalize()})")
    answer = st.text_input("Answer:", key=f"quest_{st.session_state.quest_index}")
    if st.button("Submit Answer", key=f"submit_{st.session_state.quest_index}"):
        if answer.strip().lower() == quest["answer"].lower():
            gained_xp = difficulty_xp[quest["difficulty"]]
            st.success(f"Correct! You gained {gained_xp} XP.")
            st.session_state.player["xp"] += gained_xp
            st.session_state.quest_index += 1
        else:
            st.error("Incorrect. Try again.")

elif not st.session_state.boss_mode:
    st.header("🎉 All quests complete! Prepare for the Boss Battle!")
    if st.button("Enter Boss Battle"):
        st.session_state.boss_mode = True
        st.session_state.boss_step = 0

# Boss battle logic
if st.session_state.boss_mode:
    boss = boss_quests[0]
    st.header(f"👹 {boss['title']}")
    step = boss["steps"][st.session_state.boss_step]
    answer = st.text_input("Boss Challenge:", key=f"boss_{st.session_state.boss_step}", placeholder=step["question"])
    if st.button("Submit Boss Answer", key=f"submit_boss_{st.session_state.boss_step}"):
        if answer.strip().lower() == step["answer"].lower():
            st.success("Correct!")
            st.session_state.boss_step += 1
            if st.session_state.boss_step >= len(boss["steps"]):
                st.success("🎉 You defeated the boss and completed the F5 101 RPG!")
                st.session_state.player["xp"] += 50
                st.session_state.boss_mode = False
        else:
            st.error("Wrong answer! The boss strikes back!")
            st.session_state.player["hp"] -= 10
            if st.session_state.player["hp"] <= 0:
                st.error("💀 You have been defeated. Restarting game...")
                st.session_state.player["hp"] = 100
                st.session_state.player["xp"] = 0
                st.session_state.quest_index = 0
                st.session_state.boss_mode = False

# Level up logic
level_threshold = st.session_state.player["level"] * 50
if st.session_state.player["xp"] >= level_threshold:
    st.session_state.player["level"] += 1
    st.session_state.player["max_hp"] += 20
    st.session_state.player["hp"] = st.session_state.player["max_hp"]
    st.success(f"🎉 Level Up! You are now level {st.session_state.player['level']}!")

# Reset button
if st.button("Reset Game"):
    st.session_state.player = {
        "name": "Hero",
        "level": 1,
        "xp": 0,
        "hp": 100,
        "max_hp": 100,
        "sprite": "🧙‍♂️"
    }
    st.session_state.quest_index = 0
    st.session_state.boss_mode = False
