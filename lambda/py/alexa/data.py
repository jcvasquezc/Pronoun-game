# -*- coding: utf-8 -*-

STATES_LIST = [
    {
        'name': 'Gorillas',
        'species': 'Gorilla', 
        'size': 3,
        'fact':'walks with its long arms',
        'color':'black and have fur',
        'diet':'plants and fruits',
        'habitat': 'the forest', 
        'number':'220000',
        'endangered':'of habitat encroachment and poaching for bushmeat and trophies',
        'descrip':'Gorillas have hands and feet like humans including opposable thumbs and big toes and live in small groups called troops. They are endangered because people are hunting them. ',
        'sound':"""<audio src="soundbank://soundlibrary/animals/gorilla/gorilla_07"/>"""
    },
    {
        'name':'Elephants',
        'species': 'Elephant',
        'size': 4,
        'fact':'use the trunk for breathing, touching, and producing sound',
        'color':'grey and hairless',
        'diet':'plants',
        'habitat': 'savannahs, forests and deserts', 
        'number':'40000',
        'endangered':'is poached for its ivory, meat, and skin.',
        'descrip':'Elephants are the largest land animals on earth, they will throw sand and dirt on their backs to keep from getting sunburned and they don\'t really like peanuts. We have to protect the elephants because people is hunting them for their ivory. ',
        'sound':"""<audio src="soundbank://soundlibrary/animals/amzn_sfx_elephant_01"/>"""
    },
    {
        'name':'Tigers',
        'species': 'Tiger',
        'size': 2,
        'fact':'is the biggest species of the cat family',
        'color':'is orange with dark vertical stripes',
        'diet':'meat',
        'habitat': 'forests', 
        'number':'3000',
        'endangered':'habitat destruction and poaching',
        'descrip':'Tigers are the biggest species of the cat family, they are good swimmers, and they can jump over five meters in length. The are endangered because people is hunting them and destroying their habitat. ',
        'sound':"""<audio src="soundbank://soundlibrary/animals/amzn_sfx_lion_roar_03"/>"""
    }]


SIMILAR={
    'gorilla':['golilla', 'korilla', 'golillas', 'galillas', 'kolilla', 'guerilla'],
    'elephant':['elephanti','elefante','efelant','epelant','edephant','edepant'],
    'tiger':['tigre','tiga','tige','tigla']
}


SKILL_TITLE = "Pronoun game"

WELCOME_MESSAGE = ("Welcome to the Pronoun Game!  "
                  "Ask me to "
                 "start a quiz. ")


START_QUIZ_MESSAGE = ("")

EXIT_SKILL_MESSAGE = ("That was <say-as interpret-as='interjection'>fun</say-as><break strength='strong'/> " 
                        "Let me know if you want to play again.")

REPROMPT_SPEECH = "Which other animal would you like to know about?"

HELP_MESSAGE = ("If you want me to play with you, you can ask to start a quiz,  "
                "or you can ask me to stop. "
                "What would you like to do? ")

CORRECT_SPEECHCONS = ['Booya', 'All righty', 'Bam', 'Bazinga', 'Bingo',
                      'Boom', 'Bravo', 'Cha Ching', 'Cheers', 'Dynomite',
                      'Hip hip hooray', 'Hurrah', 'Hurray', 'Huzzah',
                      'Oh dear.  Just kidding.  Hurray', 'Kaboom', 'Kaching',
                      'Oh snap', 'Phew', 'Righto', 'Way to go', 'Well done',
                      'Whee', 'Woo hoo', 'Yay', 'Wowza', 'Yowsa']

NICE_TRY = ("Nice try, here is another hint. ")

WRONG_SPEECHCONS = ['Aw man']

IMG_PATH = (  "https://m.media-amazon.com/images/G/01/mobile-apps/dex/alexa/"
  "alexa-skills-kit/tutorials/quiz-game/state_flag/{}x{}/{}._TTH_.png")

USE_CARDS_FLAG = True

MAX_QUESTIONS = 5

BAD_ANSWER = (
    "I'm sorry. {} is not something I know very much about in this skill.")

NO_ANSWER = ('The animal i was thinking of is the')

FALLBACK_ANSWER = (
    "Sorry. I can't help you with that. {}".format(HELP_MESSAGE))

SCORE = "Your {} score is {}. "

SPEECH_DESC = ("{}")

SPEECH_PROUN= ("But actually most people pronounce it like <emphasis level='strong'>{}</emphasis>.  ")
