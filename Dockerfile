# Étape de build
FROM gcc:13 AS build
WORKDIR /app
COPY output.cpp .
RUN g++ -O2 -o subtilizer output.cpp

# Étape finale minimale
FROM debian:stable-slim
WORKDIR /app
COPY --from=build /app/subtilizer .
CMD ["./subtilizer"] 