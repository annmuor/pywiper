FROM python
RUN mkdir -p /app
WORKDIR /app
ADD pywiper.py pywiper.py
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt