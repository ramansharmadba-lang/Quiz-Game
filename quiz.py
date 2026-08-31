import streamlit as st

st.set_page_config(page_title="KBC Quiz Game", page_icon="💰")
st.title("💰 KBC Style Quiz Game")

questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Rome", "Paris", "London", "Berlin", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Shark", 2],
    ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Homer", 2],
    ["What is the square root of 64?", "6", "8", "10", "12", 2],
    ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "South Korea", "India", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the fastest land animal?", "Cheetah", "Lion", "Elephant", "Horse", 1],
    ["Which ocean is the largest?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "San Marino", "Liechtenstein", 1]
]
prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

# Session state se score yaad rahega
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.total_prize = 0
    st.session_state.finished = False

if not st.session_state.finished:
    i = st.session_state.current_q
    q = questions[i]

    st.subheader(f"Question {i+1} for ₹{prizes[i]:,}")
    st.progress((i+1)/len(questions))
    st.write(f"**{q[0]}**")

    options_map = {1: q[1], 2: q[2], 3: q[3], 4: q[4]}
    choice = st.radio("Select your answer:", [1,2,3,4], format_func=lambda x: f"{['a','b','c','d'][x-1]}> {options_map[x]}", key=f"q{i}")

    if st.button("Lock Answer"):
        if choice == q[5]:
            st.success(f"Correct! You won ₹{prizes[i]:,}")
            st.session_state.total_prize += prizes[i]
            st.session_state.current_q += 1
            if st.session_state.current_q >= len(questions):
                st.session_state.finished = True
            st.rerun()
        else:
            st.error(f"Incorrect! Correct was {['a','b','c','d'][q[5]-1]}> {options_map[q[5]]}")
            st.session_state.finished = True
            st.rerun()
else:
    st.header(f"Game Over! Final Prize: ₹{st.session_state.total_prize:,}")
    if st.session_state.total_prize > 0:
        st.balloons()
    if st.button("Play Again"):
        st.session_state.current_q = 0
        st.session_state.total_prize = 0
        st.session_state.finished = False
        st.rerun()