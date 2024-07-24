Call Transcript Sentiment Analysis
Frontend Documentation: Streamlit Application
Overview
This Streamlit application allows users to upload call transcripts, analyze their sentiment, and visualize the results. The application interacts with a backend Flask server for sentiment analysis and supports user authentication.

Features

File Upload:
Functionality: Users can upload a .txt file containing a call transcript.
File Type: .txt only.
Sentiment Analysis:

Process: Upon file submission, the file is sent to the Flask backend for sentiment analysis.
Display: Shows the sentiment label (Positive, Negative, Neutral) and score.
Visualizations:

Pie Chart: Illustrates the distribution of sentiment scores (Positive, Negative, Neutral).
Horizontal Bar Chart: Visualizes the sentiment scores for different categories.
Word Cloud: Displays a visual representation of the most frequent words in the transcript.
Additional Bar Chart: Shows the sentiment score distribution.

Backend Documentation: Flask Application
Overview
The Flask application handles file uploads, performs sentiment analysis, and returns the results. It uses the transformers library for sentiment analysis and supports cross-origin requests.

Features
File Upload:
Functionality: Accepts .txt files through POST requests.
Storage: Saves the uploaded file to a server directory (uploads).

Sentiment Analysis:
Process: Analyzes the sentiment of the uploaded file using the transformers pipeline.
Chunk Handling: Handles long texts by splitting them into manageable chunks to fit the model’s token limit.
Error Handling:

File Errors: Returns appropriate error messages for missing files, empty filenames, or issues during analysis.
Sentiment Analysis of the Text
Model Used:

Sentiment Analysis Pipeline:
Functionality: Utilizes a pre-trained model for sentiment classification.
Implementation: The pipeline('sentiment-analysis') function from the transformers library creates a pipeline specifically for sentiment analysis.
Tokenizer:

Purpose: Converts text into tokens that the model can process.
Model: AutoTokenizer.from_pretrained('distilbert-base-uncased') is used for tokenization.
How It Works:

Tokenization:
Process: The text is tokenized into subword units or tokens using the tokenizer.
Analysis:

Pipeline Execution: The tokenized text is passed through the sentiment analysis pipeline, which classifies the sentiment and provides a score.
Handling Long Texts:

Chunking: Long texts are split into smaller chunks to adhere to the model's token limit and avoid processing issues.
Result Aggregation:

Combining Results: Results from individual chunks are aggregated to produce a final sentiment score and label.
Token Limit:

Maximum Tokens: The distilbert-base-uncased model has a maximum token limit of 512 tokens per input. Text exceeding this limit is split into chunks for processing.


