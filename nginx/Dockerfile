# Используем базовый образ Nginx 1.25 на основе Alpine Linux для минимизации размера контейнера
FROM nginx:1.25-alpine

# Удаляем дефолтный конфиг, чтобы не было конфликтов
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш конфиг
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Указываем, что контейнер будет слушать порт 80 (стандартный HTTP порт)
EXPOSE 80

# Запускаем nginx в foreground (требование для Docker)
CMD ["nginx", "-g", "daemon off;"]
