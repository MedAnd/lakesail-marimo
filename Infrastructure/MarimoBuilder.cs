using Aspire.Hosting;
using Aspire.Hosting.ApplicationModel;

internal static class MarimoBuilder
{
    internal static IResourceBuilder<ContainerResource> AddMarimoInfrastructure(IDistributedApplicationBuilder builder, IResourceBuilder<ContainerResource> lakeSail)
    {
        return builder.AddDockerfile("marimo", "./docker/marimo", "Dockerfile")
            .WithImageTag("marimo-aspire")
            .WithBuildArg("PYSAIL_VERSION", "0.7.3")
            .WithBuildArg("PYSPARK_VERSION", "4.2.0")
            .WithHttpEndpoint(name: "ui", targetPort: 8080, port: 8080)
            .WithEnvironment("SAIL_SPARK_CONNECT_URL", "sc://sail:50051")
            .WithBindMount("./data", "/data")
            .WithBindMount("./sail-examples", "/sail-examples")
            .WaitFor(lakeSail);
    }
}