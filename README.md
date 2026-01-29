# English to Kannada Translator 🇮🇳

A simple yet powerful Python application to translate English words, sentences, and paragraphs into Kannada (ಕನ್ನಡ).

## Features

- **Word Translation**: Translate individual English words to Kannada
- **Sentence Translation**: Translate complete sentences with word-by-word translation
- **Paragraph Translation**: Translate multiple sentences at once
- **Dictionary Management**: 
  - Built-in dictionary with 200+ words
  - Add new words to the dictionary
  - Search for words in the dictionary
- **Translation History**: Keep track of all translations performed
- **Statistics**: View translation statistics and success metrics
- **Case Insensitive**: Works with any capitalization
- **Unknown Word Handling**: Marks unknown words in translations

## Installation

### Prerequisites
- Python 3.6 or higher

### Steps

1. Clone or download the project:
```bash
cd ENGLISH-TO-KANNADA--TRANSLATOR
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

### Interactive Commands

Once the application is running, use these commands:

#### Translation Commands
- `word <english_word>` - Translate a single word
  ```
  > word hello
  ✓ hello → ಹಲೋ
  ```

- `sentence <english_sentence>` - Translate a sentence
  ```
  > sentence hello how are you
  English: hello how are you
  Kannada: ಹಲೋ ಹೇಗಿದ್ದೀರಿ
  ```

- `paragraph` - Translate multiple sentences
  ```
  > paragraph
  Enter paragraph (type 'END' on a new line when done):
  Hello world. How are you today?
  END
  ```

#### Dictionary Commands
- `search <term>` - Search for words containing the term
  ```
  > search good
  ✓ Found 1 match(es):
    good                           → ಚೆನ್ನ
  ```

- `add` - Add a new word to the dictionary
  ```
  > add
  Enter English word: test
  Enter Kannada translation: ಪರೀಕ್ಷೆ
  ✓ Added: test → ಪರೀಕ್ಷೆ
  ```

- `size` - Show dictionary size
  ```
  > size
  ✓ Dictionary contains 200 words
  ```

#### Utility Commands
- `stats` - Show translation statistics
  ```
  > stats
          Statistics
  ========================================
  Total Translations: 5
  Unknown Words Encountered: 2
  Dictionary Size: 200 words
  Success Rate: 75.0%
  ```

- `history` - View translation history
  ```
  > history
  Translation History
  ==================================================
  1. English: hello
     Kannada: ಹಲೋ
  ```

- `clear` - Clear translation history
  ```
  > clear
  ✓ Translation history cleared
  ```

- `help` or `?` - Display help menu

- `exit` or `quit` - Exit the application

## Dictionary Contents

The application includes translations for:

- **Greetings**: hello, hi, goodbye, welcome, etc.
- **Common Words**: thank you, please, sorry, yes, no, etc.
- **Numbers**: zero through ten
- **Days of Week**: Monday through Sunday
- **Months**: January through December
- **Nouns**: food, water, house, car, book, etc.
- **Verbs**: go, come, run, walk, eat, drink, sleep, etc.
- **Adjectives**: good, bad, big, small, hot, cold, etc.
- **Time**: morning, afternoon, evening, night, today, tomorrow, etc.
- **Family Members**: father, mother, brother, sister, etc.
- **Colors**: red, blue, green, yellow, etc.
- **Body Parts**: head, eyes, nose, hand, leg, etc.
- **Travel & Places**: hotel, restaurant, train, airport, etc.

## Project Structure

```
ENGLISH-TO-KANNADA--TRANSLATOR/
├── main.py              # Main CLI application
├── translator.py        # Core translation logic
├── dictionary.py        # Kannada dictionary database
├── test.py             # Test suite
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## API Usage (Programmatic)

You can also use the translator in your own Python code:

```python
from translator import Translator

# Create translator instance
translator = Translator()

# Translate a word
word_translation = translator.translate_word("hello")
print(word_translation)  # Output: ಹಲೋ

# Translate a sentence
sentence = "hello how are you"
translation = translator.translate_sentence(sentence)
print(translation)

# Translate a paragraph
paragraph = "Hello world. How are you?"
translation = translator.translate_paragraph(paragraph)
print(translation)

# Add word to dictionary
translator.add_word_to_dictionary("python", "ಪೈಥಾನ್")

# Search dictionary
results = translator.search_words("good")
print(results)

# Get statistics
stats = translator.get_translation_stats()
print(stats)

# Get translation history
history = translator.get_history()
for item in history:
    print(f"{item['english']} → {item['kannada']}")
```

## Testing

Run the test suite:

```bash
python test.py
```

Expected output:
```
==================================================
Running English-to-Kannada Translator Tests
==================================================

✓ Word translation tests passed
✓ Sentence translation tests passed
✓ Dictionary operation tests passed
✓ History tests passed
✓ Statistics tests passed
✓ Paragraph translation tests passed

==================================================
✓ All tests passed successfully!
==================================================
```

## Kannada Writing System

The Kannada script (ಕನ್ನಡ) is one of the major Dravidian languages spoken in Karnataka, India. This translator uses the official Kannada Unicode characters for translations.

Example translations:
- Hello → ಹಲೋ
- Thank you → ಧನ್ಯವಾದ
- Water → ನೀರು
- Beautiful → ಸುಂದರ

## Limitations

- Translations are literal word-to-word conversions
- Grammar rules specific to Kannada are not applied
- Proper nouns and specialized terminology may not be included
- For complex sentences, professional human translation is recommended

## Future Enhancements

- [ ] Advanced NLP for grammatical translations
- [ ] Machine Learning-based translation
- [ ] Web interface
- [ ] Mobile app
- [ ] Reverse Kannada to English translation
- [ ] Sentence structure analysis
- [ ] Multi-language support
- [ ] Translation API

## Contributing

Contributions are welcome! Feel free to:
- Add more words to the dictionary
- Improve translation accuracy
- Add new features
- Fix bugs
- Improve documentation

## License

This project is open source and available under the MIT License.

## Author

English to Kannada Translator Project

## Support

For issues or questions, please create an issue in the project repository.

---

**Happy Translating!** ಕನ್ನಡ ಭಾಷೆಗೆ ಸ್ವಾಗತ