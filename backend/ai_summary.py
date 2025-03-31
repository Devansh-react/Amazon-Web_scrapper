import openai


API_KEY = "AIzaSyAiJaYkfOk8aHjUw0-q2zGPopQ12pFiumM"
openai.api_key = API_KEY

def generate_ai_summary(reviews):
    if not reviews:
        return "No reviews available for summary."

    prompt = f"Summarize the following customer reviews in a short, engaging paragraph:\n{reviews}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  
            messages=[{"role": "system", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message["content"]  
    except Exception as e:
        print("AI Summary Error:", str(e))
        return "AI Summary Failed. Please try again later."

