# Используем актуальный slim-образ для баланса между размером и совместимостью
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Создаем непривилегированного пользователя (Security Best Practice)
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Копируем код приложения
COPY app.py .

# Меняем владельца и права
RUN chown -R appuser:appgroup /app

# Переключаемся на пользователя
USER appuser

# Документируем порт, который приложение слушает по умолчанию
EXPOSE 8080

# Запускаем приложение
CMD ["python", "app.py"]
