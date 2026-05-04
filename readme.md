\# 🎯 AI Mock Interview Coach (Multi-Agent System)



An AI-powered mock interview system that simulates realistic interviews, evaluates responses, and provides structured coaching feedback.



Built as a multi-agent system using LLMs, this project demonstrates prompt engineering, agent orchestration, and adaptive conversational design.



\---



\## 🚀 Features



\- 🧠 \*\*Multi-Agent Architecture\*\* (Interviewer, Evaluator, Coach)

\- 🔁 \*\*Adaptive Interview Flow\*\* (dynamic follow-ups based on answers)

\- 📊 \*\*Structured Evaluation\*\* (multi-dimensional scoring)

\- 🎯 \*\*Personalized Feedback\*\* (actionable coaching insights)

\- 💬 \*\*Realistic Conversations\*\* (handles vague, weak, or strong responses)



\---



\## 🏗️ Architecture Overview



The system consists of three distinct agents:



\### 1. Interviewer Agent

\- Conducts the interview

\- Asks questions dynamically

\- Adapts based on previous responses and evaluation signals



\### 2. Evaluator Agent

\- Analyzes each candidate response

\- Outputs structured JSON:

&#x20; - clarity

&#x20; - depth

&#x20; - relevance

&#x20; - confidence

\- Suggests:

&#x20; - follow-up direction

&#x20; - difficulty adjustment



\### 3. Coach Agent

\- Reviews full interview transcript

\- Generates structured feedback:

&#x20; - strengths

&#x20; - weaknesses

&#x20; - missed opportunities

&#x20; - actionable improvements



\---



\## 🔁 Orchestration Flow

User Input → Interviewer starts



Loop (5–7 turns):

Interviewer → asks question

User → answers

Evaluator → evaluates answer

Context updated → influences next question



End:

Coach → generates final feedback


\---



\## 📁 Project Structure

mock\_interview/

│

├── agents/

│ ├── init.py

│ ├── interviewer.py

│ ├── evaluator.py

│ └── coach.py

│

├── prompts/

│ ├── interviewer.txt

│ ├── evaluator.txt

│ └── coach.txt

│

├── main.py

├── requirements.txt

├── README.md

├── .env

└── .gitignore


\---



\## ⚙️ Setup Instructions



\### 1. Clone the repository



```bash

git clone <your-repo-link>

cd mock\_interview
pip install -r requirements.txt
OPENAI\_API\_KEY=your\_api\_key\_here

Run the application

python main.py

## 🔐 API Key Note

This project uses the OpenAI API.

⚠️ The API key is not included in this repository for security reasons.

To run the project:
1. Create a `.env` file in the root directory
2. Add your API key:


