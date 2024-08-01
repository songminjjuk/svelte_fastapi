#FROM public.ecr.aws/docker/library/python:3.9-slim
FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh
#
ENV DB_URL=mysql+pymysql://admin:test1234@database-1.cny8owwkaw4k.ap-northeast-2.rds.amazonaws.com/test
ENTRYPOINT ["/app/entrypoint.sh"]