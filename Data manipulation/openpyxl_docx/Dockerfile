FROM python:latest

WORKDIR /Data manipulation/openpyxl_docx/

COPY openpyxl_script.py list.xlsx ./

RUN pip install transliterate openpyxl googletrans==3.1.0a0

CMD ["python", "./openpyxl_script.py"]

