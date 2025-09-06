
from ollama import chat 
from ollama import ChatResponse


class Email_AI:
    def __init__(self,LLm_Model='gemma2:2b'):
        self.Input = None
        self.system_msg = '''You are an email assistant. Here are the instructions for you.
                            1. Take user input as a context and generate three different emails. Each has three different styles: Professional, Casual, Friendly.
                            2. Use regular email format.
                            3. Also with the input you will receive whether you are constructing a new email or replying to one; Input will start with either send or reply.
                            4. Do not generate anything that's not part of those three emails. Use separators in your output to divide the emails so it could easily be extracted.
                            5. Example separators: #ProfessionalStart ... #ProfessionalEnd, #CasualStart ... #CasualEnd, #FriendlyStart ... #FriendlyEnd.'''
        self.email = None
        self.Model = LLm_Model
        self.output = None
    
    def Generate_email(self,user_input: str)-> dict:
        self.Input = user_input
        messages = [
            {'role':'system','content':self.system_msg},
            {'role':'user','content':self.Input}
        ]
        response: ChatResponse = chat(self.Model,messages=messages)
        self.email = response.message.content 
        print(self.email)
        
        return self.Parse_email()

    def Parse_email(self)->dict:
        
        email = {}


        for style in ['Professional','Casual','Friendly']:
            start_tag = f"#{style}Start"
            end_tag = f"#{style}End"
            text = self.email.split(start_tag)[1].split(end_tag)[0].strip()
            email[style] = text
        return email 






