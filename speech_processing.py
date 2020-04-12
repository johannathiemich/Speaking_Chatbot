import speech_recognition as sr
import urllib.request as url
import urllib
import logging
import json

class EasySpeechHandler():
    def __init__(self):
        logging.log(msg="Initializing speech handler", level=20)
        self._speech_rec = sr.Recognizer()

    def _internet_on(self):
        try:
            url.urlopen('http://216.58.192.142', timeout=2)
            return True
        except urllib.error.URLError:
            logging.log("No internet connection. Using offline speech recognizer")
            return False

    def recognize(self, audio_data):
        if self._internet_on():
            #TODO: does not work
            return self._speech_rec.recognize_google_cloud(audio_data, credentials_json=json.dumps("My First Project-6bdc83168a82.json"))
        else:
            return self._speech_rec.recognize_sphinx(audio_data)


#class ManualSpeechHandler():


