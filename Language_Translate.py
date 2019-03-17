def translate_text(text):
    from google.cloud import translate
    client = translate.Client()
    test = True
    while test:
        try:
            language = input("Please select a language: English (en), French (fr), Spanish (es) German (de): ")
            output = client.translate(text, target_language=language)
            test = False
        except:
            print("Invalid language selection, please input a valid language code")
    return output['translatedText']
