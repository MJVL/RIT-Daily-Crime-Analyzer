from utility.pdf_parser import extract_text_from_pdf
from model.report import Report
import re 

def generate_reports(text):
    """
    While the pdf scanner can accurately parse the text, the order can be quite random.
    For this reason we must handle countless location and formatting cases, thus we use regex.
    """
    reports = []
    for chunk in text.split('Case Log Media')[1:]:
        re.sub('\s+', ' ', chunk)
        for report in chunk.split('Date Reported:')[1:]:
            r = Report(
                 int(re.findall(r'(\d{6})', report)[-1]) if len(re.findall(r'(\d{6})', report)) > 0 else reports[-1].report_number + 1,
                 re.findall(r'\d{2}/\d{2}/\d{2}', report)[0],
                 re.findall(r'(?<=Location\s:\s)(.*)(?=Address)', report)[-1].strip() if len(re.findall(r'(?<=Location\s:\s)(.*)(?=Address)', report)) > 0 else re.findall(r'(?<=\d:\d{2})(.*)(?<=LOT)', report)[-1].strip(),
                 re.findall(r'(?<=Case\sIncident\(s\):)(.*)(?=Synopsis)', report)[-1].strip())
            reports.append(r)
    return reports


def main(pdfs):
    text = {}
    for pdf in pdfs:
        text[pdf] = extract_text_from_pdf('data/' + pdf + '.pdf')
        print(generate_reports(text[pdf]))


if __name__ == '__main__':
    main(['dec_2018'])