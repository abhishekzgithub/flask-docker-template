FROM python:3.6-alpine
COPY . /
RUN pip3 install --user -r requirements.txt
EXPOSE 9091
WORKDIR /
CMD ["/bin/sh","run.sh"]