import speech_recognition as sr

def func():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("what to print?")
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        s = r.recognize_google(audio)
        ans = "print('" + s + "')\n"

        f = open("new.py","a")
        f.write(ans)
        f.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def define_func():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("what are the parameters")
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        s = r.recognize_google(audio)
        ans = "print('" + s + "')\n"

        f = open("new.py","a")
        f.write(ans)
        f.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

m = {
     "hash" : "#",
     "colin" : ":",
     "slash" : "/",
     "enter" : "\n",
     "flash" : "/",
     "tick" : "(",
     "tik" : "(",
     "tok" : ")",
     "talk" : ")",
     "sep" : ",",
     "tab" : "\t",
     "less" : "<",
     "lakh" : "<",
     "more" : ">",
     "equal" : "=",
    }

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    s = r.recognize_google(audio)
    print(s)
    ls = s.split()
    ans = ""
    for word in ls:
        word = word.lower()
        if word in m:
            ans = ans + m[word] + " "
        elif word == "print":
            func()
        else:
            ans = ans + word + " "

    f = open("new.py","a")
    f.write(ans)
    f.close()
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
