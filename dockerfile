# Sử dụng base image Python
FROM python:3.9-slim

# Thiết lập môi trường làm việc
WORKDIR /app

# Sao chép file yêu cầu vào container
COPY requirements.txt requirements.txt

# Cài đặt các gói Python cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ code vào container
COPY . .

# Expose port để chạy Streamlit (nếu cần)
EXPOSE 8501

# Lệnh chạy ứng dụng
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
