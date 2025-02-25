from deep_translator import GoogleTranslator

text = input("Enter Text: ")
language = input("Enter Language Code (e.g., ur for Urdu, en for English): ")

# Ensure source is Urdu
result = GoogleTranslator(source='ur', target=language).translate(text)

print("Translated Text:", result)