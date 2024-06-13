FROM python:3.10-slim

# Set build-time environment variables
ARG GOOGLE_API_KEY
ARG MOONSHOT_API_KEY

ENV GOOGLE_API_KEY=$GOOGLE_API_KEY
ENV MOONSHOT_API_KEY=$MOONSHOT_API_KEY

WORKDIR /app
COPY . /app
RUN rm /app/.env

EXPOSE 8080
RUN pip install -r requirements.txt
CMD streamlit run home.py --server.port=8080 --server.address=0.0.0.0