FROM python:3.7

ADD find_the_vendor_mac.py /

RUN pip install requests

CMD [ "python", "./find_the_vendor_mac.py" ]
