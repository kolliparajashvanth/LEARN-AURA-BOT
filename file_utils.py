import os
from fpdf import FPDF


def convert_file(file_path):
    try:
        if file_path.endswith(".txt"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            with open(file_path, "r") as f:
                for line in f:
                    pdf.cell(200, 10, txt=line.strip(), ln=True)
            output = file_path.replace(".txt", ".pdf")
            pdf.output(output)
            return output
        return None
    except Exception as e:
        print("Conversion error:", e)
