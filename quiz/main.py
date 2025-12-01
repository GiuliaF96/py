
def mostra_feedback(messaggio : str) -> None:
    simbol : srt = "*"*30
    print(f"""
{simbol}
{messaggio}
{simbol}
""")
def is_risposta_esatta(scelta : str) -> bool:
    if scelta.upper() == "C":
          return True
    else: 
          return False
 

def genera_feedback(is_corretta: bool) -> str:
    
     if is_corretta() == True:
          return "Hai indovitato!"
     else: 
          return "Non hai indovinato.Riprova"





def valida_scelta(scelta : str) -> bool:
   scelta_tmp = scelta.upper()
   if scelta_tmp == "A" or scelta_tmp == "B" or scelta_tmp == "C" or scelta_tmp == "D":
    return True
   else:
    return False 


def mostra_domanda() -> None:
     
    print(
        
    """

    Chi parteciperà a Sanremo 2026?

    A. Nayt
    B. La Nina
    C. J-AX
    D. Rocco Papaleo

    """

    )


def raccogli_risposta() -> str:
        risposta: str = input("Inserisci la tua scelta: ")
        return risposta


def main():
    is_risposta_corretta: bool = False 
    
    while True:

        mostra_domanda()

        risposta_da_validare: str = raccogli_risposta()
        risposta_validata: bool = valida_scelta(risposta_da_validare)
        feedback : str = ""

        if risposta_validata == True:
            is_risposta_corretta = is_risposta_esatta(risposta_da_validare)
            feedback = genera_feedback(is_risposta_corretta)
            
        else:
            feedback = "inserisci solo la risposta tra le opzioni elencate"


        mostra_feedback(feedback)
        if is_risposta_corretta == True:
            break

main()