# MCQ Generator

This project is a streamlit application that generates Multiple Choice Questions (MCQs) from text input (PDF or TXT files) using OpenAI's GPT-3.5-turbo model. The application allows users to generate, review, and evaluate quizzes based on the content of the uploaded files.

## Features

- **File Upload:** Upload PDF or TXT files to extract text.
- **MCQ Generation:** Automatically generate a specified number of MCQs based on the text.
- **Dynamic Quiz Table:** View the generated MCQs in a table format.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/akhilesh1709/mcq-generator.git
   cd mcq-generator
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload a File:** Use the file uploader to upload a PDF or TXT file.
2. **Set Parameters:** Enter the number of MCQs, subject, and tone of the questions.
3. **Generate MCQs:** Click on "Create MCQs" to generate the quiz.
4. **View Results:** The generated MCQs will be displayed in a table format.

## Project Structure

- `app.py`: Main entry point for the Streamlit application.
- `src/`: Contains utility functions and additional logic for MCQ generation.
- `response.json`: Template JSON file used to format the quiz output.
