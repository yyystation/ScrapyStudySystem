# Create your views here.
from django.http import HttpResponse
import json


if __name__ == '__main__':
    with open(r"C:\Users\Dell\Desktop\spider\ted_data.json", encoding='utf-8') as f:
        data = f.read()
    data = json.loads(data)
