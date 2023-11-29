# atv 12 sem entrega

FROM python:3.11-slim

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt
COPY ./scr /code
#aqui tu pode só tirar o scr e deixar ./ /code *TEM QUE ESTAR COM IGUAL AQUI

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
ENTRYPOINT ["python"]
CMD ["apiPastelaria.py"]