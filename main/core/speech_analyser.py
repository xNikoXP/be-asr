

def ban_check(transcript: str)->bool:
    """Checks for banned words
    
    Takes the transcript and checks it for words the degrade the quality of
    of a speech

    Args:
        transcript: The written form of the speech
    """
    bannedWords = ["UM", "LIKE", "UH"]
    transcript = transcript.split()
    for word in transcript:
        for banned_word in bannedWords:
            if(word.casefold() == banned_word.casefold()):
                return True
    return False