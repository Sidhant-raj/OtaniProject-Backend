import cv2 as cv
import pandas as pd
import pytesseract
from PIL import Image
from langdetect import detect
from translate import Translator
import LanguageSelector
import SplitSentences as Sp


def detect_and_translate(text, target_language='en'):
    detected_language = detect(text)
    translator = Translator(from_lang=detected_language, to_lang=target_language)
    translated_text = translator.translate(text)

    return translated_text, detected_language, target_language


def StarterFunction(choice: str, target_language: str, fileName):
    global sentence, translated_text
    target_lang = "hi"
    Path = "images/" + fileName
    Img = cv.imread(Path, 0)
    # Img = cv.resize(Img, (1080, 1080))
    # cv.imshow("Image", Img)
    _, binary_image = cv.threshold(Img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # Key = cv.waitKey(0)
    # custom_config = r'--oem 3 --psm 6'
    # input_text = pytesseract.image_to_string(Img)
    input_text = pytesseract.image_to_string(Image.fromarray(binary_image))  # config=custom_config)

    sentences = Sp.split_into_sentences(input_text)

    # print("Do you want to Update Languages: ")
    # print("1. Yes")
    # print("2. No")

    # choice = input("Your Choice: ")

    if choice == 'Yes' or choice == 'yes':
        LanguageSelector.GetLanguages()

    LanguageDF = pd.read_csv('LanguageSelector.csv')

    for Index in LanguageDF.index:
        if target_language.lower() == (LanguageDF['Language Name'][Index]).lower():
            target_lang = LanguageDF['Langauge Codes'][Index]
            break
    translated_texts = ""
    original_sentences = ""

    for i, sentence in enumerate(sentences):
        # print(f"Sentence {i + 1}: {sentence}")
        translated_text, detected_language, target_language = detect_and_translate(sentence, target_lang)
        translated_texts += translated_text
        original_sentences += sentence

    return translated_texts, original_sentences

    # cv.destroyAllWindows()
