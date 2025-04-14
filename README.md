# data_clean

 --- 
 - 图像识别
 - pdf识别
 ---
### 项目启动
**1、环境配置**
```angular2html
.env文件配置到config文件下
```
**2、启动命令**
- 方式1：
```shell
cd ./data_clean
docker-compose up -d --build
```
- 方式2：
```shell
cd ./data_clean
docker build -t data-clean-app .
docker run -d -p 50003:8501 --name my-streamlit-app data-clean-app
```

### 版本说明
- dc-v1.0
```angular2html
1、支持图片上传识别
2、支持pdf上传识别
```