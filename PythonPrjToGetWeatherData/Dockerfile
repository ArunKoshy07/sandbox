FROM python:3.6.4
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
CMD ["ls", "-ltr"]
CMD ["sh", "\jobscripts\runJob.sh"]