# MCQ Generator

This is a Streamlit application that generates multiple-choice questions (MCQs) based on a given text or PDF file. The application uses the LangChain library to interact with the OpenAI API and generate the quiz questions.

## Features

- **Upload File**: Users can upload a PDF or text file containing the content for which they want to generate MCQs.
- **Set MCQ Count**: Users can specify the number of MCQs they want to generate, with a range of 3 to 50.
- **Specify Subject**: Users can enter the subject for which the MCQs are being generated.
- **Set Complexity Level**: Users can set the complexity level of the generated questions, with the option to choose "Simple" as the default.
- **Generate MCQs**: The application generates the requested number of MCQs based on the uploaded content and the user's input.
- **Display MCQs**: The generated MCQs are displayed in a table format, showing the question, options, and the correct answer.

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
