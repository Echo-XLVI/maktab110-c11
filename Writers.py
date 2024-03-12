from Stories import Story
import Validators
import UploaderContextManager as ucm

class Writer:
    def __init__(self, name:str, email:str) -> None:
        if Validators.Validation.email_validation(email):
            self.name=name         
            self.email=email
            self.stories={}
        else:
            raise ValueError("Entered email address is in the wrong format.")
    
    def add_story(self, title:str, file_address:str) -> Story:
        if Validators.Validation.check_directory(file_address):
            with ucm.MyContextManager(file_address,'r',title):
                pass
            story=Story(title,self,file_address)
            self.stories[title]=story
            return story
        
    def average_writer_point(self):
        total=0        
        for story in self.stories.values():
            total+=story.average_story_point() 
        return int(total/len(self.stories))    

    def __repr__(self) -> str:
        return f"Name:{self.name}\nEmail:{self.email}"