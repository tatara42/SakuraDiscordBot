import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'
      
    if p_message == 'anime':
      return 'Naruto.'

    if message == 'roll':
        return str(random.randint(1, 6))
    
    if message == 'fcoin':
        coin = ["HEAD","TAIL"]
        return str(coin[random.randint(0,1)])

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    
    if p_message == '!hello':
        return '`Hello World!`'

    return 'I didn\'t understand what you wrote. Try typing "!help".'