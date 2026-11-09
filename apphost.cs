using Aspire.Hosting;
using Microsoft.Extensions.Configuration;

var builder = DistributedApplication.CreateBuilder(args);

var lakeSail = LakeSailBuilder.AddLakeSailInfrastructure(builder);
MarimoBuilder.AddMarimoInfrastructure(builder, lakeSail);

builder.Build().Run();