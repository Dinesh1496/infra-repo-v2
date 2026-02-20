FROM python:3.13.3-slim
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY ./source /source
EXPOSE 5000
CMD [ "python" , "/source/app.py" ]
