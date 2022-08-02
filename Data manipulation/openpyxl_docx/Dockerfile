FROM python:3.8

COPY openpyxl_script.py list.xls .

RUN pip install transliterate openpyxl googletrans==3.1.0a0

CMD ["python", "Data manipulation/openpyxl_docx/openpyxl_script.py"]

