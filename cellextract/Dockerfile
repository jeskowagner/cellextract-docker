FROM mambaorg/micromamba:alpine3.19
COPY --chown=$MAMBA_USER:$MAMBA_USER cellextract.yaml /tmp/env.yaml

# Install dependencies
RUN micromamba install -y -n base \
    -f /tmp/env.yaml && \
    micromamba clean -ay