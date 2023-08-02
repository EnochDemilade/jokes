# import modules
import pyjokes
import talk

# get joke
joke = pyjokes.get_joke()

# print joke
print(joke)
talk.talk(joke)
