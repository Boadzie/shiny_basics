from app.app_server import df
import polars as pl

total_og = df.select(pl.col("Name").n_unique()).item()

avg_employees = round(df.select(pl.col("Number of employees").mean()).item(), 2)

industry_count = df.select(pl.col("Industry").unique().count()).item()

industries = df["Industry"].unique()

founded = df["Founded"].unique()

names = df["Name"].unique()


X = df.select(pl.col(pl.Utf8)).drop(["Organization Id", "Description", "Website"])
Y = df.select(pl.col([pl.Float64, pl.Int64])).drop(["Index"])

industry_group = (
    df.groupby("Industry")
    .agg(pl.col("Number of employees").count())
    .top_k(10, by="Number of employees")
    .sort(by="Number of employees", descending=True)
)
