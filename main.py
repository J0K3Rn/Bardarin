import requests
from bardapi import Bard, SESSION_HEADERS
import pandas as pd
import tkinter as tk

session = requests.Session()

# <--> User Intervention Needed Here! <--> #
# All of these cookies are temporary and reset occasionally
# Replace the below x's with your Google Bard cookies!
# Follow the steps in the README
token = "aQgPcrTJda3yp4rrzZx67jQPd0OuoprkWXtov-91dz6Td9DOBCpTtRa5n7AFlE8ajNigww."  # token is same as __Secure-1PSID
session.cookies.set("__Secure-1PSID", "aQgPcrTJda3yp4rrzZx67jQPd0OuoprkWXtov-91dz6Td9DOBCpTtRa5n7AFlE8ajNigww.")
session.cookies.set("__Secure-1PSIDCC", "APoG2W_QjBqx0EM1BoUWusN2OsupNZ7jAMI0U55sUAeOkYfMu0uDzMtY9l3BPUoa0nW4NbCoafo")
session.cookies.set("__Secure-1PSIDTS", "sidts-CjIBSAxbGYJRZ8IhZ9LuspZGbJWiWnbr-yJfgyiUCEwA3aGCdRPDhrk6-cpbBZi4FY4gLxAA")
# And that's it! Now you can run the program!
session.headers = SESSION_HEADERS

#bard = Bard(token=token, session=session)

# BACKGROUND_COLOR = "#FFFFFF"
#
# # Read csv and convert to dictionary
# try:
#     df = pd.read_csv('data/words_to_learn.csv')
# except FileNotFoundError:
#     df = pd.read_csv('data/chinese_words.csv')
# to_learn = df.to_dict(orient="records")
#
#
# class App(object):
#     def __init__(self):
#         window.title("Bardarin")
#         window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#
#         self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#         # image_img = PhotoImage(file="images/images.png")
#         # self.card_back_img = tk.PhotoImage(file="images/card_back.png")
#         # self.card_front_img = tk.PhotoImage(file="images/card_front.png")
#         # self.card_image = self.canvas.create_image(400, 263, image=self.card_front_img)
#         # self.card_title = self.canvas.create_text(400, 150, fill="#000000", font=("Ariel", 40, "italic"))
#         # self.card_word = self.canvas.create_text(400, 263, fill="#000000", font=("Ariel", 60, "bold"))
#         # self.card_pinyin_label = self.canvas.create_text(400, 363, fill="#000000", font=("Ariel", 60, "bold"))
#         # self.canvas.itemconfig(self.card_pinyin_label, state='hidden')
#         # self.canvas.bind("<Button-1>", self.on_click)
#         #
#         # Buttons
#         self.correct_img = tk.PhotoImage(file="images/right.png")
#         self.incorrect_img = tk.PhotoImage(file="images/wrong.png")
#         self.volume_img = tk.PhotoImage(file="images/volume_icon.png")
#         self.volume_img = self.volume_img.subsample(10)
#         self.wrong_button = tk.Button(highlightbackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, image=self.incorrect_img)#, command=self.incorrect)
#         self.correct_button = tk.Button(highlightbackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, image=self.correct_img)#, command=self.correct)
#         self.show_pinyin_button = tk.Button(window, highlightbackground="#FFFFFF", bg="#FFFFFF", text="Show Pinyin")#, command=self.show_pinyin)  # , height=3, width=10)
#         self.narrator_button = tk.Button(window, highlightbackground="#FFFFFF", bg="#FFFFFF", image=self.volume_img)#, command=self.narrate)
#
#         # Grid Layout
#         self.canvas.grid(column=0, row=0, columnspan=15, rowspan=10)
#         self.wrong_button.grid(column=5, row=10)
#         self.correct_button.grid(column=9, row=10)
#         self.show_pinyin_button.grid(column=7, row=7)
#         self.narrator_button.grid(column=7, row=8)
#         #
#         # # Set up flashcards
#         # self.next_card()
#
#
# window = tk.Tk()
# a = App()
#
# window.mainloop()

# Bard sometimes provides explanations. Don't want this to mess with the parser
#print(bard.get_answer("Generate 3 complex sentences in Chinese using the character 我. Do not provide explanations."))

