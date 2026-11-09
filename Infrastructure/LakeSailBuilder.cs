using Aspire.Hosting;
using Aspire.Hosting.ApplicationModel;
using Microsoft.Extensions.Configuration;

internal static class LakeSailBuilder
{
    internal static IResourceBuilder<ContainerResource> AddLakeSailInfrastructure(IDistributedApplicationBuilder builder) 
    {
        return builder.AddDockerfile("sail", "./docker/sail", "Dockerfile")
            .WithImageTag("sail-aspire")
            .WithBuildArg("PYSAIL_VERSION", "0.7.3")
            .WithBuildArg("PYSPARK_VERSION", "4.2.0")
            .WithArgs("spark", "server", "--ip", "0.0.0.0", "--port", "50051")
            .WithBindMount("./data", "/data")
            .WithEndpoint(name: "spark-connect", scheme: "tcp", targetPort: 50051, isExternal: true)
            .WithEnvironment("SAIL_TELEMETRY__EXPORTER__OTLP__ENDPOINT", "http://aspire.dev.internal:19217")
            .WithEnvironment("SAIL_TELEMETRY__EXPORTER__OTLP__PROTOCOL", "grpc")
            .WithEnvironment("SAIL_TELEMETRY__EXPORTER__SYSTEM__ENABLED", "true")
            .WithEnvironment("SAIL_TELEMETRY__EXPORT_TRACES", "true")
            .WithEnvironment("SAIL_TELEMETRY__EXPORT_METRICS", "true")
            .WithEnvironment("SAIL_TELEMETRY__EXPORT_LOGS", "true")
            .WithOtlpExporter();
    }
}