from Modules import os

class MyContextManager:
    temp_dir="temp_stories"
    current_dir=os.getcwd()

    def __init__(self,file_address:str, mode:str, title:str) -> None:
        self.title=title
        self.file_address=file_address
        self.data=None
        self.mode=mode

    def __enter__(self):
        self.file=open(self.file_address,self.mode)
        if self.mode == 'r':
            self.data=self.file.readlines()
        
    def __exit__(self,exc_type, exc_value, exc_tb):
        if not os.path.exists(os.path.join(self.current_dir,self.temp_dir)):
            os.mkdir(os.path.join(self.current_dir,self.temp_dir))
        with open(os.path.join(self.current_dir,self.temp_dir,f'temp_story_{self.title}.txt'),'w') as temp_file:
            temp_file.writelines(self.data)
        self.file.close()      