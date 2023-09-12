#modelo manual criado por ghost404
import openai
openai.api_key="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"
class Responder:
    def responder_chat(p):
        if "herlay" in p:
            return "Herlay è uma chatbot de inteligencia artificial criado pela a equipa Mtevolution , um grupo mocambicano"
        elif "diqui" in p:
                return "Se esta falar de Dique joaquim , ele é um jovem mocambicano  com um talento muito grande na programacao . Ele è do norte do pais em Niassa tem uma equipa em Maputo e angola"
        elif "danca" and "ouro" in p:
             return "A danca de ouro è um tipo de danca que um Repper Moçambicano ,Lil wayne de moz inventou ,Neste caso nao tenho mais informacoes sobre a danca"
        elif "quem" and "criou" in p:
             return "Fui criado por Diqui joaquim simplesmente ghost404 ,ele é um dos programadores da Mt evolution o grupo fundado por jose em Maputo."
        elif "membros" and "evolution" in p:
            return "Claro, aqui estao os membros da mt evolution.  Jose,Sandino, Dique, Jorge Claro que podem existir outos mas nao tenho acesso a informaçao em tempo real."
        else:
               resposta = openai.ChatCompletion.create(
               model="gpt-3.5-turbo",
       messages=[{"role": "system", "content": "Você é um chatbot"},
        {"role": "user", "content": p}])
        return resposta.choices[0].message["content"]
  
              
    