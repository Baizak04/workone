import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)
    
    return sentences

def generate_response(user_input, sentences):
    # Add the user input to the list of sentences
    sentences.append(user_input)
    
    # Preprocess the sentences and convert them into TF-IDF vectors
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    
    # Calculate the cosine similarity between the user input and all other sentences
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    
    # Find the most similar sentence
    most_similar_sentence_index = similarity_scores.argmax()
    
    # Generate the response based on the most similar sentence
    response = sentences[most_similar_sentence_index]
    
    return response

def chat():
    print("Chatbot: Hello! How can I assist you today?")
    print("Chatbot: Type 'exit' to end the conversation.")
    
    # Define a list of predefined sentences for the chatbot
    predefined_sentences = [
        "Hello",
        "How are you?",
        "What is your name?",
        "Tell me a joke",
        "What is the meaning of life?",
        "Who is your creator?"
    ]
    
    # Preprocess the predefined sentences
    sentences = preprocess_text(" ".join(predefined_sentences))
    
    # Start the conversation loop
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        response = generate_response(user_input, sentences)
        print("Chatbot:", response)

chat()