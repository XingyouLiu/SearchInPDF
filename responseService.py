from openai import OpenAI
client = OpenAI()

class ResponseService():
    def __init__(self):
        pass

    def generate_response(self, facts, user_question):
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{
              "role": "user",
              "content": [
                {
                  "text": f"Based on the following FACTS, give an answer to the QUESTION. \
                    FACTS: {facts}. QUESTION: {user_question}",
                  "type": "text"
                }
              ]
            }],
        )
         #extract the response
        return (response.choices[0].message.content)