FROM python:3.10.0-alpine3.15
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY scr scr  
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
        CMD curl -f http://localhost:3000/health || exit 1
ENTRYPOINT [ "python", "./scr/app.py" ]  
