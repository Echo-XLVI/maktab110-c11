from Writers import Writer
from Stories import Story
from Readers import Reader


def main():
        reader1=Reader('negar','negar@gmail.com')
        reader2=Reader('reyhane','reyhane@gmail.com')

        writer1=Writer('amir','amir@gmail.com')
        writer2=Writer('mohamad','mamad@gmail.com')    

        story1=writer1.add_story('dogs','Text.txt')
        story2=writer1.add_story('cats','Text.txt')
        story3=writer1.add_story('death','Text.txt')
        story4=writer2.add_story('life','Text.txt')

        story1.check_story({'Lists':'Dict'})
        story2.check_story({'kinds':'ways'})

        Story.stories_list()

        story1.add_point(reader1,7)
        story1.add_point(reader2,10)

        story2.add_point(reader2,5)

        print(writer1.average_writer_point())
        print(writer2.average_writer_point())


if __name__=="__main__":
    main()