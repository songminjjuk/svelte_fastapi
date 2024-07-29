FROM public.ecr.aws/docker/library/python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn","main:app","--host","0.0.0.0"]
