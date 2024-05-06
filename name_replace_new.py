import openai
import pandas as pd
import random
import time

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

# # Process each row in the specified column
# print(" .......Processing each rows......")
# excel_data['Statement'] = excel_data['words'].apply(lambda x: extract_and_replace_names(x, indian_names))


print(" .......Processing each rows......")

row_count = 0  # Initialize a counter for rows
for index, row in excel_data.iterrows():
    excel_data.at[index, 'Updated Question Statement'] = extract_and_replace_names(row['Question Statement (character limit 335)'], indian_names)
    row_count += 1

    # Check if 50 rows have been processed
    if row_count % 50 == 0:
        print(f"Processed {row_count} rows, pausing for 2 seconds...")
        time.sleep(2)  # Pause for 2 seconds


print(" .......Excel Created ......")
excel_data.to_excel('English\English_5_new.xlsx', index=False)


