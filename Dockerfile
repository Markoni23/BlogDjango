FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /MyCoolBlog
WORKDIR /MyCoolBlog
COPY . /MyCoolBlog/
RUN pip install -r requirements.txt