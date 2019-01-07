from pdf_parser import extract_text_from_pdf
from model import Report
import re 

def generate_reports(text):
    reports = []
    for chunk in text.split('Case Log Media')[1:]:
        re.sub('\s+', ' ', chunk)
        for report in chunk.split('Date Reported:')[1:]:
            """
            While the pdf scanner can accurately parse the text, the order can be quite random.
            For this reason we must handle multiple location cases, thus we use regex.
            """
            print(report)
            r = Report(
                 int(re.findall(r'(\d{6})', report)[-1]),
                 re.findall(r'\d{2}/\d{2}/\d{2}', report)[0],
                 re.findall(r'(?<=Location\s:\s)(.*)(?=Address)', report)[-1].strip(), 
                 re.findall(r'(?<=Case\sIncident\(s\):)(.*)(?=Synopsis)', report)[-1])
            reports.append(r)
            print(r)


def main(pdfs):
    text = {}
    for pdf in pdfs:
        text[pdf] = extract_text_from_pdf('data/' + pdf + '.pdf')
        generate_reports(text[pdf])


if __name__ == '__main__':
    main(['dec_2018'])