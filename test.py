#!/usr/bin/env python3
"""
Test suite for English to Kannada Translator
"""

from translator import Translator
from dictionary import get_word_translation, ENGLISH_TO_KANNADA

def test_word_translation():
    """Test single word translation."""
    translator = Translator()
    
    # Test existing words
    assert translator.translate_word("hello") == "ಹಲೋ"
    assert translator.translate_word("water") == "ನೀರು"
    assert translator.translate_word("good") == "ಚೆನ್ನ"
    
    # Test case insensitivity
    assert translator.translate_word("HELLO") == "ಹಲೋ"
    assert translator.translate_word("Water") == "ನೀರು"
    
    # Test non-existent word
    assert translator.translate_word("xyz123") is None
    
    print("✓ Word translation tests passed")

def test_sentence_translation():
    """Test sentence translation."""
    translator = Translator()
    
    # Test simple sentence
    result = translator.translate_sentence("hello how are you")
    assert "ಹಲೋ" in result
    
    # Test with unknown word
    result = translator.translate_sentence("hello xyz")
    assert "ಹಲೋ" in result
    assert "[xyz]" in result
    
    print("✓ Sentence translation tests passed")

def test_dictionary_operations():
    """Test dictionary operations."""
    translator = Translator()
    
    # Test dictionary size
    initial_size = translator.get_dictionary_size()
    assert initial_size > 100
    
    # Test adding new word
    translator.add_word_to_dictionary("test", "ಪರೀಕ್ಷೆ")
    assert translator.translate_word("test") == "ಪರೀಕ್ಷೆ"
    
    # Test search
    results = translator.search_words("good")
    assert "good" in results
    
    print("✓ Dictionary operation tests passed")

def test_history():
    """Test translation history."""
    translator = Translator()
    
    # Clear history
    translator.clear_history()
    assert len(translator.get_history()) == 0
    
    # Translate something
    translator.translate_word("hello")
    translator.translate_sentence("hello world")
    
    history = translator.get_history()
    assert len(history) >= 1
    
    print("✓ History tests passed")

def test_statistics():
    """Test translation statistics."""
    translator = Translator()
    translator.clear_history()
    
    # Do some translations
    translator.translate_word("hello")
    translator.translate_sentence("hello xyz")
    
    stats = translator.get_translation_stats()
    assert stats['total_translations'] >= 1
    assert stats['total_unknown_words'] >= 1
    
    print("✓ Statistics tests passed")

def test_paragraph_translation():
    """Test paragraph translation."""
    translator = Translator()
    
    paragraph = "Hello world. How are you?"
    result = translator.translate_paragraph(paragraph)
    
    assert "ಹಲೋ" in result
    
    print("✓ Paragraph translation tests passed")

def run_all_tests():
    """Run all tests."""
    print("\n" + "="*50)
    print("Running English-to-Kannada Translator Tests")
    print("="*50 + "\n")
    
    try:
        test_word_translation()
        test_sentence_translation()
        test_dictionary_operations()
        test_history()
        test_statistics()
        test_paragraph_translation()
        
        print("\n" + "="*50)
        print("✓ All tests passed successfully!")
        print("="*50 + "\n")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    run_all_tests()
