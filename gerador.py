import random
import string


def password(len_pass = 8):
    ascii_opc = string.ascii_letters
    numero_opc = string.digits
    pont_opc = string.punctuation
    opcoes = ascii_opc + numero_opc + pont_opc
    # oi + oiola + oioiola

    senha_user = ""

    for i in range(0, len_pass):
        digito =random.choice(opcoes)
        senha_user = senha_user + digito
    
    return senha_user

choice_user = input("Qauntos dígitos na senha?")

if choice_user.isdigit():
        choice_user = int(choice_user)
else:
     print("Tentativa Inválida")
     quit()

response = password(len_pass = choice_user)
print(f"Senha Gerada:/n{response}")


