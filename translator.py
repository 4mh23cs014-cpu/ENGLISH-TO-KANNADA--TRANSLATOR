import re
from dictionary import ENGLISH_TO_KANNADA

class Translator:
    """English to Kannada Translator"""
    
    def __init__(self):
        self.dictionary = ENGLISH_TO_KANNADA
        self.translation_history = []
    
    def translate_word(self, word):
        """Translate a single word from English to Kannada."""
        word_lower = word.lower().strip()
        translation = self.dictionary.get(word_lower)
        return translation
    
    def translate_sentence(self, sentence):
        """Translate a sentence from English to Kannada word by word."""
        if not sentence.strip():
            return ""
        
        # Split sentence into words
        words = re.findall(r'\b\w+(?:\'s)?\b', sentence.lower())
        
        translated_words = []
        unknown_words = []
        
        for word in words:
            word_clean = word.rstrip("'s").lower()
            translation = self.dictionary.get(word_clean)
            
            if translation:
                translated_words.append(translation)
            else:
                translated_words.append(f"[{word}]")  # Mark unknown words
                unknown_words.append(word)
        
        result = " ".join(translated_words)
        
        # Store in history
        self.translation_history.append({
            'english': sentence,
            'kannada': result,
            'unknown_words': unknown_words
        })
        
        return result
    
    def translate_paragraph(self, paragraph):
        """Translate a paragraph (multiple sentences)."""
        sentences = re.split(r'[.!?]+', paragraph)
        translations = []
        
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                translation = self.translate_sentence(sentence)
                translations.append(translation)
        
        return '\n'.join(translations)
    
    def get_translation_stats(self):
        """Get statistics about translations."""
        total = len(self.translation_history)
        total_unknown = sum(len(item['unknown_words']) for item in self.translation_history)
        return {
            'total_translations': total,
            'total_unknown_words': total_unknown,
            'success_rate': ((total - (total_unknown > 0)) / total * 100) if total > 0 else 0
        }
    
    def clear_history(self):
        """Clear translation history."""
        self.translation_history = []
    
    def get_history(self):
        """Get translation history."""
        return self.translation_history
    
    def add_word_to_dictionary(self, english_word, kannada_word):
        """Add a new word to the dictionary."""
        word_key = english_word.lower().strip()
        self.dictionary[word_key] = kannada_word
        return f"Added: {english_word} -> {kannada_word}"
    
    def get_dictionary_size(self):
        """Get the number of words in the dictionary."""
        return len(self.dictionary)
    
    def search_words(self, search_term):
        """Search for words containing the search term."""
        search_lower = search_term.lower()
        results = {k: v for k, v in self.dictionary.items() if search_lower in k}
        return results
