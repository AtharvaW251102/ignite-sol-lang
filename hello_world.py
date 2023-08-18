from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
port = 5000

class Greeting:
    def __init__(self, language, message):
        self.language = language
        self.message = message

class EnglishGreeting(Greeting):
    def __init__(self):
        super().__init__('English', 'Hello world')

class FrenchGreeting(Greeting):
    def __init__(self):
        super().__init__('French', 'Bonjour le monde')

class HindiGreeting(Greeting):
    def __init__(self):
        super().__init__('Hindi', 'Namastey sansar')

class GreetingService:
    def __init__(self):
        self.greetings = {
            'English': EnglishGreeting(),
            'French': FrenchGreeting(),
            'Hindi': HindiGreeting()
        }

    def get_greeting(self, language):
        return self.greetings.get(language, Greeting(language, 'Hello world'))

greeting_service = GreetingService()

@app.route('/hello')
def hello():
    language = request.args.get('language', 'English')
    greeting = greeting_service.get_greeting(language)
    return greeting.message

if __name__ == '__main__':
    app.run(port=port)
