import Writers
import datetime
import FilteredEditorHandler as feh
from Readers import Reader

class Story:
    stories=[]
    def __init__(self, title:str, writer_obj:Writers, file_address:str):
        self.title=title
        self.writer_obj=writer_obj
        self.file_address=file_address
        self.upload_date=datetime.datetime.now()
        self.story_checked=False
        self.points={}
        self.comments={}
        Story.stories.append(self)

    def add_comment(self, reader_obj:Reader, comment=str):
        if reader_obj in self.comments:
            self.comments[reader_obj].append(comment)
        else:
            self.comments[reader_obj]=comment

    @classmethod
    def search_story(cls, title:str) -> object:
        for story in cls.stories:
            if title==story.title:
                return story
        else:
            print(f"{story} not found!")

    def add_point(self, reader_obj:Reader, point:int):            
        if point<=10 and point>=0:
            self.points[reader_obj]=int(point)
        else:
            raise ValueError('Point out of range')
        
    def average_story_point(self) -> int:
        if self.points:
            return int(sum(self.points.values())/len(self.points))
        else:
            return 0

    def check_story(self, replacement:dict) -> None:
        """Check the given story title and replace the invalid words with valid ones.
        Args:
            title: the title of the story.
            replacement: {invalid_word:valid_substitute}
        """
        with feh.EditorHandler(self.title,replacement,'w'):
            pass
        self.story_checked=True
        
    @classmethod
    def stories_list(cls):
        print(f"{'Story List':*^30}")
        for story in cls.stories:
            if story.story_checked:
                print(story)
                print(100*'=')

    def __repr__(self) -> str:
        return f'Title:{self.title}\nUpload date:{self.upload_date}\nCheck status:{self.story_checked}\n{self.writer_obj}'           