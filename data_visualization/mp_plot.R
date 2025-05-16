
library(ggplot2)
library(maps)
library(dplyr)

# Crear datos de ejemplo (como tu CSV)
datos <- data.frame(
  geography = c("Spain", "France", "Germany"),
  value = c(10, 20, 15)
)

# Obtener datos del mapa mundial
world_map <- map_data("world")

# Filtrar solo los países que nos interesan
europa <- world_map %>% 
  filter(region %in% c("Spain", "France", "Germany"))

# Combinar con nuestros datos
mapa_datos <- europa %>% 
  left_join(datos, by = c("region" = "geography"))

# Crear el mapa de colores
ggplot(mapa_datos, aes(x = long, y = lat, group = group, fill = value)) +
  geom_polygon(color = "black") +
  scale_fill_gradient(low = "lightblue", high = "darkblue") +
  labs(title = "Mapa de valores para España, Francia y Alemania",
       fill = "Valor") +
  theme_minimal() +
  coord_fixed(1.3) # Ajustar relación de aspecto
