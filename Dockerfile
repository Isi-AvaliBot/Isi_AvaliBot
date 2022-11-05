FROM docker.io/ubuntu:22.10
LABEL AUTHOR="HUSKI3"

COPY . /

RUN apt update && apt install --no-install-recommends python3-pip -y

# Install Python dependencies 
COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"] 