# Trimming the data so we can use it.
a = {'content': 'Sure, here are 3 complex sentences in Chinese using the character 我:\n\n1. 我很高兴今天见到你。 (Wǒ hěn gāoxìng jīntiān jiàn dào nǐ.) - I am very happy to meet you today.\n2. 我希望明天能和你一起去旅行。 (Wǒ xīwàng míngtiān néng hé nǐ yīqǐ qù lǚxíng.) - I hope we can go on a trip together tomorrow.\n3. 我会尽力完成这项任务。 (Wǒ huì jìnliàng wánchéng zhè xiàng rènwù.) - I will do my best to complete this task.\n\nI hope this is what you are looking for. Let me know if you have any other questions.', 'conversation_id': 'c_a09aa485e6283581', 'response_id': 'r_a09aa485e628396c', 'factuality_queries': None, 'text_query': ['3 complex sentences in Chinese using the character 我', 1], 'choices': [{'id': 'rc_a09aa485e6283d03', 'content': ['Sure, here are 3 complex sentences in Chinese using the character 我:\n\n1. 我很高兴今天见到你。 (Wǒ hěn gāoxìng jīntiān jiàn dào nǐ.) - I am very happy to meet you today.\n2. 我希望明天能和你一起去旅行。 (Wǒ xīwàng míngtiān néng hé nǐ yīqǐ qù lǚxíng.) - I hope we can go on a trip together tomorrow.\n3. 我会尽力完成这项任务。 (Wǒ huì jìnliàng wánchéng zhè xiàng rènwù.) - I will do my best to complete this task.\n\nI hope this is what you are looking for. Let me know if you have any other questions.']}, {'id': 'rc_a09aa485e62830ee', 'content': ["Sure, here are 3 complex sentences in Chinese using the character 我:\n\n* 我喜欢吃中国菜，但是我不会做。 (Wǒ xǐhuì chī zhōngguó cài, dànshì wǒ bù huì zuò.) - I like to eat Chinese food, but I don't know how to cook.\n* 我知道你很忙，但是我还是想和你聊天。 (Wǒ zhīdao nǐ hěn máng, dànshì wǒ hái shì xiǎng hé nǐ liáotian.) - I know you're busy, but I still want to talk to you.\n* 我希望有一天我可以去中国旅行。 (Wǒ xīwàng yǒu yītiān wǒ kěyǐ qù zhōngguó lǚxíng.) - I hope that one day I can travel to China.\n\nI hope these sentences are helpful!"]}, {'id': 'rc_a09aa485e62834d9', 'content': ['Sure, here are 3 complex sentences in Chinese using the character 我:\n\n* 我知道你在想什么。 (Wǒ zhīdao nǐ zài xiǎng shénme.) - I know what you are thinking.\n* 我希望你能帮我。 (Wǒ xīwàng nǐ néng bāng wǒ.) - I hope you can help me.\n* 我很高兴见到你。 (Wǒ hěn gāoxìng jiàn dào nǐ.) - I am very happy to see you.\n\nThese sentences are all complex because they have two or more clauses. The first sentence has a main clause ("我知道") and a subordinate clause ("你在想什么"). The second sentence has a main clause ("我希望") and a subordinate clause ("你能帮我"). The third sentence has a main clause ("我很高兴") and a subordinate clause ("见到你").\n\nI hope this is what you were looking for. Let me know if you have any other questions.']}], 'links': [], 'images': set(), 'program_lang': None, 'code': None, 'status_code': 200}
b = a['content'].split("\n")[2:5]

bard_response = a['content'].split('\n')[0]
bard_prompt = "Generate 3 complex sentences in Chinese using the character 我. Do not provide explanations."

# Print
print(f"Prompt: {bard_prompt}")
print(f"Bard Response: {bard_response}")
print("Bard wrangled data below:")
for i in b:
    #print(i)
    i = i[3:]
    pinyin_start_index = i.find('(')
    pinyin_end_index = i.find(')')
    # Could probably do some checks to verify this isn't a parenthesis provided by Bard in Chinese. Check if character before is in Chinese.
    chinese = i[:pinyin_start_index-1]
    print(chinese)
    pinyin = i[pinyin_start_index+1:pinyin_end_index]
    print(pinyin)
    english = i[pinyin_end_index+4:]
    print(english)
# We don't care about the pinyin or english translation.. we can do that ourselves.. however it would really be easier
#print(b)
