import streamlit
st.title(f"Question Paper")
st.subheader(f"Grade: {Level}    PE: {periodic_evaluation}")
st.markdown("---")

question_number = 1

for section_title, q_type in [("I. Reading words 1", "three_letter_words"),
                              ("II. Reading words 2", "four_letter_words"),
                              ("III. Reading letters", "letters_1")]:
    st.markdown(f"**{section_title}**")

    subset = filtered[filtered["Question Type"] == q_type].sample(n=5, replace=True)
    
    for _, row in subset.iterrows():
        st.write(f"{question_number}. {row['Question']}")
        question_number += 1
    
    st.markdown("---")
