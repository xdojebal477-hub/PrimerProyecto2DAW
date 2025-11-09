import google.generativeai as genai

API_KEY='AIzaSyCuiZZmRQK7s5fZT_STKl04rO21_y3zaw8'

genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-2.5-flash")

chat=model.start_chat()

print("|===================================================================|")
print("|Habla con Gemini desde aqui (escribe salir para cerrar el programa)|")
print("|===================================================================|")

print("Hola soy Gemini, en que te puedo ayudar?")

while True:
    user_input=input("Tu:")
    if user_input.lower()=='salir':
        break
    response=chat.send_message(user_input)
    print(f"Gemini: {response.text}")