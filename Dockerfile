FROM python:3.10.8
WORKDIR /py-exposer
COPY requirements.txt /py-exposer/
RUN pip install -r requirements.txt
COPY . /py-exposer
CMD python main.py