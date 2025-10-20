import pywhatkit as pwk

phone_number = '+34654983649'
message = 'Hola, este es un mensaje de prueba enviado desde Python usando pywhatkit!'
pwk.sendwhatmsg(phone_number, message, 0, 0)