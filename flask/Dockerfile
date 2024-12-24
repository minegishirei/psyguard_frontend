
# python version number:3.9.16
FROM python:3.9.16

# code ... directory for python codes.
WORKDIR /code

# copy localcode to container image.
COPY ./code /code

# upgrade pip command
RUN pip install --upgrade pip 

# install python lib 
RUN pip install -r requirements.txt

ENV GROQ_API_KEY=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