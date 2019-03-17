from google.cloud import translate

def translate_text(text):
    language = input("Please select a language: English (en), French (fr), Spanish (es) Geerman (de): ")
    client = translate.Client()
    output = client.translate(text, target_language=language)
    return output

print(translate_text("hello"))
