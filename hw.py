# – Запаковать кодом в zip архив несколько разных файлов: pdf, xlsx, csv;
# – Положить его в ресурсы;
# – Реализовать чтение и проверку содержимого каждого файла из архива не распаковывая сам архив


from pypdf import PdfReader
from openpyxl import load_workbook


# from csv23 import - Что импортировать?

