FROM python:3.8

COPY openpyxl_script.py .

RUN pip install transliterate openpyxl googletrans==3.1.0a0

CMD ["python", "./openpyxl_script.py"]

