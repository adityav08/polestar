# Using Python3.7
FROM python:3.7

WORKDIR /polestar

ADD . /polestar

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py"]
