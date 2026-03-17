import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

from models.structure import CodeResponse

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0,
    anthropic_api_key=ANTHROPIC_API_KEY
)

structured_llm = llm.with_structured_output(CodeResponse)

prompt = ChatPromptTemplate.from_template(
"""
You are a code analyzer or Senior Developer.

Explain the code in 2-4 sentences.
note: There might be multiple code snippets, so analyze each one separately and provide a detailed explanation for each.

Also provide:
- Time complexity
- Space complexity
- Optimized code

Analysis:
{analysis}

Code:
{code}
"""
)

chain = prompt | structured_llm

def explain_code(code: str, analysis: dict):
    
    try:
        response = chain.invoke({
            "code": code,
            "analysis": analysis
        })

    except Exception as e:
        print(f"Error occurred while explaining code: {e}")
        return None
      
    data = []
    
    for result in response.get("results", []):
        comparison = {
            "original": code,
            "optimized": result.get("optimized_code") if result else "Optimized code not available"
        }

        item = {
            "analysis": analysis if analysis.get("error") is None else analysis.get("error"),
            "explanation":  result.get("Explanation") if result else "Explanation not available",
            "time_complexity": result.get("time_complexity") if result else "Time complexity not available",
            "comparison": comparison
        }
        
        data.append(item)

    return data