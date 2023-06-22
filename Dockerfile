FROM python:3

WORKDIR /usr/src/app

COPY ./server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./server/start_server.sh
SHELL ["/bin/bash", "-c"]
CMD ["./server/start_server.sh"]
EXPOSE 3000