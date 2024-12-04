import plotly.express as px
import pandas as pd

# Load your data
file_path = "./Avocado Stages.csv"
avocado_data = pd.read_csv(file_path)

# Convert date columns to datetime
date_columns = ["seed", "split", "germination", "sprout", "seedling"]
for col in date_columns:
    avocado_data[col] = pd.to_datetime(
        avocado_data[col], format="%d/%m/%y", errors="coerce"
    )

# Prepare the data for plotting
stages_dict = {"seed": 1, "split": 2, "germination": 3, "sprout": 4, "seedling": 5}
plot_data = []
for _, row in avocado_data.iterrows():
    for stage in stages_dict:
        if pd.notnull(row[stage]):
            color = "green" if row["environment"] == "soil" else "blue"
            plot_data.append(
                {
                    "Date": row[stage],
                    "Stage": stages_dict[stage],
                    "Avocado ID": row["avocado_id"],
                    "Color": color,
                }
            )

# Convert to DataFrame
plot_df = pd.DataFrame(plot_data)

# Create a line plot for each avocado
fig = px.line(
    plot_df,
    x="Date",
    y="Stage",
    color="Avocado ID",
    line_group="Avocado ID",
    hover_name="Avocado ID",
)

# Update layout and axis labels
fig.update_layout(
    title="Interactive Evolution of Avocado Stages Over Time",
    xaxis_title="Date",
    yaxis_title="Stage",
    yaxis=dict(
        tickmode="array",
        tickvals=list(stages_dict.values()),
        ticktext=list(stages_dict.keys()),
    ),
)

# Show the plot
fig.show()
