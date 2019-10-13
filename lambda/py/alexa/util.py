# -*- coding: utf-8 -*-

"""Utility module to generate text for commonly used responses."""

import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type

from . import data


def no_answer(item):
    text = data.NO_ANSWER+ ' '+item+'. '
    return text

def get_hint(handler_input,lists,item):
    val = state_properties()
    for k in lists:
        val.remove(k)
    #random_state = get_random_state(data.STATES_LIST)
    random_property = random.choice(val)

    attr = handler_input.attributes_manager.session_attributes

    attr["quiz_item"] = item
    attr["quiz_attr"] = random_property
    attr["counter"] += 1

    handler_input.attributes_manager.session_attributes = attr
    
    return data.NICE_TRY+get_question(attr["counter"], random_property, item)


#def pronoun_variations():
    

def get_random_state(states_list):
    """Return a random value from the list of states."""
    return random.choice(states_list)


def state_properties():
    """Return the list of state properties."""
    val = [ "color", "diet","habitat", "fact", "endangered", "sound"]
    return val


def get_random_state_property():
    """Return a random state property."""
    return random.choice(state_properties())


def get_card_description(item):
    """Return the description shown on card in Alexa response."""
    text = "State Name: {}\n".format(item['name'])
    return text


def supports_display(handler_input):
    # type: (HandlerInput) -> bool
    """Check if display is supported by the skill."""
    try:
        if hasattr(
                handler_input.request_envelope.context.system.device.
                        supported_interfaces, 'display'):
            return (
                    handler_input.request_envelope.context.system.device.
                    supported_interfaces.display is not None)
    except:
        return False


def get_bad_answer(item):
    """Return response text for incorrect answer."""
    return "{} {}".format(data.BAD_ANSWER.format(item), data.HELP_MESSAGE)


def get_current_score(score, counter):
    """Return the response text for current quiz score of the user."""
    return data.SCORE.format("current", score)


def get_final_score(score, counter):
    """Return the response text for final quiz score of the user."""
    return data.SCORE.format("final", score)


def get_card_title(item):
    """Return state name as card title."""
    return item["state"]


def get_image(ht, wd, label):
    """Get flag image with specified height, width and state abbr as label."""
    return data.IMG_PATH.format(str(ht), str(wd), label)


def get_small_image(item):
    """Get state flag small image (720x400)."""
    return get_image(720, 400, item['abbreviation'])


def get_large_image(item):
    """Get state flag large image (1200x800)."""
    return get_image(1200, 800, item['abbreviation'])


def get_speech_description(item):
    """Return state information in well formatted text."""
    return data.SPEECH_DESC.format(item['descrip'])


def get_ordinal_indicator(counter):
    """Return st, nd, rd, th ordinal indicators according to counter."""
    if counter == 1:
        return "1st"
    elif counter == 2:
        return "2nd"
    elif counter == 3:
        return "3rd"
    else:
        return "{}th".format(str(counter))


def __get_attr_for_speech(attr):
    """Helper function to convert attribute name."""
    return attr.lower().replace("_", " ").strip()


def get_question_without_ordinal(attr, item):
    key=__get_attr_for_speech(attr)
    
    if key=='fact':
        return "The animal i am thinking about {}.".format(item[key])
    elif key=='endangered':
        return "The animal i am thinking about is endangered because {}.".format(item[key])
    elif key=='diet':
        return "The animal i am thinking about like to eat {}".format(item[key])
    elif key=='habitat':
        return "The animal i am thinking about mostly lives in {}.".format(item[key])
    elif key=='color':
        return "The animal i am thinking about is {}".format(item[key])
    elif key=='sound':
        return "The animal i am thinking about makes this sound: {}".format(item[key])
    else:
        return "The {} of the animal I am thinking of is {}. ".format(
            key, item[key])


def get_question(counter, attr, item):
    """Return response text for nth question to the user."""
    return ("{}").format(get_question_without_ordinal(attr, item))


def get_answer(attr, item):
    """Return response text for correct answer to the user."""
    #if attr.lower() == "skin":
    #   return ("The {} of {} is "
    #            "<say-as interpret-as='spell-out'>{}</say-as>. ").format(
    #       __get_attr_for_speech(attr), item["name"], item["name"])
    #else:
    return "The animal i was thinking of was {} . ".format(
            item['species'])


def ask_question(handler_input):
    # (HandlerInput) -> None
    """Get a random state and property, return question about it."""
    random_state = get_random_state(data.STATES_LIST)
    random_property = get_random_state_property()

    attr = handler_input.attributes_manager.session_attributes

    attr["quiz_item"] = random_state
    attr["quiz_attr"] = random_property

    handler_input.attributes_manager.session_attributes = attr

    return get_question(attr["counter"], random_property, random_state)


def get_speechcon(correct_answer):
    """Return speechcon corresponding to the boolean answer correctness."""
    text = ("<say-as interpret-as='interjection'>{} !"
            "</say-as><break strength='strong'/>")
    if correct_answer:
        return text.format(random.choice(data.CORRECT_SPEECHCONS))
    else:
        return text.format(random.choice(data.WRONG_SPEECHCONS))


def get_multiple_choice_answers(item, attr, states_list):
    """Return multiple choices for the display to show."""
    answers_list = [item[attr]]
    # Insert the correct answer first

    while len(answers_list) < 3:
        state = random.choice(states_list)

        if not state[attr] in answers_list:
            answers_list.append(state[attr])

    random.shuffle(answers_list)
    return answers_list


def get_item(slots, states_list):
    """Get matching data object from slot value."""
    item = []
    resolved_slot = None
    for _, slot in six.iteritems(slots):
        if slot.value is not None:
            resolved_slot = slot.value
            for state in states_list:
                for _, v in six.iteritems(state):
                    if v.lower() == slot.value.lower():
                        item.append(state)
            if len(item) > 0:
                return item[0], True
    else:
        return resolved_slot, False


def compare_token_or_slots(handler_input, value):
    """Compare value with slots or token,
        for display selected event or voice response for quiz answer."""
    if is_request_type("Display.ElementSelected")(handler_input):
        return handler_input.request_envelope.request.token == value
    else:
        
        correct, flag= compare_slots(
            handler_input.request_envelope.request.intent.slots, value)
        return correct, flag


def compare_slots(slots, value):
    """Compare slot value to the value provided."""
    for _, slot in six.iteritems(slots):
        if slot.value is not None:
            if slot.value.lower() == value.lower():
                return True, 'perfect'

        for k in data.SIMILAR[value.lower()]:
            if slot.value is not None:
                if slot.value.lower() == k:
                    return True, 'miss'
                else:
                    continue
    return False, 'wrong'

