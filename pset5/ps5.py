# 6.0001/6.00 Problem Set 5 - RSS Feed Filter

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
	"""
	Fetches news items from the rss url and parses them.
	Returns a list of NewsStory-s.
	"""
	feed = feedparser.parse(url)
	entries = feed.entries
	ret = []
	for entry in entries:
		guid = entry.guid
		title = translate_html(entry.title)
		link = entry.link
		description = translate_html(entry.description)
		pubdate = translate_html(entry.published)

		try:
			pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
			pubdate.replace(tzinfo=pytz.timezone("GMT"))
			#  pubdate = pubdate.astimezone(pytz.timezone('EST'))
			#  pubdate.replace(tzinfo=None)
		except ValueError:
			pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

		newsStory = NewsStory(guid, title, description, link, pubdate)
		ret.append(newsStory)
	return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
	"""
	Holds information about a news story from RSS feed

	Params:
	- guid
	- title
	- description
	- link
	- pubdate (publication datetime)
	"""
	def __init__(self, guid, title, description, link, pubdate):
		self.guid = guid
		self.title = title
		self.description = description
		self.link = link
		self.pubdate = pubdate
	def get_guid(self):
		return self.guid
	def get_title(self):
		return self.title
	def get_description(self):
		return self.description
	def get_link(self):
		return self.link
	def get_pubdate(self):
		return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
	def evaluate(self, story):
		"""
		Returns True if an alert should be generated
		for the given news item, or False otherwise.
		"""
		# DO NOT CHANGE THIS!
		raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
	def __init__(self,phrase):
		"""
		params:
		- phrase: string to set as property of class instance
		"""
		match = phrase.lower().strip()
		match_check = match.split(' ') # if spaces are next to each other, this leaves one intact
		for word in match_check:
			for char in string.punctuation+' ':
				if char in word:
					raise ValueError("Can't use more than 1 space between words or punctuation")
		self.phrase = match_check
	def get_match(self):
		return self.phrase.copy()
	def is_phrase_in(self,story_string):
		"""
		Returns True if an alert should be generated
		for the given news item, or False otherwise.

		Params:
			- story_string: thing to compare against match
		"""
		story_string = story_string.lower()
		match_check = self.get_match()
		for punc in string.punctuation:
			# we don't care what is between the words so long as it's not
			# an alphabet char so just make them all spaces
			story_string = story_string.replace(punc, ' ')
		# All spaces would be gotten rid of and only the word in between spaces left
		story_array = story_string.split()
		if len(story_array) == len(match_check) and story_array == match_check:
			return True
		else:
			j = len(match_check)
			for i in range(0,len(story_array)-j+1):
				if match_check == story_array[i:j]:
					return True
				j += 1
			return False



