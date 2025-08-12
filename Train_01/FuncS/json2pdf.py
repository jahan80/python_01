import base64
import json


def json_to_pdf(json_path, output_pdf_path):
    # 1 Read file
    with open(json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    #conver to base 64
    pdf_base64 = data['pdf_base64']

    #
    pdf_bytes = base64.b64decode(pdf_base64)

    # save to pdf
    with open(output_pdf_path, 'wb') as pdf_file:
        pdf_file.write(pdf_bytes)

    print(f"file created {output_pdf_path} ")


#
json_path = r"C:\Users\m.jahangiri\Desktop\temp\electronic_document.json"  # input
output_pdf_path = r"C:\Users\m.jahangiri\Desktop\temp\restored.pdf"  # output

# exec fun
json_to_pdf(json_path, output_pdf_path)