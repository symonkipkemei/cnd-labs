# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.


from datetime import datetime


def log_time(func):
    def wrapper(*args,**kwargs):
        print(f"{func.__name__} run at {datetime.now()}")
        return func(*args,**kwargs)
    return wrapper
        
@log_time
def word_censor(*censor_words):
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