# Problem 3
class TitleTrigger(PhraseTrigger):
	def evaluate(self,story):
		"""
		Returns true if the title matches the phrase this instance
		of TitleTrigger was created with

		Params:
		- story: an instance of NewsStory
		"""
		return self.is_phrase_in(story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
	def evaluate(self,story):
		"""
		Returns true if the description matches the phrase this instance
		of DescriptionTrigger was created with

		Params:
		- story: an instance of NewsStory
		"""
		return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
	def __init__(self,time):
		"""
		Takes time string and converts to datetime before saving
		as part of the object

		param:
		- time: string in format '3 Oct 2016 17:00:10'
		"""
		try:
			date = datetime.strptime(time, "%d %b %Y %H:%M:%S")
			date = date.replace(tzinfo=pytz.timezone("EST"))
		except ValueError:
			date = datetime.strptime(time, "%d %b %Y %H:%M:%S")
		self.date = date
	def get_time(self):
		return self.date


# Problem 6
class BeforeTrigger(TimeTrigger):
	def evaluate(self,story):
		"""
		Takes a story and checks if it was published before the date that
		this class was instantiated with

		params:
		- story: NewsStory instance
			- pubdate: date in %d %b %Y %H:%M:%S format
		"""
		if self.get_time() > story.get_pubdate().replace(tzinfo=pytz.timezone("EST")):
			return True
		return False

class AfterTrigger(TimeTrigger):
	def evaluate(self,story):
		"""
		Takes a story and checks if it was published after the date that
		this class was instantiated with

		params:
		- story: NewsStory instance
			- pubdate: date in %d %b %Y %H:%M:%S format
		"""
		if self.get_time() < story.get_pubdate().replace(tzinfo=pytz.timezone("EST")):
			return True
		return False


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
	def __init__(self,other_trigger):
		"""
		Takes a trigger and triggers itself only if the other doesn't
		go off

		params:
		- other_trigger: Instance of a trigger
		"""
		self.other = other_trigger
	def get_trigger(self):
		return self.other
	def evaluate(self, story):
		return not self.get_trigger().evaluate(story)


# Problem 8
class AndTrigger(Trigger):
	def __init__(self,trig1,trig2):
		"""
		Takes two instantiated triggers and only triggers if both of them trigger
		"""
		self.trig1 = trig1
		self.trig2 = trig2
	def get_triggers(self):
		return [self.trig1,self.trig2]
	def evaluate(self,story):
		"""
		Given a story, checks if that story triggers both triggers
		that this instance of AndTrigger was instantiated with
		"""
		triggers = self.get_triggers()
		if triggers[0].evaluate(story) and triggers[1].evaluate(story):
			return True
		return False

# Problem 9
class OrTrigger(Trigger):
	def __init__(self,trig1,trig2):
		"""
		Takes two instantiated triggers and only triggers if either of them trigger
		"""
		self.trig1 = trig1
		self.trig2 = trig2
	def get_triggers(self):
		return [self.trig1,self.trig2]
	def evaluate(self,story):
		"""
		Given a story, checks if that story triggers either of the triggers
		that this instance of OrTrigger was instantiated with
		"""
		triggers = self.get_triggers()
		if triggers[0].evaluate(story) or triggers[1].evaluate(story):
			return True
		return False


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
	"""
	Takes in a list of NewsStory instances.

	Returns: a list of only the stories for which a trigger in triggerlist fires.

	Params:
	- stories(List)
	- Triggers(List)
	"""
	verified = []
	for story in stories:
		for trigger in triggerlist:
			if trigger.evaluate(story):
				verified.append(story)
				break
	return verified



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
	"""
	filename: the name of a trigger configuration file

	Returns: a list of trigger objects specified by the trigger configuration
		file.
	"""
	trigger_file = open(filename, 'r')
	lines = []
	for line in trigger_file:
		line = line.rstrip() #gets rid of trailing space
		if not (len(line) == 0 or line.startswith('//')):
			lines.append(line)

	trigger_dict = {}
	returns = []
	for line in lines:
		if line.startswith('ADD'):
			adds = line.split(',')[1:]
			returns.extend([trigger_dict.get(item) for item in adds])
		else:
			content = line.split(',')
			if content[1]=='TITLE':
				trigger_dict[content[0]] = TitleTrigger(content[2])
			elif content[1]=='DESCRIPTION':
				trigger_dict[content[0]] = DescriptionTrigger(content[2])
			elif content[1]=='AFTER':
				trigger_dict[content[0]] = AfterTrigger(content[2])
			elif content[1]=='BEFORE':
				trigger_dict[content[0]] = BeforeTrigger(content[2])
			elif content[1]=='NOT':
				trigger_dict[content[0]] = NotTrigger(content[2])
			elif content[1]=='AND':
				trigger_dict[content[0]] = AndTrigger(trigger_dict.get(content[2]),trigger_dict.get(content[3]))
			else:
				trigger_dict[content[0]] = OrTrigger(trigger_dict.get(content[2]),trigger_dict.get(content[3]))
	return returns






SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
	# A sample trigger list - you might need to change the phrases to correspond
	# to what is currently in the news
	try:
		t1 = TitleTrigger("election")
		t2 = DescriptionTrigger("Trump")
		t3 = DescriptionTrigger("Biden")
		t4 = AndTrigger(t2, t3)
		triggerlist = [t1, t4]

		# Problem 11

		triggerlist = read_trigger_config('triggers.txt')
		print(triggerlist)

		# HELPER CODE - you don't need to understand this!
		# Draws the popup window that displays the filtered stories
		# Retrieves and filters the stories from the RSS feeds
		frame = Frame(master)
		frame.pack(side=BOTTOM)
		scrollbar = Scrollbar(master)
		scrollbar.pack(side=RIGHT,fill=Y)

		t = "Google & Yahoo Top News"
		title = StringVar()
		title.set(t)
		ttl = Label(master, textvariable=title, font=("Helvetica", 18))
		ttl.pack(side=TOP)
		cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
		cont.pack(side=BOTTOM)
		cont.tag_config("title", justify='center')
		button = Button(frame, text="Exit", command=root.destroy)
		button.pack(side=BOTTOM)
		guidShown = []
		def get_cont(newstory):
			if newstory.get_guid() not in guidShown:
				cont.insert(END, newstory.get_title()+"\n", "title")
				cont.insert(END, "\n---------------------------------------------------------------\n", "title")
				cont.insert(END, newstory.get_description())
				cont.insert(END, "\n*********************************************************************\n", "title")
				guidShown.append(newstory.get_guid())

		while True:

			print("Polling . . .", end=' ')
			# Get stories from Google's Top Stories RSS news feed
			stories = process("http://news.google.com/news?output=rss")

			# Get stories from Yahoo's Top Stories RSS news feed
			stories.extend(process("https://www.yahoo.com/news/rss"))

			stories = filter_stories(stories, triggerlist)

			list(map(get_cont, stories))
			scrollbar.config(command=cont.yview)


			print("Sleeping...")
			time.sleep(SLEEPTIME)

	except Exception as e:
		print(e)


if __name__ == '__main__':
	root = Tk()
	root.title("Some RSS parser")
	t = threading.Thread(target=main_thread, args=(root,))
	t.start()
	root.mainloop()

