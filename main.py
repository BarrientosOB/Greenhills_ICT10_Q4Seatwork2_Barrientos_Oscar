from pyscript import display, document


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    
    def introduce(self):
        return f'Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}.'


classmate_list = [
    Classmate('Juanico', 'Emerald', 'Math'),
    Classmate('Gurnoor', 'Emerald', 'Science'),
    Classmate('Thomas', 'Ruby', 'English'),
    Classmate('Angela', 'Emerald', 'Math'),
    Classmate('Gino', 'Sapphire', 'Social Studies')
]


def add_classmate(event):
    name_input = document.querySelector('#name').value
    section_input = document.querySelector('#section').value
    subject_input = document.querySelector('#subject').value

    if name_input and section_input and subject_input:
        new_person = Classmate(name_input, section_input, subject_input)
        classmate_list.append(new_person)
        
     
        document.querySelector('#name').value = ""
        document.querySelector('#section').value = ""
        document.querySelector('#subject').value = ""



def show_list(event):
    display_area = document.querySelector('#display-area')
    display_area.innerHTML = ""
    
    for person in classmate_list:
        p_tag = document.createElement("p")
        p_tag.innerText = person.introduce()
        display_area.appendChild(p_tag)