from textblob import TextBlob
import pandas as pd
import numpy as np
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def validate_textual_analysis(text):
    quality_score = 0

    # Completeness check (dummy check for length)
    completeness = len(text) > 100
    quality_score += completeness * 0.4

    # Coherence check
    coherence = TextBlob(text).correct()
    quality_score += coherence * 0.3

    # Relevance check (dummy keyword check)
    relevance = any(keyword in text.lower() for keyword in ["market", "stock", "analysis"])
    quality_score += relevance * 0.3

    return quality_score >= 0.7  # Threshold for acceptance

def validate_numerical_data(data):
    quality_score = 0

    # Completeness check
    completeness = data.notnull().mean().mean()
    quality_score += completeness * 0.4

    # Accuracy check (dummy check, replace with actual benchmark comparison)
    accuracy = 1.0 if data['price'].mean() > 0 else 0.0
    quality_score += accuracy * 0.3

    # Consistency check
    consistency = 1.0 if data['price'].dtype == 'float64' else 0.0
    quality_score += consistency * 0.3

    return quality_score >= 0.7  # Threshold for acceptance

def validate_mixed_data(data, text):
    numerical_quality = validate_numerical_data(data)
    textual_quality = validate_textual_analysis(text)
    return numerical_quality and textual_quality

def validate_data(data, data_type, text=None):
    if data_type == "textual":
        return validate_textual_analysis(data)
    elif data_type == "numerical":
        return validate_numerical_data(data)
    elif data_type == "mixed":
        return validate_mixed_data(data, text)
    else:
        raise ValueError("Unknown data type")

# CHATGPT 

def query_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def validate_data(data):
    factors = {
        "completeness": "Check if all required fields are filled and optional fields are appropriately filled.",
        "accuracy": "Compare data against known benchmarks or historical data for error rates.",
        "consistency": "Ensure data follows expected formats and check for duplications.",
        "relevance": "Assess if the data is pertinent to market insights and is up-to-date.",
        "validity": "Verify data conforms to industry standards and maintains logical integrity.",
        "coherence": "Evaluate the coherence of textual data and logical consistency.",
        "richness": "Determine the level of detail and comprehensive coverage.",
        "usability": "Assess ease of interpretation and presence of documentation.",
        "authenticity": "Validate the source and ensure data genuineness.",
        "innovation": "Evaluate novelty and predictive value of the data.",
        "security": "Check compliance with privacy regulations and data encryption.",
        "user_feedback": "Collect ratings and reviews, and check community endorsements."
    }

    scores = {}
    for factor, prompt in factors.items():
        query = f"Evaluate the following data for {factor}: {data}\n{prompt}"
        score = query_chatgpt(query)
        scores[factor] = float(score) if score.replace('.', '', 1).isdigit() else 0

    # Aggregate scores with weights (example weights, adjust as needed)
    weights = {
        "completeness": 0.1,
        "accuracy": 0.1,
        "consistency": 0.1,
        "relevance": 0.1,
        "validity": 0.1,
        "coherence": 0.1,
        "richness": 0.05,
        "usability": 0.05,
        "authenticity": 0.1,
        "innovation": 0.05,
        "security": 0.1,
        "user_feedback": 0.05
    }

    total_score = sum(scores[factor] * weights[factor] for factor in scores)
    return total_score >= 0.7  # Example threshold for acceptance

# Example data
data = {
    'price': [100, 200, 150],
    'market': ['stock', 'crypto', 'stock'],
    'analysis': 'This is a detailed market analysis...',
    'source': 'Reputable Source'
}

is_valid = validate_data(data)
print("Data is valid:", is_valid)