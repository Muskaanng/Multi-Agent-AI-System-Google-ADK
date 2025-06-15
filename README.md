

## ✅ README.md Template

````markdown
# 🚀 Multi-Agent AI System – Google ADK

## 📌 Project Overview

This project is a multi-agent AI system built using Google ADK principles. It takes a user-defined goal, plans a task sequence, and uses cooperative agents to fulfill the goal iteratively. The UI is implemented using Streamlit.

> 🔍 **Example Goal**:  
> "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed."

---

## 🧠 System Architecture

### 🔹 Agents Used
1. **Planner Agent**  
   Parses the goal and defines task sequence.
   
2. **Launch Data Agent** (SpaceX API)  
   Fetches the next scheduled SpaceX launch.

3. **Weather Agent** (OpenWeatherMap API)  
   Retrieves current weather at the launch site.

4. **Analysis Agent**  
   Evaluates if weather conditions are favorable or may cause delay.

Each agent enriches the previous agent's output and passes it forward.

---

## 🔗 APIs Used
- [SpaceX API](https://github.com/r-spacex/SpaceX-API)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## ⚙️ Setup Instructions

### 🔐 1. Clone the Repo and Set Up API Keys
```bash
git clone https://github.com/your-username/multi-agent-ai-system.git
cd multi-agent-ai-system
cp .env.example .env
````

Edit `.env` and add:

```env
OPENWEATHERMAP_API_KEY=your_openweathermap_key
```

---

### 🛠 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🚀 3. Run the App

```bash
streamlit run main.py
```

---

## 📷 Demo Screenshot

![Multi-Agent System Screenshot](screenshots/ui.png)

---

## 📄 Evaluation Samples

See [evaluation/test\_case\_1.json](evaluation/test_case_1.json) for a full run:

```json
{
  "goal": "Find the next SpaceX launch, check weather at that location, then summarize if it may be delayed.",
  "agent_sequence": ["launch_agent", "weather_agent", "analysis_agent"],
  "final_output": "Weather conditions seem optimal for launch.",
  "goal_satisfied": true
}
```

---

## 🗂️ Folder Structure

```
multi-agent-ai-system/
├── agents/
│   ├── planner_agent.py
│   ├── launch_agent.py
│   ├── weather_agent.py
│   └── analysis_agent.py
├── main.py
├── .env.example
├── README.md
├── requirements.txt
├── evaluation/
│   └── test_case_1.json
├── docs/
│   └── logic.md
└── screenshots/
    └── ui.png
```

---

## 📌 Note

* Keep `.env` file in `.gitignore`.
* Use modular agent design to improve reusability.
* Ensure final goal is logged and evaluated.

---

## 👩‍💻 Author

**Muskaan Gupta**
M.Tech (AI & DS), KIIT University
GitHub: [github.com/Muskaanng](https://github.com/Muskaanng)

---

```

---

## 🗂️ Final ZIP Structure

Once everything is ready, zip the folder like this:

```

multi-agent-ai-system.zip
└── multi-agent-ai-system/
├── main.py
├── agents/
├── evaluation/
├── screenshots/
├── docs/
├── .env.example
├── requirements.txt
└── README.md

```


