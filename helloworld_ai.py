import groq

client = groq.Client(api_key="YOUR_GROQ_API_KEY_HERE")

def generate_hello_world():
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Use an available Groq model
        messages=[
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": "Generate a unique and fun 'Hello World' message and just give one which you think is the most creative"}
            
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print(generate_hello_world())