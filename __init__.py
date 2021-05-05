from mycroft import MycroftSkill, intent_file_handler


class Testplay(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('testplay.intent')
    def handle_testplay(self, message):
        self.speak_dialog('testplay')


def create_skill():
    return Testplay()

