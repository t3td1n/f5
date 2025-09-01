
import streamlit as st
import random
from PIL import Image

# Load sprites
cute_sprite = Image.open("images/cute_enemy.jpg")
scary_sprite = Image.open("images/scary_boss.jpg")

# Initialize session state
if "player" not in st.session_state:
    st.session_state.player = {
        "level": 1,
        "xp": 0,
        "hp": 100,
        "attack": 10,
        "defense": 5,
        "quests_completed": [],
        "bosses_defeated": []
    }

# Define quests and bosses
quests = [
    {
        "id": "q1",
        "title": "Learn Load Balancing",
        "question": "What is the main purpose of load balancing?",
        "options": ["Encrypt traffic", "Distribute traffic", "Store data", "Monitor servers"],
        "answer": "Distribute traffic",
        "difficulty": "Easy",
        "xp": 10,
        "sprite": "cute"
    },
    {
        "id": "q2",
        "title": "Understand SSL Offloading",
        "question": "What does SSL offloading do?",
        "options": ["Stores SSL certificates", "Encrypts outbound traffic", "Moves SSL processing from server to device", "Blocks SSL traffic"],
        "answer": "Moves SSL processing from server to device",
        "difficulty": "Medium",
        "xp": 20,
        "sprite": "cute"
    },
    {
        "id": "q3",
        "title": "Master iRules",
        "question": "What are iRules used for in F5?",
        "options": ["Routing logic", "User authentication", "Database queries", "Firewall rules"],
        "answer": "Routing logic",
        "difficulty": "Hard",
        "xp": 30,
        "sprite": "cute"
    }
]

bosses = [
    {
        "id": "b1",
        "title": "Boss: F5 Architect",
        "question": "Which F5 feature allows custom traffic handling?",
        "options": ["iRules", "SSL Offloading", "Load Balancing", "Caching"],
        "answer": "iRules",
        "difficulty": "Boss",
        "xp": 50,
        "sprite": "scary"
    }
]

# Display player stats
st.title("🧙‍♂️ F5 101 RPG Learning Game")
st.sidebar.header("Player Stats")
st.sidebar.write(f"Level: {st.session_state.player['level']}")
st.sidebar.write(f"XP: {st.session_state.player['xp']}")
st.sidebar.write(f"HP: {st.session_state.player['hp']}")
st.sidebar.write(f"Attack: {st.session_state.player['attack']}")
st.sidebar.write(f"Defense: {st.session_state.player['defense']}")

# Function to handle quest
def handle_quest(quest):
    st.header(quest["title"])
    if quest["sprite"] == "cute":
        st.image(cute_sprite, width=150)
    else:
        st.image(scary_sprite, width=150)
    st.write(quest["question"])
    choice = st.radio("Choose your answer:", quest["options"], key=quest["id"])
    if st.button("Submit", key=f"submit_{quest['id']}"):
        if choice == quest["answer"]:
            st.success("Correct! You gained XP.")
            st.session_state.player["xp"] += quest["xp"]
            if quest["id"].startswith("q"):
                st.session_state.player["quests_completed"].append(quest["id"])
            else:
                st.session_state.player["bosses_defeated"].append(quest["id"])
            # Level up logic
            level_threshold = st.session_state.player["level"] * 50
            if st.session_state.player["xp"] >= level_threshold:
                st.session_state.player["level"] += 1
                st.session_state.player["hp"] += 20
                st.session_state.player["attack"] += 5
                st.session_state.player["defense"] += 3
                st.success("🎉 You leveled up!")
        else:
            st.error("Wrong answer! Try again.")

# Display quests
st.subheader("📘 Quests")
for quest in quests:
    if quest["id"] not in st.session_state.player["quests_completed"]:
        handle_quest(quest)

# Display boss battles
st.subheader("👹 Boss Battles")
for boss in bosses:
    if boss["id"] not in st.session_state.player["bosses_defeated"]:
        handle_quest(boss)

# Reset button
if st.button("Reset Game"):
    del st.session_state.player
    st.experimental_rerun()
