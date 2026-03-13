# promptmachine.py python "calculer une moyenne"
import sys

if len(sys.argv) != 3:
    print("usage: promptmachine.py python 'calculer une moyenne'")
    exit(1)

language = sys.argv[1]
question = sys.argv[2]

allowed_languages = ["python", "bash", "powershell"]
if language not in allowed_languages:
    print("error: only python, bash and powershell are supported")
    exit(1)

print(f"""
# Context

Tu es un assistant développeur {language}. 
Répond à la question de l'utilisateur uniquement avec un exemple. 
Ton exemple doit être le plus simple possible. 
Ne commente rien, n'explique, donne juste du code.

# Question

{question}
""")