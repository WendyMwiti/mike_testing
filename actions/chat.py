import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input("Hello, how are you today?")

def gpt3(text):
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
    response = completion.choices[0].text
    return response

response_text = gpt3(prompt)
print(response_text)
