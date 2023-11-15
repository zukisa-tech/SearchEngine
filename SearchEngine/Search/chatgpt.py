import openai

openai.api_key = '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'

def search(query):
    response = openai.Completion.create(
        engine='davinci',
        prompt=query,
        max_tokens=100,
        n=5,
        stop=None,
        temperature=0.7
    )
    
    results = [choice['text'].strip() for choice in response['choices']]
    return results
