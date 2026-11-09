# LakeSail + Marimo (MS Aspire Recipe)

This MS Aspire Recipe starts a LakeSail Spark Connect server and a Marimo editor. 

Marimo waits for LakeSail, uses its `sc://sail:50051` endpoint, and serves notebooks from 
`sail-examples/`. 

Both containers can access the local `data/` directory.

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
dotnet tool install -g Aspire.Cli --version 13.6.4
```

Ensure the .NET global tools directory is on your PATH, then verify with `aspire --version`.

## 🚀 Run

```sh
aspire start
```

🌐 Open the Microsoft Aspire dashboard URL printed by the CLI and use the `marimo` resource's `ui`
endpoint to open the editor. 

Put notebooks in `sail-examples/`; files in `data/` are available to both containers under `/data`.

📡 The AppHost configures LakeSail OTLP export to the local Microsoft Aspire dashboard. 

The Spark Connect endpoint is exposed on port `50051`.