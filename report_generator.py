from pdf_parser import extract_text_from_pdf
import re 

def generate_reports(text):
    reports = []
    for chunk in text.split('Case Log Media')[1:]:
        re.sub('\s+', ' ', chunk)
        for report in chunk.split('Date Reported:')[1:]:
            """
            while the pdf scanner can accurately parse the text,
            the index and location of it can be random within each report
            for this reason we must handle multiple location cases
            """
            keys = report.split(':')
            print(keys)
            print('Date Reported: ' + keys[0].split('-')[0].strip())
            print('Report #' + str(keys[-1]))
            print('Location ' + keys[3].replace('Address', '').strip())
            exit()
            #print('Date Reported:' + report)
            # print(dict(map(lambda s : s.split(':'), 'Date Reported:' + report)))

def main(pdfs):
    text = {}
    for pdf in pdfs:
        text[pdf] = extract_text_from_pdf('data/' + pdf + '.pdf')
        generate_reports(text[pdf])
    
if __name__ == '__main__':
    main(['dec_2018'])