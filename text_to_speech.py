import pyttsx3

def text_to_speech():
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Get user input for the text
    text = input("Enter the text you want to convert to speech: ")

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (default is 200)
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Get available voices
    voices = engine.getProperty('voices')
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index}: {voice.name}")

    # Choose a voice
    voice_choice = int(input("Enter the voice number you want to use: "))
    engine.setProperty('voice', voices[voice_choice].id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech()
