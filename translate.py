import os
import openai

# Set OpenAI API Key and API Base
openai.api_key = os.environ.get('CHATGPT_API_KEY')
openai.api_base = os.environ.get('CHATGPT_API_BASE')

# Define the translation function
def translate_file(input_file, output_file):
    # Read the content of the input file
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read()
        #print(input_text)

    # Use OpenAI API to translate
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Translate the following Chinese text into English:\n\n{}\n\nEnglish:".format(input_text)}]
    )

    # Get the translation result
    output_text = completion.choices[0].message.content

    # Write to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output_text)

# Translate all .md files in the docstest directory
for filename in os.listdir("docstest"):
    if filename.endswith(".md"):
        # Get the file name and extension
        file_name, file_ext = os.path.splitext(filename)

        # Translate the file name
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Translate the following Chinese text into English:\n\n{}\n\nEnglish:".format(filename)}]
        )

        # Get the translation result
        file_name_en = completion.choices[0].message.content

        # Create a new file
        output_file = os.path.join("docstest", "en", f"{file_name_en}")

        # Translate the content of the file
        input_file = os.path.join("docstest", filename)
        translate_file(input_file, output_file)

        print(f"Translated {input_file} to {output_file}")