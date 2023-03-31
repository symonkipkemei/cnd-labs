# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def word_censor(censor_words):
    def censor(func):

        def wrapper_func(*args, **kwargs):
            words = func(*args,**kwargs)
            words_in_text = words.split(" ")
            new_sentence = ""

            for word in words_in_text:
                if str.lower(word) in censor_words:
                    length_of_word_rem = len(word) -1
                    replace_word = ""
                    for x in range(0, length_of_word_rem):
                        replace_word += "*"
                    first_character = word[0]
                    new_word = first_character + replace_word

                    new_sentence += new_word + " "
                else:
                    new_sentence += word + " "
        
            return new_sentence
    
        return wrapper_func
    return censor




@word_censor("fuck","sex","shoot","pussy","motherfucker","fucking","cunt")
def secret_message(text):
    return text

print(secret_message("I fucking miss baby panda's pussy"))
print(secret_message("I should taste her cunt next time we fuck"))

