FROM ghcr.io/marimo-team/marimo:latest-data

ARG PYSAIL_VERSION
ARG PYSPARK_VERSION

RUN test -n "${PYSAIL_VERSION}" \
    && test -n "${PYSPARK_VERSION}" \
    && uv pip install --no-cache-dir \
        "pysail==${PYSAIL_VERSION}" \
        "pyspark-client==${PYSPARK_VERSION}"

WORKDIR /sail-examples

EXPOSE 8080

CMD ["marimo", "edit", "--no-token", "--host", "0.0.0.0", "--port", "8080", "/sail-examples"]