import streamlit as st


st.title("Streamlit Tutorial App")
st.write("Hello World")


# Button
st.header("Button Section")
button1 = st.button("Click Me")
if button1:
  st.write("This is run after button1 is clicked")


# Checkbox
st.header("Checkbox Section")
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
  if like:
    st.write("Thanks, I like it too")
  else:
    st.write("I'm sorry, you have bad taste!")


# Radio button
st.header("Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lions", "Tigers", "Bears"))
button3 = st.button("Submit Animal")
if button3:
  st.write(animal)


# Selectbox
st.header("Selectbox Section")
animal2 = st.selectbox("What animal is your favorite?", ("Lions", "Tigers", "Bears"))
button4 = st.button("Submit Animal 2")
if button4:
  st.write(animal2)


# Multi-select
st.header("Multi-select Section")
options = st.multiselect("What animals do you like?", ["Lions", "Tigers", "Bears"])
button5 = st.button("Print Animals")
if button5:
  st.write(options)


# Slider
st.header("Slider Section")
epochs_num = st.slider("How many epochs?", 1, 100, 10)
if st.button("Slider Button"):
  st.write(epochs_num)


# Text Input
st.header("Text Input Section")
enter = ""
user_text = st.text_input("What's your favorite movie?", "Star Wars Ep. IV")
# Submits on button click or when user presses enter on keyboard
if st.button("Text Button") or (enter != user_text):
  st.write(user_text)

user_num = st.number_input("What's your favorite number?")
if st.button("Number Button") or (enter != user_text):
  st.write(user_num)

def run_sentiment_analysis(txt):
  st.write(f"Analysis Complete. {txt}")
txt = st.text_area('Text to analyze', '''It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair''')
st.write('Sentiment:', run_sentiment_analysis(txt))