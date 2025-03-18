# Conversational Weather & Reasoning Agent

**Setup Instructions**
### **Prerequisites**
- Python 3.8 or later
- A virtual environment (recommended)
- Required API keys:
  - Groq API key for the LLM
  - Weather API key for real-time weather retrieval
- `.env` file containing:
  ```ini
  API_KEY=your_groq_api_key
  BASE_URL=https://api.groq.com/openai/v1
  LLM_MODEL=llama-3.3-70b-versatile
  WEATHER_API_KEY=your_weather_api_key
  ```

### **Installation**
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/conversational-agent.git
   cd conversational-agent
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the agent:
   ```sh
   python conversational_agent.py
   ```

5. To evaluate agents, run:
   ```sh
   python evaluation.py
   ```

---
## 🛠 **Implementation Overview**
This project implements a conversational agent capable of:
- Retrieving weather information via an API
- Performing mathematical calculations
- Providing reasoning-based responses using Chain of Thought (CoT) and ReAct strategies
- Logging conversations and enabling user evaluation

### **Key Components**
- `conversational_agent.py`: Main agent logic with user interaction
- `bonus_evaluation.py`: Evaluates agent responses and logs them to a CSV
- `tools.py`: Functions for weather retrieval, calculations, and web search

---
## 💬 **Example Conversations**

### **Basic Agent**
```
You: What is the weather in New York?
Weather Assistant: The current weather in New York is Sunny, 7.2°C (45.0°F).
```

### **Chain of Thought Agent**
```
You: What is 25 + 67?
Weather Assistant: Let's break it down step by step. 25 plus 67 equals 92.
```

### **ReAct Agent**
```
You: Explain climate change.
Thought: To explain climate change, I need to define it and discuss its causes and effects.
Action: Retrieve general knowledge.
Observation: Climate change is the long-term warming of the planet due to greenhouse gases.
Final Answer: Climate change is caused by CO2 emissions and leads to extreme weather.
```

---
## 📊 **Analysis: Effect of Reasoning Strategies on Response Quality**
| Agent Type  | Strengths | Weaknesses |
|-------------|-----------|-------------|
| **Basic**   | Fast responses, good for direct queries | Lacks deeper reasoning, struggles with multi-step problems |
| **Chain of Thought** | Provides step-by-step explanations | Can be verbose, may overcomplicate simple queries |
| **ReAct**   | Uses tools efficiently, shows reasoning | Slightly slower due to multiple steps |

### **Key Findings:**
- **Basic Agent** is ideal for factual, one-step answers.
- **Chain of Thought** improves numerical reasoning and step-by-step breakdowns.
- **ReAct Agent** dynamically decides when to use tools, making it the most adaptable.

---
**Challenges & Solutions**
### **1. Handling Different Message Formats**
- **Issue**: `ChatCompletionMessage` objects vs. dictionaries caused errors.
- **Solution**: Implemented type checking before accessing attributes.

### **2. Logging the Correct Assistant Response**
- **Issue**: CSV logs contained full conversation history instead of final response.
- **Solution**: Extracted only the most recent assistant response for logging.

### **3. Ensuring API Calls Work Consistently**
- **Issue**: Weather API occasionally failed due to location formatting.
- **Solution**: Standardized location formatting before making API requests.

---
**Conclusion**
This project successfully implemented a conversational AI capable of reasoning and using external tools. The different reasoning strategies (Basic, Chain of Thought, and ReAct) provided insights into the strengths and trade-offs of various LLM-based decision-making approaches.

