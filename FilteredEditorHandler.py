import os
import Validators

class EditorHandler:
    final_dir="final_stories"
    temp_dir="temp_stories"
    temp_current_dir=os.getcwd()
    current_dir=os.getcwd()
        
    def __init__(self, title:str, replacement:dict, mode:str) -> None:
        self.title=title
        self.replacement=replacement
        self.data=None
        self.mode=mode

    def __enter__(self):
        if not os.path.exists(os.path.join(self.current_dir,self.final_dir)):
            os.mkdir(os.path.join(self.current_dir,self.final_dir))
        self.file=open(os.path.join(self.current_dir,self.final_dir,f'final_story_{self.title}.txt'),self.mode)
        if self.mode == 'w':
            with open(os.path.join(self.temp_current_dir,self.temp_dir,f"temp_story_{self.title}.txt"),'r') as temp_file:
                self.data="".join(temp_file.readlines())
                self.data=Validators.Validation.text_validation(self.data,self.replacement)
                for line in self.data.split('\n'):
                    self.file.write(f"{line}\n")
        
    def __exit__(self,exc_type, exc_value, exc_tb):
        os.remove(os.path.join(self.temp_current_dir,self.temp_dir,f'temp_story_{self.title}.txt'))
        self.file.close()       
