import json
import openai

def lambda_handler(event, context):
    # retrieve the user's request
    request = event['request']
    # check if the request is for the AskAssistantIntent
    if request['type'] == 'IntentRequest' and request['intent']['name'] == 'AskAssistantIntent':
        # retrieve the user's question from the request
        question = request['intent']['slots']['Question']['value']
        # send the question to me using the OpenAI API
        openai.api_key = "YOUR_API_KEY"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
        )
        # retrieve the response from me
        answer = response['choices'][0]['text']
        # create the Alexa response
        alexa_response = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": answer
                },
                "shouldEndSession": True
            }
        }
        return alexa_response
    # return an error response if the request is not recognized
    else:
        return {
            "error": "Invalid request"
        }
