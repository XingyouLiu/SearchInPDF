from openai import OpenAI
client = OpenAI()

class IntentService():
    def __init__(self):
        pass

    def get_intent(self, user_question: str):
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{
              "role": "user",
              "content": [
                {
                  "text": f"Extract the key words from the following question: {user_question}. \
                  Do not answer anything else, only extract keywords.",
                  "type": "text"
                }
              ]
            }],
        )

        return response.choices[0].message.content
