#!/usr/bin/env python3
"""
Flask web application for English to Kannada Translator
"""

from flask import Flask, render_template, request, jsonify
from translator import Translator
import json

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    """Render main page."""
    return render_template('index.html')

@app.route('/api/translate-word', methods=['POST'])
def translate_word_api():
    """API endpoint to translate a single word."""
    try:
        data = request.json
        word = data.get('word', '').strip()
        
        if not word:
            return jsonify({'error': 'Word is required'}), 400
        
        translation = translator.translate_word(word)
        
        if translation:
            return jsonify({
                'english': word,
                'kannada': translation,
                'found': True
            })
        else:
            return jsonify({
                'english': word,
                'found': False,
                'message': f'Word "{word}" not found in dictionary'
            }), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/translate-sentence', methods=['POST'])
def translate_sentence_api():
    """API endpoint to translate a sentence."""
    try:
        data = request.json
        sentence = data.get('sentence', '').strip()
        
        if not sentence:
            return jsonify({'error': 'Sentence is required'}), 400
        
        translation = translator.translate_sentence(sentence)
        
        return jsonify({
            'english': sentence,
            'kannada': translation,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/translate-paragraph', methods=['POST'])
def translate_paragraph_api():
    """API endpoint to translate a paragraph."""
    try:
        data = request.json
        paragraph = data.get('paragraph', '').strip()
        
        if not paragraph:
            return jsonify({'error': 'Paragraph is required'}), 400
        
        translation = translator.translate_paragraph(paragraph)
        
        return jsonify({
            'english': paragraph,
            'kannada': translation,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/search', methods=['POST'])
def search_api():
    """API endpoint to search dictionary."""
    try:
        data = request.json
        term = data.get('term', '').strip()
        
        if not term:
            return jsonify({'error': 'Search term is required'}), 400
        
        results = translator.search_words(term)
        
        return jsonify({
            'term': term,
            'results': results,
            'count': len(results)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/add-word', methods=['POST'])
def add_word_api():
    """API endpoint to add a new word."""
    try:
        data = request.json
        english = data.get('english', '').strip()
        kannada = data.get('kannada', '').strip()
        
        if not english or not kannada:
            return jsonify({'error': 'Both English and Kannada words are required'}), 400
        
        message = translator.add_word_to_dictionary(english, kannada)
        
        return jsonify({
            'status': 'success',
            'message': message,
            'english': english,
            'kannada': kannada
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats', methods=['GET'])
def stats_api():
    """API endpoint to get translation statistics."""
    try:
        stats = translator.get_translation_stats()
        stats['dictionary_size'] = translator.get_dictionary_size()
        
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def history_api():
    """API endpoint to get translation history."""
    try:
        history = translator.get_history()
        
        return jsonify({
            'history': history,
            'count': len(history)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear-history', methods=['POST'])
def clear_history_api():
    """API endpoint to clear translation history."""
    try:
        translator.clear_history()
        
        return jsonify({
            'status': 'success',
            'message': 'History cleared'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/dictionary-size', methods=['GET'])
def dictionary_size_api():
    """API endpoint to get dictionary size."""
    try:
        size = translator.get_dictionary_size()
        
        return jsonify({
            'dictionary_size': size
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment."""
    return jsonify({
        'status': 'healthy',
        'service': 'English-to-Kannada Translator',
        'dictionary_size': translator.get_dictionary_size()
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
