import streamlit as st
import pandas as pd
import random
import numpy as np
import time


# Reading in / manipulating data 
df = pd.read_csv("emojis.csv")
df.columns = ["Emoji", "Text"]

seconds = []

for idx, row in df.iterrows():
    seconds.append(row.Text[1].lower())
    
df["Second"] = seconds


# Starting Streamlit code...
header = st.container()
text_to_emoji = st.container()
emoji_to_text = st.container()
# animation = st.container()

with header:
    st.title("Text Emoji Translator!")
    st.markdown("here is some maths!")
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


with text_to_emoji:
    text = st.text_input('Type Text Here:', '')
    text=text.lower()

    code = ""

    for i, char in enumerate(text):
        if char == ",":
            code += ","
            continue
        df_sub = df[df.Second == char]
        num = random.randint(0, df_sub.shape[0] -1)
        df_sub.reset_index(inplace=True)
        code += df_sub.Emoji[num]
    st.write('Coded message:', code)


with emoji_to_text:
    code = st.text_input('Type Emojis Here:', '')

    text = ""

    for char in code:
        if char == " ":
            text += " "
            continue
        
        if char == ",":
            text += ","
            continue 
            
        c = df.Second[df.Emoji == char].values
        text += c

    text = str(text).lstrip("['").rstrip("']")

    st.write('Translated message:', text)

# with animation: 
#     progress_bar = st.progress(0)
    # status_text = st.empty()
    # chart = st.line_chart(np.random.randn(10, 2))

# for i in range(100):
#     # Update progress bar.
#     progress_bar.progress(i + 1)

#     new_rows = np.random.randn(10, 2)

#     # Update status text.
#     status_text.text(
#         'The latest random number is: %s' % new_rows[-1, 1])

#     # Append data to the chart.
#     chart.add_rows(new_rows)

#     # Pretend we're doing some computation that takes time.
#     time.sleep(0.1)

# status_text.text('Done!')


# st.subheader("Ok - here is the .csv file")
# st.write(df.head())