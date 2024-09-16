import whisper
import logging
import ollama
from llama_index.core import PromptTemplate

class AiDescription:
    def __init__(self) -> None:
        """ 
        To create automatic descriptions from audio-to-text transcriptions.
        
        ---
        Args:
        
        ---
        Returns:
        """
        self.template = (
                "Fornecemos as informações de contexto abaixo. \n"
                "---------------------\n"
                "{context_str}"
                "\n---------------------\n"
                "A partir desta informação, por favor responda a pergunta: {query_str}\n"
            )
        
        self.query_data = """\
                            Você é um criador de conteúdo expert em criar descrições engajadoras para vídeos a partir de textos.\
                            Crie três descrições adaptadas para plataformas de vídeo em português-BR sendo que a primeira descrição deve ser generalista,\
                            a segunda direta e a terceira descritiva. \

                            EXEMPLO PARA RESPOSTA:\   
                            Descrição 1 (generalista): Neste vídeo...\
                            Descrição 2 (direta): Neste vídeo...\ 
                            Descrição 3 (descritiva): Neste vídeo..."""

        self.qa_template = PromptTemplate(self.template)
        self.text_to_prompt = ''
        
        

    def speech_to_text(self, audio_file = "./source/audio/transcription.mp3", verbose = True) -> object:
        """ 
        To process audio to texts.
        
        ---
        Args:
            audio_file - audio path/data to process
            verbose - display results in terminal
        
        ---
        Returns: 
            A data object.
        """
        with open("./source/output/video_transcription.txt", "w") as file:
            model = whisper.load_model("medium")
            result = model.transcribe(audio_file)
            file.write(result["text"])
            
            if verbose:
                print("Text transcription", result["text"])
                
            return result

    def description_generation(self, transcription = "./source/output/video_transcription.txt")-> object:
        """ 
        To generate description.
        
        ---
        Args:
            transcription - transcription file to process
            
        ---
        Returns: 
            A data object.
        """
        if type(transcription) == type("a"):
            with open(transcription, "r") as text_data:
                self.text_to_prompt = text_data.read()
        else: 
            self.text_to_prompt = transcription["text"]       
        
        prompt = self.qa_template.format(context_str = self.text_to_prompt, query_str = self.query_data)

        response = ollama.chat(model="dolphin-llama3:8b", messages=[{
                'role': 'user',
                'content': prompt,
            },
        ])       
        
        with open("./source/output/video_description.txt", "w") as video_description:
            video_description.write(response['message']['content'])
            
        return response        

def pipeline():
    """ 
    To run.
    
    ---
    Args:
        
    ---
    Returns: 
    """
    description = AiDescription()
    transcription = description.speech_to_text()   
    description.description_generation(transcription)     
       
if __name__ == '__main__':
    pipeline()