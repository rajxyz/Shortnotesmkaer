import spacy
from datetime import datetime

# Load the language model
nlp = spacy.load("en_core_web_sm")

def extract_key_terms(text):
    doc = nlp(text)
    key_terms = []
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'GPE', 'PRODUCT', 'NORP', 'PERSON']:
            key_terms.append(ent.text)
    return key_terms

def extract_main_ideas(text):
    # This is just a simple placeholder for main ideas extraction
    doc = nlp(text)
    main_ideas = [sent.text for sent in doc.sents if len(sent.text.split()) > 10]
    return main_ideas

def extract_questions_and_answers(text):
    # Placeholder logic: returns sentences that look like questions
    doc = nlp(text)
    questions = [sent.text for sent in doc.sents if '?' in sent.text]
    return questions

def extract_important_dates(text):
    doc = nlp(text)
    important_dates = [ent.text for ent in doc.ents if ent.label_ == 'DATE']
    return important_dates

def extract_headings(text):
    # Placeholder for headings extraction based on capitalized text
    doc = nlp(text)
    headings = [sent.text for sent in doc.sents if sent.text.isupper()]
    return headings

def extract_examples(text):
    # Placeholder for examples, looking for words like 'for example', 'e.g.', etc.
    doc = nlp(text)
    examples = [sent.text for sent in doc.sents if 'for example' in sent.text.lower() or 'e.g.' in sent.text.lower()]
    return examples

def extract_highlighted_text(text):
    # Placeholder for highlighted text logic (this could be based on some custom tags or emphasis)
    highlighted_text = [sent.text for sent in text.split("\n") if "*" in sent]
    return highlighted_text

def extract_bullet_points(text):
    # Placeholder for bullet points extraction, assuming lines starting with '-'
    bullet_points = [line.strip() for line in text.split('\n') if line.strip().startswith('-')]
    return bullet_points

def extract_relationships(text):
    # Placeholder for relationships, simply returning noun chunks for now
    doc = nlp(text)
    relationships = [chunk.text for chunk in doc.noun_chunks]
    return relationships

def extract_citations(text):
    # Placeholder for citation extraction, looking for references like [Author, Year]
    citations = [sent.text for sent in nlp(text).sents if "[" in sent.text and "]" in sent.text]
    return citations

def extract_content(text, extract_type):
    if extract_type == "keyTerms":
        return extract_key_terms(text)
    elif extract_type == "mainIdeas":
        return extract_main_ideas(text)
    elif extract_type == "questions":
        return extract_questions_and_answers(text)
    elif extract_type == "importantDates":
        return extract_important_dates(text)
    elif extract_type == "headings":
        return extract_headings(text)
    elif extract_type == "examples":
        return extract_examples(text)
    elif extract_type == "highlightedText":
        return extract_highlighted_text(text)
    elif extract_type == "bulletPoints":
        return extract_bullet_points(text)
    elif extract_type == "relationships":
        return extract_relationships(text)
    elif extract_type == "citations":
        return extract_citations(text)
    else:
        return "Invalid extraction type"
