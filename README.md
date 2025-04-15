# 🍉 data_clean

 --- 
 - 图像识别
 - pdf识别
 ---
### 🧰 项目启动
**1、⚙ 项目环境配置**
```shell
git clone https://github.com/DDongAI/data_clean.git
```
```angular2html
.env文件配置到config文件夹下
```
**2、⚙ 启动命令**
- 🛠 方式1：
```shell
cd data_clean
```
```shell
docker-compose up -d --build
```
- 🛠 方式2：
```shell
cd data_clean
```
```shell
docker build -t data-clean-app .
```
```shell
docker run -d -p 50003:8501 --name my-streamlit-app data-clean-app
```
--- 
### Ⓥ 版本说明
- 🔄 v-1.0
```angular2html
1、支持图片上传识别
2、支持pdf上传识别
```
