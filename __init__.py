import os
from mycroft import MycroftSkill, intent_file_handler

def is_playing():
	playing = False
	check = os.popen('ps ax | grep cmus | grep -v "grep"').readlines()
	if len(check) > 0:
		playing = True
	return playing

class TestPlay(MycroftSkill):

	def __init__(self):
		MycroftSkill.__init__(self)
		self.open_player()


	@intent_file_handler('start.intent')
	def handlle_start_intent(self, message):
		self.start_player()
		self.speak_dialog("start")

	@intent_file_handler('pause.intent')
	def handle_pause_intent(self, message):
		self.pause_player()

	@intent_file_handler('continue.intent')
	def handlle_continue_intent(self, message):
		self.toggle_pause()

	@intent_file_handler('stop.intent')
	def handle_stop_intent(self, message):
		self.stop_player()

	@intent_file_handler('next.intent')
	def handle_next_intent(self, message):
		self.play_next()

	@intent_file_handler('update.intent')
	def handlle_update_intent(self, message):
		self.update_library()

	def open_player(self):
		if not is_playing():
			self.start_player()

	def start_player(self):
		os.system("screen -d -m -S cmus cmus &")
		os.system('cmus-remote -C "view 2"')
		os.system('cmus-remote -p')

	def update_library(self):
		os.system('cmus-remote -C clear')
		os.system('cmus-remote -C "add ~/music"')
		self.speak_dialog("update")

	def pause_player(self):
		self.speak_dialog("pause")
		os.system('cmus-remote -U')

	def toggle_pause(self):
		self.speak_dialog("continue")
		os.system('cmus-remote -u')

	def stop_player(self):
		self.speak_dialog("stop")
		os.system('cmus-remote -s')

	def play_next(self):
		self.speak_dialog("next")
		os.system('cmus-remote -n')

def create_skill():
	return TestPlay()
