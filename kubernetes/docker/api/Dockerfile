FROM python:3
USER root
WORKDIR /root

COPY ./*.py ./
COPY ./requirements.txt ./requirements.txt

#RUN apt-get update
#RUN apt-get -y install locales && \
#    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "./api.py", "0.0.0.0", "5001"]