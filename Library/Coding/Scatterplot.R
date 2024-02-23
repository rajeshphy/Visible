# Load necessary packages
library(ggplot2)
library(scales)
library(ggrepel)

# Data from Revigo
revigo.names <- c("term_ID", "description", "frequency", "plot_X", "plot_Y", "log_size", "value", "uniqueness", "dispensability")
revigo.data <- data.frame(
  term_ID = c("GO:01", "GO:02", "GO:03", "GO:04"),
  description = c("mitotic cell cycle", "immune system process", "carbohydrate metabolic process", "tricarboxylic acid cycle"),
  frequency = c(1.0666419329406853, 1.1964939943421602, 4.962203774984928, 0.28289199091035566),
  plot_X = c(5.064186421706109, 8.103567498529376, 1.8014359544072842, -4.739423589846138),
  plot_Y = c(-6.525445427202065, -2.838748603521349, 7.40503889940543, 5.131648707231193),
  log_size = c(2.3636119798921444, 2.413299764081252, 3.029789470831856, 1.792391689498254),
  value = c(-4.853871964321762, -9.468521082957745, -12.200659450546418, -3.2924298239020637),
  uniqueness = c(0.9487524915303618, 1, 0.9482842955678698, 0.9311505075404733),
  dispensability = c(0.03450995, 0, 0, 0.12074105)
)

# Filter out null values
one.data <- revigo.data[!is.na(revigo.data$plot_X) & !is.na(revigo.data$plot_Y), ]

# Convert character columns to numeric
numeric_cols <- c("plot_X", "plot_Y", "log_size", "value", "frequency", "uniqueness", "dispensability")
one.data[numeric_cols] <- lapply(one.data[numeric_cols], as.numeric)



# Plotting
p1 <- ggplot(data = one.data) +
  geom_point(aes(plot_X, plot_Y, colour = value, size = log_size), alpha = 0.6) +
  scale_colour_gradientn(colours = c("blue", "green", "yellow", "red"), limits = c(min(one.data$value), 0)) +
  geom_point(aes(plot_X, plot_Y, size = log_size), shape = 21, fill = "transparent", colour = alpha("black", 0.6)) +
  scale_size(range = c(5, 30)) +
  theme_bw() +
  geom_label_repel(data = subset(one.data, dispensability < 0.15), aes(plot_X, plot_Y, label = description), 
                   fill = "white", colour = alpha("black", 0.85), size = 3, box.padding = unit(0.3, "lines"),
                   segment.size = 0.5, segment.color = "black", force = 1, 
                   nudge_x = 1, nudge_y = 2, 
                   arrow = arrow(length = unit(0.02, "npc"))) +
  labs(x = "X-axis label", y = "Y-axis label") +
  theme(legend.key = element_blank()) +
  xlim(min(one.data$plot_X) - diff(range(one.data$plot_X)) / 10, max(one.data$plot_X) + diff(range(one.data$plot_X)) / 10) +
  ylim(min(one.data$plot_Y) - diff(range(one.data$plot_Y)) / 10, max(one.data$plot_Y) + diff(range(one.data$plot_Y)) / 10)

# Output the plot to screen
print(p1)

# Uncomment the line below to also save the plot to a file.
# ggsave("/path_to_your_file/revigo-plot.pdf", p1)
