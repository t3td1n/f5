
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
        "quest": 0
    }

if "log" not in st.session_state:
    st.session_state.log = []

# Define F5 101 quests
quests = [
    {
        "title": "Quest 1: Load Balancing",
        "enemy": "Load Balancer Beast",
        "question": "What is the primary purpose of a load balancer?",
        "options": [
            "To store data securely",
            "To distribute network traffic across multiple servers",
            "To encrypt user data",
            "To monitor CPU temperature"
        ],
        "answer": "To distribute network traffic across multiple servers"
    },
    {
        "title": "Quest 2: SSL Offloading",
        "enemy": "SSL Dragon",
        "question": "What does SSL offloading do?",
        "options": [
            "It stores SSL certificates in the cloud",
            "It shifts SSL encryption/decryption from the server to the load balancer",
            "It disables SSL encryption",
            "It compresses SSL traffic"
        ],
        "answer": "It shifts SSL encryption/decryption from the server to the load balancer"
    },
    {
        "title": "Quest 3: iRules",
        "enemy": "iRule Golem",
        "question": "What are iRules used for in F5?",
        "options": [
            "To define routing logic and traffic manipulation",
            "To create user accounts",
            "To monitor disk usage",
            "To configure DNS records"
        ],
        "answer": "To define routing logic and traffic manipulation"
    }
]

# Display player stats
player = st.session_state.player
st.title("F5 101 RPG Quest")
st.sidebar.header("Player Stats")
st.sidebar.write(f"Name: {player['name']}")
st.sidebar.write(f"Level: {player['level']}")
st.sidebar.write(f"XP: {player['xp']}")
st.sidebar.write(f"HP: {player['hp']}")
st.sidebar.write(f"Attack: {player['attack']}")
st.sidebar.write(f"Defense: {player['defense']}")

# Display current quest
if player["quest"] < len(quests):
    quest = quests[player["quest"]]
    st.header(quest["title"])
    st.write(f"You encounter the **{quest['enemy']}**!")
    st.write("Answer the question to defeat the enemy:")

    selected = st.radio(quest["question"], quest["options"])
    if st.button("Submit Answer"):
        if selected == quest["answer"]:
            st.success("Correct! You defeated the enemy and gained XP.")
            player["xp"] += 50
            if player["xp"] >= player["level"] * 100:
                player["level"] += 1
                player["hp"] += 20
                player["attack"] += 5
                player["defense"] += 2
                st.balloons()
                st.success(f"You leveled up to Level {player['level']}!")
            player["quest"] += 1
        else:
            st.error("Incorrect! Try again.")
else:
    st.header("🎉 Congratulations!")
    st.write("You have completed all F5 101 quests and mastered the basics!")

# Display battle log
st.subheader("Battle Log")
for entry in st.session_state.log:
    st.write(entry)
