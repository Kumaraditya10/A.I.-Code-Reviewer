import subprocess
from google import genai
import os

def getDiff():
    diff = subprocess.check_output(["git", "show"], text=True)
    return diff



client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    diff = getDiff()
    prompt = f"Review the following code changes and provide feedback:\n\n{diff}"
    responce = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    print("Code Review Feedback")
    print(responce.text)
    
    
main()