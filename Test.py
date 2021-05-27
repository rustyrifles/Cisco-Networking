""" Some initial comments here at the top
of the screen. This just shows how we can
comment multiline"""

from tkintertoy import Window
bob = ''
bob2 = ''
bob3 = ''
categories = ['Car', 'Bike', 'Bus']
gui = Window()
gui.setTitle('My First Tkintertoy GUI!')
gui.addEntry('name', 'Type in your name')
gui.addLabel('welcome', 'Welcome message *** TEST ***')
gui.addEntry('Age', 'Type in your age')
gui.addLabel('old', 'You are of age')
gui.addButton('commands')
gui.addRadio('')
gui.addRadio('category', 'Item Types' , categories)
gui.plot('name', row=0)
gui.plot('Age', row=1)
gui.plot('welcome', row=2)
gui.plot('old', row=3)
gui.plot('category', row=4)
gui.plot('commands', row=5, pady=10)
while True:
    gui.waitforUser()
    if gui.content:
        gui.set('welcome', 'Welcome ' + gui.get('name'))
        bob = gui.get('name')
        gui.set('old', gui.get('Age'))
        bob2 = gui.get('Age')
        bob3 = gui.get('category')
        if bob3 == 'Bus':
            break
    else:
        break
print(bob, bob2, bob3)
