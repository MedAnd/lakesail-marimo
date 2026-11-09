FROM python:3.14-slim

ARG PYSAIL_VERSION
ARG PYSPARK_VERSION

RUN test -n "${PYSAIL_VERSION}" \
    && test -n "${PYSPARK_VERSION}" \
    && python3 -m pip install --no-cache-dir \
        "pysail==${PYSAIL_VERSION}" \
        "pyspark-client==${PYSPARK_VERSION}"

ENTRYPOINT ["/usr/local/bin/sail"]