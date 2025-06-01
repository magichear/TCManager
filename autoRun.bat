@echo off
chcp 65001 >nul
:: 设置后端和前端路径
set BACKEND_PATH=.
set FRONTEND_PATH=src\main\resources\fronter

:: 启动数据库服务
echo [INFO] 正在启动数据库服务...
start cmd /k "mysqld --console"
timeout /t 5 >nul

:: 启动后端服务
echo [INFO] 正在启动后端服务...
cd %BACKEND_PATH%
start cmd /k "mvn spring-boot:run"
cd /d %~dp0

timeout /t 2 >nul

:: 启动前端服务  注意！请关闭代理
echo [INFO] 正在启动前端服务...
cd %FRONTEND_PATH%
start cmd /k "python Broswer.py"
cd /d %~dp0

echo 前后端服务已启动！
:: pause