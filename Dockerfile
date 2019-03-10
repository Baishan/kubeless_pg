from python:2.7

ADD ./requirements.txt .
RUN pip install -r requirements.txt

ADD ./hello.py .
ADD ./consumer.py .
CMD ["python", "./consumer.py"] 
