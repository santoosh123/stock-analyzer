FROM python:3.13.6-slim-trixie
WORKDIR /docker
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "flask", "--app", "loan", "run", "--host=0.0.0.0"]