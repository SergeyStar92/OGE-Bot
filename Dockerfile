FROM python:3.12
COPY . .
RUN pip3 install -r requirements.txt
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Novosibirsk /etc/localtime
RUN echo "Asia/Novosibirsk" > /etc/timezone
CMD python main.py
