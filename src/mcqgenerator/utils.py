import os
import PyPDF2
import json
import logging
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PyPDF2.PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text
            
        except Exception as e:
            raise Exception(e)
        
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "unsupported file format only pdf and text file suppoted"
            )

def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        # iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join([f"{option}-> {option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data

    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        logging.error(f"quiz_str: {quiz_str}")
        return False
    
    except Exception as e:
        logging.error(f"Unexpected error in get_table_data: {e}")
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False