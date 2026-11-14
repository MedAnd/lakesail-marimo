# LakeSail + Marimo (MS Aspire Recipe)

This MS Aspire Recipe starts a local [LakeSail](https://lakesail.com/) Spark Connect server and a [Marimo](https://marimo.io) next-generation Python notebook editor. 

This recipe was inspired by the blog post [Bringing Rust-native Spark compatibility to Microsoft OneLake with Sail and LakeSail](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/bringing-rust-native-spark-compatibility-to-microsoft-onelake-with-sail-and-lake/5377595). 

Combining the developer productivity of [MS Aspire](https://aspire.dev/) with LakeSail, Marimo, and OneLake for a super-low-friction data analytics experience.

## 📓 Marimo workspace examples

The Marimo workspace includes two examples:

- [`Hello Sail.py`](sail-examples/Hello%20Sail.py) is a simple introduction to running Spark SQL and DataFrame operations on Sail.
- [`MS Fabric & OneLake.py`](sail-examples/MS%20Fabric%20%26%20OneLake.py) is a more advanced example that connects to a Microsoft Fabric Lakehouse, reads a Lakehouse table, and reads a Parquet file from OneLake. It requires a Microsoft Entra service principal and Microsoft Fabric workspace and Lakehouse configuration.

## 🧰 Setup

🐳 Install Docker and start the Docker engine. 

Install [dotnetup](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnetup/getting-started) from Microsoft:

🍎 On macOS or Linux:

```sh
curl -fsSL https://aka.ms/dotnetup/get-dotnetup.sh | bash
```

🪟 On Windows, in PowerShell:

```powershell
irm https://aka.ms/dotnetup/get-dotnetup.ps1 | iex
```

🔧 Follow the printed instructions to add `dotnetup` to your PATH, then open a new terminal.
Run the interactive setup:

```sh
dotnetup init
```

Choose **No, customize setup**, select the `10` SDK channel, and choose `shell` access
mode (or `everywhere` on Windows). 

Open a new terminal after setup, then verify the SDK:

```sh
dotnet --version
dotnetup list
```

📦 Install the Microsoft Aspire CLI version used by this project:

```sh
dotnet tool install -g Aspire.Cli --version 13.6.5
```

Ensure the .NET global tools directory is on your PATH, then verify with `aspire --version`.

## 🚀 Run

```sh
aspire start
```

🌐 Open the Microsoft Aspire dashboard URL printed by the CLI and use the `marimo` resource's `ui` endpoint to open the editor. 

📡 LakeSail OpenTelemetry support is still experimental with OTLP export (logs, metrics and traces) to the local Microsoft Aspire dashboard enabled. 

The Spark Connect endpoint is exposed on port `50051`.

## 📚 References

- Refer to the [OneLake catalog guide](https://docs.lakesail.com/sail/latest/guide/catalog/onelake.html) in the Sail documentation.
- Learn more about [Microsoft OneLake](https://learn.microsoft.com/fabric/onelake/onelake-overview).
- Explore [Sail on GitHub](https://github.com/lakehq/sail) and the [getting started guide](https://docs.lakesail.com/sail/latest/introduction/getting-started/).
