"""
- Dove si trova il testo?
    -Il testo viene preso da un file
    -i file vengono mostrati a video dalla console
-voglio contare i caratteri di un testo
    -con spazi e senza spazi
    -voglio contare anche le parole
    -voglio contare le frasi
    -voglio contare i paragrafi
    -voglio avere il tempo di lettura
    -voglio verificare le ripetizioni delle parole e delle lettere
-dove voglio mostrare il risultato?
    -a video sulla console
    -scriverlo su file
"""


    




"""def get_testo(text: TextIO) -> str:
    with text as f:
        content = f.read()
        return content """
    





from ui.console import print_risultato
from data.services import get_caratteri_len, get_phrase_number, get_text_len_no_space, get_words_number
from data.repository import get_file_content 

def main() -> None:
    try:
        content: str = get_file_content("file.txt")
        print(f"Frase:{content}")
        print(get_caratteri_len(content),"caratteri")
        print(get_text_len_no_space(content),"caratteri senza spazi")
        print(get_words_number(content),"parole")
        print(get_phrase_number(content),"frasi")


     
        #get_text_len_no_space((get_testo(content)))
    except ValueError as e:
        print(f"{e}")
    
    except FileNotFoundError as e: 
        print(f"{e}")

    except Exception as e:
        print(f"{e}")

    
if __name__ == "__main__":
    main()