# 基础镜像
FROM python:3.12-slim

# 镜像维护者
MAINTAINER user 2584278161@qq.com

# 设置docker工作目录
WORKDIR /data_clean

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到配置的WORKDIR下
COPY . .

# 暴露Streamlit默认端口
EXPOSE 8501

# 运行命令
CMD ["streamlit", "run", "home.py", "--server.address=0.0.0.0", "--server.port=8501"]