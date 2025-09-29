# app.py
# יוצר קוד בפייתון על פי מטרה נתונה ויוצר עבורו בדיקות יחידה (unit tests)
# באמצעות מודל שפה גדול (LLM) של OpenAI דרך LangChain   
import os
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# ------------------------------
# הגדרת API KEY
# ------------------------------
# os.environ["OPENAI_API_KEY"] = openai_key  

openai_key = os.getenv("OPENAI_API_KEY")


# ------------------------------
# הגדרת מודל
# ------------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0  # פחות יצירתיות, יותר דיוק
)

# ------------------------------
# שלב ראשון – יצירת הקוד
# ------------------------------
code_prompt = PromptTemplate(
    input_variables=["goal"],
    template="אתה מתכנת בפייתון. כתוב קוד שעונה על המטרה הבאה:\n{goal}"
)

code_chain = code_prompt | llm | StrOutputParser()

# ------------------------------
# שלב שני – יצירת בדיקות יחידה (unit tests)
# ------------------------------
test_prompt = PromptTemplate(
    input_variables=["generated_code"],
    template="כתוב קובץ unit tests בפייתון לקוד הבא:\n{generated_code}"
)

test_chain = test_prompt | llm | StrOutputParser()

# ------------------------------
# הרצת כל התהליך
# ------------------------------
if __name__ == "__main__":
    user_goal = "כתוב פונקציה שמחשבת ממוצע של רשימת מספרים"

    # קודם מפעילים את שלב יצירת הקוד
    generated_code = code_chain.invoke({"goal": user_goal})

    # מעבירים את הפלט לשלב יצירת הטסטים
    unit_tests = test_chain.invoke({"generated_code": generated_code})

    print("=== הקוד ===")
    print(generated_code)

    print("\n=== הטסטים ===")
    print(unit_tests)
