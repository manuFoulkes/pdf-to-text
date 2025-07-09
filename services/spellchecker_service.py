import re
from spellchecker import SpellChecker

class SpellCheckerService():
    def __init__(self, language='es'):
        self.spell = SpellChecker(language=language)
    
    def correct_text(self, raw_text):
        tokens = re.findall(r'\w+|[^\w\s]|\s+', raw_text)
        corrected_tokens = []
        
        for token in tokens:
            if not token.strip().isalpha():
                corrected_tokens.append(token)
                continue
            
            original_word = token
            lower_word = token.lower()
            
            if lower_word in self.spell:
                corrected_tokens.append(original_word)
                continue
            
            corrected_word = self.spell.correction(lower_word)
            
            if original_word[0].isupper() and corrected_word:
                corrected_word = corrected_word.capitalize()
                
            corrected_tokens.append(corrected_word if corrected_word else original_word)
            
        return ''.join(corrected_tokens)
        