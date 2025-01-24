# https://launchschool.com/exercises/fddf66ac

def main():

    def get_prompt():
        
        while True:
            noun = input("Enter a noun: ")
            verb = input("Enter a verb: ")
            adjective = input("Enter an adjective: ")
            adverb = input("Enter an adverb: ")
            
            print()
            tell_story(noun, verb, adjective, adverb)
            print()

    def tell_story(noun, verb, adjective, adverb):
        print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
        print(f"The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.")
        print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")

    get_prompt()

if __name__ == "__main__":
    main()