@echo off
title Biblioteca Movil - .NET MAUI 10
cd /d "%~dp0"
echo ============================================================
echo   Iniciando Biblioteca Movil (.NET MAUI 10 - Windows)
echo ============================================================
echo Compilando y ejecutando en tu escritorio...
dotnet run -f net10.0-windows10.0.19041.0
if %errorlevel% neq 0 (
    echo.
    echo Hubo un problema al ejecutar. Presiona cualquier tecla para cerrar.
    pause >nul
)
