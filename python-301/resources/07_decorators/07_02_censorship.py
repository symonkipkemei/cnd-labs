# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


#identify censor words

censor_words = ["fuck","sex","shoot","pussy","motherfucker","fucking"]

def censor(func):
    def wrapper_func(text):
        words_in_text = text.split(" ")
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


@censor
def secret_message(text: str):
    return text

print(secret_message("I fucking miss baby panda's pussy"))

