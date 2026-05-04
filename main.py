#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from agents.interviewer import ask_question
from agents.evaluator import evaluate_answer
from agents.coach import generate_feedback

def run_interview():
    print("=== AI Mock Interview Coach ===\n")

    # 🧾 User Inputs
    role = input("Enter target role (e.g., Data Analyst): ")
    background = input("Enter short background (optional): ")
    focus = input("Focus area (technical / behavioral / mixed): ")

    # 🧠 Initial Context
    context = f"""
    Candidate is applying for {role}.
    Background: {background}
    Focus area: {focus}
    """

    history = []

    # 🔁 Interview Loop
    for i in range(5):
        print(f"\n--- Question {i+1} ---")

        question = ask_question(context)
        print("\nInterviewer:", question)

        answer = input("You: ")

        # 📊 Evaluate Answer
        evaluation = evaluate_answer(question, answer)

        print("\nEvaluation:", evaluation)

        # 🧠 Store History
        turn_data = {
            "question": question,
            "answer": answer,
            "evaluation": evaluation
        }
        history.append(turn_data)

        # 🔄 Update Context (for adaptive behavior)
        context += f"""
        Question: {question}
        Answer: {answer}
        Evaluation: {evaluation}
        """

    # 🎯 Final Coaching
    print("\n\n=== FINAL FEEDBACK ===\n")
    feedback = generate_feedback(history)
    print(feedback)


# 🚀 Run
if __name__ == "__main__":
    run_interview()

