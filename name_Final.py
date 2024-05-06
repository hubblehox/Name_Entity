# import pandas as pd
# from langchain.chains import create_extraction_chain
# from langchain_openai import ChatOpenAI

# class DataProcessor:
#     def __init__(self, file_path, schema, model='gpt-3.5-turbo-1106', temperature=0):
#         self.file_path = file_path
#         self.schema = schema
#         self.llm = ChatOpenAI(temperature=temperature, model=model)
#         self.chain = create_extraction_chain(schema, self.llm)

#     def read_excel(self):
#         data = pd.read_excel(self.file_path, usecols='M')
#         for index, row in data.iterrows():
#             inp =(f"Row {index + 1}: {row['Question Statement (character limit 335)']}")
#             return self.chain.invoke(inp)

# # Usage
# file_path = "F:/Company_Data/11_Name_entity/English/English_5.xlsx"
# schema = {
#     "properties": {
#         "name": {"type": "string"}
#     },
#     "required": ["name"]
# }

# processor = DataProcessor(file_path, schema)
# processor.read_excel()  # To read and print the excel file

import openai
import pandas as pd
import random
from openai import OpenAI
client = OpenAI()

def extract_and_replace_names(sentence,indian_names):
    # Use OpenAI's API to identify names in the sentence
    #prompt = f"Identify the person name from this: '{sentence}'",
    prompt = f'''Sentence: '{sentence}' with Indian Names: {indian_names}\n '''
        
     
    system_prompt = f'''
        1. "You are a text processing AI. Your task is to identify and replace "
        2. "non-Indian person names in the sentence with an Indian person name from the provided list. "
        3. "Here are a few examples:" for this sentence 
        'John and Mary went to the market' with 'Aarav and Aditi went to the market'.
        4. response or output must provided in full sentence not in list.
        5. Take care about gender while replace person mane
    '''
    response = client.chat.completions.create(
        model = "gpt-4-1106-preview",
        seed=123,
        messages = [
            {"role": "system", "content":system_prompt },
            {"role": "user","content":  prompt} ],
    
    )
    
    return response.choices[0].message.content.strip()

    # # # Replace each identified name with a random Indian name
    # # for name in names:
    # #     sentence = sentence.replace(name, random.choice(indian_names))

    # return names

# Load the Excel file
file_path = 'English\English_5_test.xlsx'
excel_data = pd.read_excel(file_path, usecols='M')


# Generating a list of 100 Indian names (mix of male and female) in Python

indian_names = [
    "Aarav", "Aditi", "Vijay", "Sunita", "Rohan", "Priya", "Nikhil", "Meera", "Karan", "Jyoti",
    "Ishaan", "Harsha", "Gautam", "Fatima", "Esha", "Deepak", "Chitra", "Bhavna", "Anjali", "Amit",
    "Akash", "Zara", "Yash", "Xavier", "Waseem", "Vasudha", "Urvashi", "Tushar", "Surya", "Shreya",
    "Shiv", "Riya", "Rakesh", "Pooja", "Om", "Naina", "Mohan", "Lata", "Kishore", "Kavita",
    "Kamal", "Jatin", "Inder", "Hema", "Gagan", "Farhan", "Ekta", "Dinesh", "Charu", "Bipin",
    "Bina", "Arjun", "Anushka", "Ankur", "Alok", "Alia", "Ajay", "Aisha", "Vivek", "Tanvi",
    "Swati", "Sumit", "Suhani", "Sudhir", "Siddharth", "Shilpa", "Shekhar", "Savitri", "Sarita", "Sandeep",
    "Samir", "Ritu", "Rajiv", "Pranav", "Pankaj", "Nidhi", "Neeraj", "Muskan", "Monica", "Milind",
    "Meenakshi", "Manoj", "Lakshmi", "Kunal", "Kirti", "Kiran", "Kapil", "Juhi", "Jignesh", "Jay",
    "Jasmin", "Irfan", "Hitesh", "Himani", "Harish", "Girish", "Geeta", "Feroz", "Divya", "Dhruv",
    "Darshan", "Chandan", "Bharti", "Atul", "Ashwin", "Arun", "Anil", "Ram", "Vikas", "Prashant", "Alok",
    "Bhavesh"]

# Process each row in the specified column
print(" .......Processing each rows......")
excel_data['Statement'] = excel_data['words'].apply(lambda x: extract_and_replace_names(x, indian_names))

#updated_column_m = excel_data.apply(lambda x: extract_and_replace_names(x,indian_names))

# Update and save the Excel file
#excel_data['M'] = updated_column_m

print(" .......Excel Created ......")
#excel_data['M'] = excel_data['Updated Question Statement']
excel_data.to_excel('English\English_5_new.xlsx', index=False)


