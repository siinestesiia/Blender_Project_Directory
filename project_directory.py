import os
import winsound


class ProjectCreator:
    def __init__(self):
        self.message()
        self.DIRECTORY = 'D:/BLENDER/PROJECTS/RANDOM STUFF/'
        self.folders = ['Blend Files', 'References', 'Progress', 'Renders']

    def message(self):
        print('\n-- welcome to the Blender project creator --\n'.upper())

    def folders_creator(self):
        project_name = input('Select the project name: ').title()
        
        ''' Checks if the folder already exists. '''
        while os.path.isdir(f'{self.DIRECTORY}{project_name}'):
            winsound.Beep(180, 200) # Plays an error kind of sound.
            rename = 'That project name already exists.\n'
            rename += 'Please enter a non-existing project name: '
            project_name = input(rename).title()
        
        ''' Creates the new directory '''
        NEW_DIRECTORY = f'{self.DIRECTORY}/{project_name}'
        os.mkdir(NEW_DIRECTORY)
        for folder in self.folders:
            os.mkdir(f'{NEW_DIRECTORY}/{folder}')
            if folder == self.folders[1]:
                open(f'{NEW_DIRECTORY}/{folder}/Image References.pur', 'x')

        os.startfile(f'{self.DIRECTORY}{project_name}/')

    ''' Creates a new project directory or exits the program. '''
    def project_manager(self):
        options_mssg = 'Press the designated keys to proceed.\n'
        options_mssg += '\nCreate a new project: B.\nTo exit: Q.'
        print(options_mssg)

        user_input = input('Select an option: ').upper()

        while user_input != 'B' and user_input != 'Q':
            winsound.Beep(180, 200) # Plays an error kind of sound.
            print('\nYou have to press either B or Q.')
            user_input = input('Select a valid option: ').upper()
            
        if user_input == 'B':
            self.folders_creator()
            winsound.Beep(2000, 200)
            print('\nProject directory created successfully!')
        elif user_input == 'Q':
            print('\nThanks for using the Blender project creator!')
        

project = ProjectCreator()
project.project_manager()