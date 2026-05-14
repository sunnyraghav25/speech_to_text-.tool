import speech_recognition as sr

def record_and_transcribe():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("\n--- Audio Recording System ---")
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening... (Aap bolna shuru karein)")
        try:
            # Record the audio
            # phrase_time_limit set kiya hai taaki recording bahut lambi na ho
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recording stopped. Processing...")

            # Using Google Web Speech API for transcription
            text = recognizer.recognize_google(audio_data)
            
            print("\n--- Transcription Result ---")
            print(f"User said: {text}")
            
            # Optional: Save the recording for proof of work
            with open("recorded_task_output.wav", "wb") as f:
                f.write(audio_data.get_wav_data())
            print("\n(Note: Recording saved as 'recorded_task_output.wav')")

        except sr.WaitTimeoutError:
            print("Error: Koi awaaz nahi sunayi di (Timeout).")
        except sr.UnknownValueError:
            print("Error: System awaaz samajh nahi paya.")
        except sr.RequestError as e:
            print(f"Error: API connectivity issue; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    record_and_transcribe()