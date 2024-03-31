FROM python:3.12.2

RUN wget https://mdipierro.pythonanywhere.com/examples/static/web2py_src.zip &&\
  unzip web2py_src.zip -d /app &&\
  rm web2py_src.zip

RUN apt-get update

ENV WORK_DIR=/app/web2py/applications/schoolmanager

WORKDIR ${WORK_DIR}

COPY . .
COPY ./routes.py /app/web2py/routes.py

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "./service_entrypoint.sh" ]
