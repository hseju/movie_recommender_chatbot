# FROM rasa/rasa:3.0.0

# WORKDIR /app

# COPY . /app

# COPY requirements.txt /app/requirements.txt
# RUN pip install --verbose -r requirements.txt
# USER root
# # WORKDIR /app
# # COPY . /app
# COPY ./data /app/data

# RUN  rasa train

# VOLUME /app
# VOLUME /app/data
# VOLUME /app/models
# CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]


FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==1.5.3
ADD . /app/
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh