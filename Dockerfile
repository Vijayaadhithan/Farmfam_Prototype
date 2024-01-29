FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY Data_Preprocessing.py .
COPY db_conn.py .

# Make port 8080 available to the world outside this container
EXPOSE 8080

CMD ["python", "db_conn.py", "&&", "python", "Data_Preprocessing.py"]

