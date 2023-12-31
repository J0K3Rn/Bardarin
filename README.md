# Bardarin

Project is still in a early state. Currently experiencing multiple issues with using the 3rd-party Bard API. See my Mandarin-Learning-Chatbot which utilizes ChatGPT! https://github.com/J0K3Rn/Mandarin-Learning-Chatbot

Utilize LLM’s to help in your language studies! Uses Google's Bard to generate sentences from the 1000 most common words in Chinese (Mandarin) to study. Provides English translations and pinyin. Generated Sentences are saved to an output file for further review.

Bard API: https://github.com/dsdanielpark/Bard-API

Builds upon many aspects from my Chinese-Flash-Cards repository: https://github.com/J0K3Rn/Chinese-Flash-Cards 

Todo:
- Use Selenium to open up Bard and automate cookie grabbing process
- Create app for UI
- Implement Google Voice (Narrator)
- Save generated Bard output to csv
- Gameify the app
- Implement Google's Speech to Text so user can practice pronunciation
- Implement the ability to click on characters to pop up the direct translation (similar to what Duolingo does)

How to run:
- Python 3.11.4 is highly recommended to resolve tkinter issues
- Download repository
- Open downloaded repository with a command line interface
- run `pip install bardapi`
- Some work must be done by YOU to fully set up the Bard API
- Open Bard in your browser (Chrome Preferred) `https://bard.google.com/`
- Open the Web Developer Tools (Three dots near top right of window -> More Tools -> Developer Tools)
- In Developer Tools go to Application tab -> Expand 'Cookies' -> Click on https://bard.google.com/
- A list should pop up where you can see many of the cookies (Many are named `__Secure-`)
- Replace the values for token, __Secure-1PSID, __Secure-1PSIDCC and __Secure-1PSIDTS in main.py
- DO NOT OPEN UP A NEW WINDOW FOR BARD OR YOU WILL HAVE TO REDO THESE STEPS
- Keep you browser session open while running the program?
- run `python main.py`

Working example in console:

![alt text](https://github.com/J0K3Rn/Bardarin/blob/main/screenshots/console_example.png?raw=true) 
