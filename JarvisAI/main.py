from time import strftime
import speech_recognition as sr
import os
from wikipedia import languages
import webbrowser
import openai
import datetime
import google.generativeai as genai
import random

def ai(prompt):
    #  Paste your valid Gemini API key here
    genai.configure(api_key="AIzaSyAhV4kPX6_cHvqwFiqCtTsd_gf8MCpRjAY")
    text = f"GeminiAI response for Prompt:  {prompt}  \n ************************ \n\n  "

    #  Use correct model name (v1-compatible)
    model = genai.GenerativeModel("gemini-1.5-flash")

    #  Your prompt
    prompt = prompt

    #  Generate the content
    response = model.generate_content(prompt)

    #  Show result
    # todo:wrap this in try catch block
    print(response.text)
    text = response.text
    if not os.path.exists("GeminiAi"):
        os.mkdir("GeminiAi")

    # with open(f"GeminiAi/ prompt- {random.randint(1, 947392773837727)}", "w") as f:
    with open(f"GeminiAi/ {prompt[0:30]}.txt","w") as f:
        f.write(text)

# def chat(query):

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = "en-in")
            print(f"User Said:{query}")
            return query
        except Exception as e:
             return "Something Went Wrong. Apologies from Jarvis"

if __name__ == '__main__':
    print('PyCharm')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"],["Google","https://www.google.com"],["Netflix","https://www.netflix.com "],["Amazon Prime","https://www.primevideo.com"],["Hulu","https://www.hulu.com"],["Disney+","https://www.disneyplus.com"],["Facebook","https://www.facebook.com "],["Instagram","https://www.instagram.com"],["Twitter (X)","https://www.twitter.com"],["LinkedIn","https://www.linkedin.com"],["Reddit","https://www.reddit.com "],["Pinterest","https://www.pinterest.com"],["Snapchat","	https://www.snapchat.com"],["Gmail","https://mail.google.com"],["Outlook","https://outlook.live.com"],["Yahoo Mail","https://mail.yahoo.com"],["GitHub","https://www.github.com"],["ChatGPT","https://chat.openai.com"],["Amazon","https://www.amazon.com"],["Walmart","https://www.walmart.com"],["Zoom","https://www.zoom.us"],["Khan Academy","https://www.khanacademy.org"],["Udemy","https://www.udemy.com"],["CNN","https://www.cnn.com"],["BBC","https://www.bbc.com"],["Canva","https://www.canva.com"],["Stack Overflow","https://stackoverflow.com"],["Coursera","https://www.coursera.org"],["eBay","	https://www.ebay.com"],["Etsy","https://www.etsy.com"],["edX","https://www.edx.org"],["TikTok","https://www.tiktok.com"],["Yahoo","https://www.yahoo.com"]]
        for site in sites:
            if f"Open {site[0]}".lower()  in query.lower():
                 say(f"Opening {site[0]}")
                 webbrowser.open(site[1])
        # if "Open Music" in query:
        #     # musicPath= "/Users/princypatel/Downloads/himalayan-village-flute-251427.mp3"
        #     os.system(f"open /Users/princypatel/Downloads/himalayan-village-flute-251427.mp3")
        if "the time" in query:
            musicPath= "/Users/princypatel/Downloads/himalayan-village-flute-251427.mp3"
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        elif "open facetime".lower() in query.lower( ):
            os.system(f"open /System/Applications/FaceTime.app")

        elif "open photos".lower() in query.lower( ):
            os.system(f"open /System/Applications/Photos.app")

        elif "open find my".lower() in query.lower():
            os.system(f"open /System/Applications/FindMy.app")

        elif "open passwords".lower() in query.lower():
            os.system(f"open /System/Applications/Passwords.app")

        elif "open calculator".lower() in query.lower():
            os.system(f"open /System/Applications/Calculator.app")

        elif "open messages".lower() in query.lower():
            os.system(f"open /System/Applications/Messages.app")

        elif "Using ai".lower() in query.lower():
            ai(prompt = query)

        # else:
        #     chat(query)


        # say(query)




