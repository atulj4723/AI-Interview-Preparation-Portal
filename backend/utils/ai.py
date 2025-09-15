from google import genai
def AIClient(content,config):
    client=genai.Client()
    response = client.models.generate_content(model="gemini-2.0-flash",contents=content,config=config)
    return response
