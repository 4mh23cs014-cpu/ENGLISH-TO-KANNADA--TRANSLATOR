#!/usr/bin/env python3
"""
English to Kannada Translator - Command Line Interface
A simple yet powerful tool to translate English to Kannada
"""

from translator import Translator
import sys

def print_header():
    """Print application header."""
    print("\n" + "="*60)
    print("    ENGLISH TO KANNADA TRANSLATOR")
    print("="*60 + "\n")

def print_menu():
    """Print main menu options."""
    print("\nAvailable Commands:")
    print("  1. Translate a word (word <english_word>)")
    print("  2. Translate a sentence (sentence <english_sentence>)")
    print("  3. Translate a paragraph (paragraph)")
    print("  4. Search dictionary (search <term>)")
    print("  5. Add word to dictionary (add)")
    print("  6. View statistics (stats)")
    print("  7. View translation history (history)")
    print("  8. Dictionary size (size)")
    print("  9. Clear history (clear)")
    print("  0. Exit (exit or quit)")
    print("\n" + "-"*60)

def translate_word(translator, parts):
    """Handle word translation."""
    if len(parts) < 2:
        print("❌ Please provide a word to translate")
        print("   Usage: word <english_word>")
        return
    
    word = ' '.join(parts[1:])
    translation = translator.translate_word(word)
    
    if translation:
        print(f"✓ {word} → {translation}")
    else:
        print(f"✗ '{word}' not found in dictionary")
        print(f"  Dictionary has {translator.get_dictionary_size()} words")

def translate_sentence(translator, parts):
    """Handle sentence translation."""
    if len(parts) < 2:
        print("❌ Please provide a sentence to translate")
        print("   Usage: sentence <english_sentence>")
        return
    
    sentence = ' '.join(parts[1:])
    translation = translator.translate_sentence(sentence)
    print(f"\n English: {sentence}")
    print(f" Kannada: {translation}\n")

def translate_paragraph_interactive(translator):
    """Handle paragraph translation interactively."""
    print("\nEnter paragraph (type 'END' on a new line when done):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    
    paragraph = '\n'.join(lines)
    if paragraph.strip():
        translation = translator.translate_paragraph(paragraph)
        print(f"\nTranslated Paragraph:\n{translation}\n")
    else:
        print("❌ No paragraph provided")

def search_words(translator, parts):
    """Handle word search."""
    if len(parts) < 2:
        print("❌ Please provide a search term")
        print("   Usage: search <term>")
        return
    
    term = ' '.join(parts[1:])
    results = translator.search_words(term)
    
    if results:
        print(f"\n✓ Found {len(results)} match(es):")
        for english, kannada in sorted(results.items()):
            print(f"  {english:30} → {kannada}")
        print()
    else:
        print(f"✗ No words found containing '{term}'")

def add_word(translator):
    """Handle adding a new word to dictionary."""
    english = input("Enter English word: ").strip()
    kannada = input("Enter Kannada translation: ").strip()
    
    if english and kannada:
        message = translator.add_word_to_dictionary(english, kannada)
        print(f"✓ {message}")
    else:
        print("❌ Both fields are required")

def show_statistics(translator):
    """Show translation statistics."""
    stats = translator.get_translation_stats()
    print(f"\n{'Statistics':^40}")
    print("-" * 40)
    print(f"Total Translations: {stats['total_translations']}")
    print(f"Unknown Words Encountered: {stats['total_unknown_words']}")
    print(f"Dictionary Size: {translator.get_dictionary_size()} words")
    if stats['total_translations'] > 0:
        print(f"Success Rate: {stats['success_rate']:.1f}%")
    print()

def show_history(translator):
    """Show translation history."""
    history = translator.get_history()
    
    if not history:
        print("\n❌ No translation history available")
        return
    
    print(f"\n{'Translation History':^60}")
    print("="*60)
    
    for i, item in enumerate(history, 1):
        print(f"\n{i}. English: {item['english']}")
        print(f"   Kannada: {item['kannada']}")
        if item['unknown_words']:
            print(f"   Unknown: {', '.join(item['unknown_words'])}")

def show_dictionary_size(translator):
    """Show dictionary size."""
    size = translator.get_dictionary_size()
    print(f"\n✓ Dictionary contains {size} words\n")

def clear_history(translator):
    """Clear translation history."""
    translator.clear_history()
    print("\n✓ Translation history cleared\n")

def main():
    """Main application loop."""
    translator = Translator()
    print_header()
    print(f"Dictionary loaded with {translator.get_dictionary_size()} words")
    print("\nType 'help' or '?' for menu, or 'exit' to quit")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if not user_input:
                continue
            
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            
            if command in ['exit', 'quit', 'q']:
                print("\n👋 Thank you for using English-to-Kannada Translator!")
                print("ಧನ್ಯವಾದ!\n")
                break
            
            elif command in ['help', '?']:
                print_menu()
            
            elif command == 'word':
                translate_word(translator, parts)
            
            elif command == 'sentence':
                translate_sentence(translator, parts)
            
            elif command == 'paragraph':
                translate_paragraph_interactive(translator)
            
            elif command == 'search':
                search_words(translator, parts)
            
            elif command == 'add':
                add_word(translator)
            
            elif command == 'stats':
                show_statistics(translator)
            
            elif command == 'history':
                show_history(translator)
            
            elif command == 'size':
                show_dictionary_size(translator)
            
            elif command == 'clear':
                clear_history(translator)
            
            else:
                print(f"❌ Unknown command: '{command}'")
                print("Type 'help' or '?' for available commands")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
