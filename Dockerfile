FROM python3.10-slim

WORKDIR /app
COPY . /app

EXPOSE 8080
CMD streamlit run app.py --server.port=8080 --server.address=0.0.0.0