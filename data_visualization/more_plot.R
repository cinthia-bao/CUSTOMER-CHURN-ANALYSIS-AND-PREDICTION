library(ggplot2)

# Cargar los datos
datos <- read.csv("dataset_modif/train_clean.csv")

# Crear el histograma y guardarlo en una variable
p <- ggplot(datos, aes(x = CreditScore)) +
  geom_histogram(binwidth = 50, fill = "skyblue", color = "black") +
  labs(title = "Histograma de Credit Score",
       x = "Credit Score",
       y = "Frecuencia") +
  theme_minimal()

# Guardar el gráfico como imagen
ggsave("Histograma_de_Credit_Score.png", plot = p, width = 8, height = 6)

