import base64
import json


#
def pdf_to_base64(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")  #
    return pdf_base64


#
def save_to_json(base64_data, output_json_path):
    data = {
        "pdf_name": "example.pdf",
        "pdf_base64": base64_data  #
    }

    with open(output_json_path, "w") as json_file:
        json.dump(data, json_file, indent=4)  #


#
pdf_path = r"C:\Users\m.jahangiri\Desktop\temp\electronic_document.pdf"  #
output_json_path = r"C:\Users\m.jahangiri\Desktop\temp\electronic_document.json"  #

#
base64_data = pdf_to_base64(pdf_path)
save_to_json(base64_data, output_json_path)

print(f"file created {output_json_path} ")