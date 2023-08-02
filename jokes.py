import pyjokes
import talk

joke = pyjokes.get_joke()

print(joke)
talk.talk(joke)