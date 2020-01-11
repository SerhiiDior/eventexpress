FROM python:3.7

RUN apt-get update && apt-get install && apt-get install git -y  --no-install-recommends \
		libpq-dev \
                default-libmysqlclient-dev \
        && rm -rf /var/lib/apt/lists/*
        
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

#install xvfb
RUN apt-get install -yqq xvfb
        
# #set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null



RUN apt-get update && apt-get upgrade && apt-get install git -y
RUN apt install python3-pip -y
RUN git clone https://github.com/SerhiiDior/eventexpress


WORKDIR /eventexpress
RUN mkdir /Reports_Allure

RUN pip3 install -r requirements.txt

ENTRYPOINT ["pytest"," --alluredir ./Reports_Allure  ./Tests"]




