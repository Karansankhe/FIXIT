-------------------------------------------Call Transcript Sentiment Analysis------------------------------------------------


-----------------------------------------Frontend Documentation: Streamlit Application------------------------------------------
Overview
This Streamlit application allows users to upload call transcripts, analyze their sentiment, and visualize the results. The application requires user authentication and performs sentiment analysis using a backend Flask server.

Features
File Upload:
Users can upload a .txt file containing a call transcript.

Sentiment Analysis:
On file submission, the file is sent to the Flask backend for sentiment analysis.
Displays the sentiment label and score.

Visualizations:
Pie Chart: Shows the distribution of sentiment scores (Positive, Negative, Neutral).
Horizontal Bar Chart: Visualizes sentiment scores.
Word Cloud: Displays a visual representation of the most frequent words in the transcript.
Additional Bar Chart: Shows sentiment score distribution.


-----------------------------------------Backend Documentation: Flask Application---------------------------------------------
Overview
This Flask application handles file uploads, performs sentiment analysis, and returns the results. It uses the transformers library for sentiment analysis and supports cross-origin requests.

Features
File Upload:
Accepts .txt files through POST requests.
Saves the file to a server directory.

Sentiment Analysis:
Analyzes the sentiment of the uploaded file using the transformers pipeline.
Handles long text by splitting it into chunks.

Error Handling:
Returns appropriate error messages for missing files, empty filenames, or analysis failures.

----------------------------------------Sentimentanalysis of the Text----------------------------------------------------------
Model Used:
a pre-trained model from the transformers library is used. Specifically:

Sentiment Analysis Pipeline: This uses a pre-trained model for sentiment classification. The pipeline('sentiment-analysis') function creates a pipeline for sentiment analysis.
Tokenizer: The tokenizer, AutoTokenizer.from_pretrained('distilbert-base-uncased'), is used to convert text into tokens that the model can process.



