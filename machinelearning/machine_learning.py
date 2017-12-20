import subprocess
import os


def parse_text_file(file):
    with open('uploads/' + file, 'r') as f:
        return f.readline()

def create_pdf():
    WORKING_DIRECTORY = os.getcwd()
    WK2PDF = os.path.join(os.sep, WORKING_DIRECTORY, 'machinelearning', 'wk', 'wkhtmltox', 'bin', 'wkhtmltopdf')

    if not os.path.exists('pdfs'):
        os.mkdir('pdfs')

    PDF_FOLDER = os.path.join(WORKING_DIRECTORY, 'pdfs')
    WK_DIR = os.path.abspath(WK2PDF)

    subprocess.call([WK_DIR, '-g', 'http://www.twotickets.de', './pdfs/news.pdf'], shell=False)
    PDF_FILE = os.path.join(PDF_FOLDER, 'news.pdf')

    #Shows the ls in the folder. You can look at it in the run server window.
    subprocess.call(['ls', PDF_FOLDER])
    return PDF_FILE
