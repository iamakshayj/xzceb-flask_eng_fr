import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#translator_instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
#e2f_translator_function
def englishToFrench(englishText):
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return frenchText
#f2e_translator_function. 
def frenchToEnglish(frenchText):
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return englishText
