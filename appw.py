
import streamlit as st
import random

# Initialize session state
if "player" not in st.session_state:
    st.session_state.player = {
        "name": "Hero",
        "level": 1,
        "xp": 0,
        "hp": 100,
        "attack": 10,
        "defense": 5,
        "quests_completed": [],
        "bosses_defeated": []
    }

if "current_quest" not in st.session_state:
    st.session_state.current_quest = None

# Define quests and bosses
quests = [
    {"id": "q1", "title": "Intro to Load Balancing", "question": "What is the main purpose of a load balancer?", "options": ["To store data", "To distribute traffic", "To encrypt data"], "answer": "To distribute traffic", "difficulty": "Easy", "xp": 10, "sprite": "🦊"},
    {"id": "q2", "title": "SSL Offloading", "question": "What does SSL offloading do?", "options": ["Encrypts traffic", "Stores cookies", "Caches pages"], "answer": "Encrypts traffic", "difficulty": "Medium", "xp": 20, "sprite": "🐸"},
    {"id": "q3", "title": "iRules Basics", "question": "What are iRules used for?", "options": ["Routing traffic", "Logging in", "User authentication"], "answer": "Routing traffic", "difficulty": "Hard", "xp": 30, "sprite": "🐉"}
]

bosses = [
    {"id": "b1", "title": "Boss: Load Master", "question": "Which layer does a load balancer typically operate on?", "options": ["Layer 1", "Layer 4 or 7", "Layer 3"], "answer": "Layer 4 or 7", "xp": 50, "sprite": "👹"},
    {"id": "b2", "title": "Boss: SSL Demon", "question": "Which protocol is used for secure web traffic?", "options": ["HTTP", "FTP", "HTTPS"], "answer": "HTTPS", "xp": 60, "sprite": "💀"}
]

def show_stats():
    st.sidebar.header("🧙 Player Stats")
    st.sidebar.write(f"**Level:** {st.session_state.player['level']}")
    st.sidebar.write(f"**XP:** {st.session_state.player['xp']}")
    st.sidebar.write(f"**HP:** {st.session_state.player['hp']}")
    st.sidebar.write(f"**Attack:** {st.session_state.player['attack']}")
    st.sidebar.write(f"**Defense:** {st.session_state.player['defense']}")

def show_tracker():
    st.sidebar.header("📜 Quest Tracker")
    st.sidebar.write("**Quests Completed:**")
    for q in st.session_state.player["quests_completed"]:
        st.sidebar.write(f"✅ {q}")
    st.sidebar.write("**Bosses Defeated:**")
    for b in st.session_state.player["bosses_defeated"]:
        st.sidebar.write(f"🏆 {b}")

def gain_xp(amount):
    st.session_state.player["xp"] += amount
    level_up()

def level_up():
    xp = st.session_state.player["xp"]
    level = st.session_state.player["level"]
    if xp >= level * 50:
        st.session_state.player["level"] += 1
        st.session_state.player["hp"] += 20
        st.session_state.player["attack"] += 5
        st.session_state.player["defense"] += 2
        st.success(f"🎉 You leveled up to Level {st.session_state.player['level']}!")

def handle_quest(quest):
    st.subheader(f"{quest['sprite']} {quest['title']}")
    st.write(quest["question"])
    choice = st.radio("Choose your answer:", quest["options"], key=quest["id"])
    if st.button("Submit", key=f"submit_{quest['id']}"):
        if choice == quest["answer"]:
            st.success("Correct! You defeated the enemy!")
            gain_xp(quest["xp"])
            st.session_state.player["quests_completed"].append(quest["title"])
        else:
            st.error("Wrong answer! Try again later.")
        st.session_state.current_quest = None

def handle_boss(boss):
    st.subheader(f"{boss['sprite']} {boss['title']}")
    st.write("⚔️ Boss Battle Initiated!")
    st.write(boss["question"])
    choice = st.radio("Choose your answer:", boss["options"], key=boss["id"])
    if st.button("Submit", key=f"submit_{boss['id']}"):
        if choice == boss["answer"]:
            st.success("You defeated the boss!")
            gain_xp(boss["xp"])
            st.session_state.player["bosses_defeated"].append(boss["title"])
        else:
            st.error("The boss defeated you! Try again later.")
        st.session_state.current_quest = None

st.title("🛡️ F5 101 RPG Learning Game")

show_stats()
show_tracker()

available_quests = [q for q in quests if q["title"] not in st.session_state.player["quests_completed"]]
available_bosses = [b for b in bosses if b["title"] not in st.session_state.player["bosses_defeated"]]

if st.session_state.current_quest is None:
    st.subheader("Choose Your Next Challenge")
    for quest in available_quests:
        if st.button(f"Start Quest: {quest['title']}", key=quest["id"]):
            st.session_state.current_quest = quest
    for boss in available_bosses:
        if st.button(f"Face Boss: {boss['title']}", key=boss["id"]):
            st.session_state.current_quest = boss
else:
    if "sprite" in st.session_state.current_quest:
        if "Boss" in st.session_state.current_quest["title"]:
            handle_boss(st.session_state.current_quest)
        else:
            handle_quest(st.session_state.current_quest)
