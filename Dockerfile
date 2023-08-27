FROM nvidia/cuda:12.2.0-base-ubuntu22.04
RUN apt update && apt upgrade -y
RUN apt install python3 python3-pip -y
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "streamlit", "run", "app.py" ]
CMD [ "--server.port", "80" ]
EXPOSE 80