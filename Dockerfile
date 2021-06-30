FROM python:3

RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]
EXPOSE 8000