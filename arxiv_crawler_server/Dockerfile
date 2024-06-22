FROM python:3.10

MAINTAINER Theron Tau

copy . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN RUN apt-get update && apt-get install -y cron

ENV CRON_SCHEDULE = "0 12 * * *"
ENV KEYWORDS = "physics,diffusion,quantitative finance"
ENV MAX_RESULTS = "8,6,6"

RUN crontab -l > temp_cron && echo "$CRON_SCHEDULE /usr/local/bin/cronjob.sh" >> temp_cron && crontab temp_cron && rm temp_cron

CMD ["streamlit", "run", "web_ui.py"]

EXPOSE 8501
