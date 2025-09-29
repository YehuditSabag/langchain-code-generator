# LangChain Code Generator 🧩

This project demonstrates a simple **LangChain pipeline** with two phases:

1. **Code Generation**  
   The user provides a goal (e.g., *"write a function to calculate the average of a list"*).  
   LangChain + OpenAI generate Python code that solves the goal.

2. **Unit Test Generation**  
   The generated code is passed into another LangChain chain that creates Python unit tests for the code.

---

## ⚙️ Requirements

- Python 3.10+
- LangChain
- OpenAI API Key

Install dependencies:
```bash
pip install langchain langchain-openai pytest
