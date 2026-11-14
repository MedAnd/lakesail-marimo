import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    from pysail.spark import SparkConnectServer
    from pyspark.sql import SparkSession

    # ============================================================
    # OneLake Authentication (Service Principal)
    # ============================================================
    # Replace with your Microsoft Entra application details.

    os.environ["AZURE_TENANT_ID"] = "<AZURE_TENANT_ID>"
    os.environ["AZURE_CLIENT_ID"] = "<AZURE_CLIENT_ID>"
    os.environ["AZURE_CLIENT_SECRET"] = "<AZURE_CLIENT_SECRET>"

    # ============================================================
    # Register OneLake Catalog
    # ============================================================
    # Replace workspace and lakehouse with your actual values.

    os.environ["SAIL_CATALOG__LIST"] = (
        '[{type="onelake", name="fabric", '
        'url="<MS_FABRIC_WORKSAPCE and MS_FABRIC_LAKEHOUSE>", '
        'api="delta"}]'
    )

    # ============================================================
    # Start an embedded Sail Spark Connect server
    # ============================================================

    server = SparkConnectServer()
    spark = None

    try:
        server.start()

        listening_address = server.listening_address
        if listening_address is None:
            raise RuntimeError("The Sail Spark Connect server did not start.")

        host, port = listening_address
        remote_url = f"sc://{host}:{port}"
        print(f"Connecting to Sail at {remote_url}")

        spark = (
            SparkSession.builder
            .remote(remote_url)
            .getOrCreate()
        )

        print("\n=== SHOW CATALOGS ===")
        spark.sql("SHOW CATALOGS").show(n=100, truncate=False)

        print("\n=== SHOW SCHEMAS IN fabric ===")
        spark.sql("SHOW SCHEMAS IN fabric").show(n=100, truncate=False)

        print("\n=== SHOW TABLES IN fabric.dbo ===")
        spark.sql("SHOW TABLES IN fabric.dbo").show(n=100, truncate=False)

        # ========================================================
        # MS Fabric Lakehouse sample data table read example
        # ========================================================

        print("\n=== READ publicholidays ===")

        public_holidays = spark.table("fabric.dbo.publicholidays")

        public_holidays.printSchema()

        public_holidays.show(50, truncate=False)

        print(f"Row count: {public_holidays.count()}")

        # ========================================================
        # MS Fabric Lakehouse sample parquet file read example
        # ========================================================

        print("\n=== SHOW TABLES ===")
        spark.sql("SHOW TABLES IN fabric.dbo").show(
            n=100,
            truncate=False,
        )

        # Replace workspace and lakehouse with your actual values.
        parquet_path = (
            "abfss://<MS_FABRIC_WORKSAPCE>@onelake.dfs.fabric.microsoft.com/"
            "<MS_FABRIC_LAKEHOUSE>/Files/sample_datasets/"
            "public_holidays.parquet"
        )

        print("\n=== PARQUET PATH ===")
        print(parquet_path)

        holidays = spark.read.parquet(parquet_path)

        print("\n=== PARQUET SCHEMA ===")
        holidays.printSchema()

        print("\n=== PARQUET DATA ===")
        holidays.show(50, truncate=False)

        print("\n=== PARQUET ROW COUNT ===")
        print(holidays.count())

    finally:
        if spark is not None:
            spark.stop()

        if server.running:
            server.stop()
    return


if __name__ == "__main__":
    app.run()
