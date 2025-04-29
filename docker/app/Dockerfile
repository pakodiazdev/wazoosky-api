# Base image
FROM python:3.11-slim

# Build-time arguments
ARG CONTAINER_USERNAME
ARG LOCAL_UID
ARG LOCAL_GID

# Environment variables
ENV USERNAME=${CONTAINER_USERNAME} \
    LOCAL_GID=${LOCAL_GID} \
    LOCAL_UID=${LOCAL_UID} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    HOME=/home/${CONTAINER_USERNAME} \
    PATH="/home/${CONTAINER_USERNAME}/.local/bin:$PATH"

# Install basic tools
RUN apt-get update && apt-get install -y \
    git \
    jq  \
    locales \
    make \
    sudo \
    vim \
    && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

# Create user and configure permissions
RUN if [ -z "$LOCAL_GID" ]; then LOCAL_GID=1000; fi && \
    if [ -z "$LOCAL_UID" ]; then LOCAL_UID=1000; fi && \
    addgroup --system --gid $LOCAL_GID ${CONTAINER_USERNAME} && \
    adduser --system --uid $LOCAL_UID --gid $LOCAL_GID --shell /bin/bash ${CONTAINER_USERNAME} && \
    mkdir -p /home/${CONTAINER_USERNAME} && \
    chown ${CONTAINER_USERNAME}:${CONTAINER_USERNAME} /home/${CONTAINER_USERNAME} && \
    echo "${CONTAINER_USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${CONTAINER_USERNAME} && chmod 0440 /etc/sudoers.d/${CONTAINER_USERNAME}

# Configure bash history and prompt for user
RUN touch /home/${CONTAINER_USERNAME}/.bash_history && \
    echo 'export HISTFILE=/home/'${CONTAINER_USERNAME}'/.bash_history' >> /home/${CONTAINER_USERNAME}/.bashrc && \
    echo 'export HISTSIZE=1000' >> /home/${CONTAINER_USERNAME}/.bashrc && \
    echo 'export HISTFILESIZE=2000' >> /home/${CONTAINER_USERNAME}/.bashrc && \
    echo 'export PS1="\[\e[1;92m\]\u\[\e[0m\]@\[\e[1;34m\]\h\[\e[0m\]:\[\e[0;34m\]\w\[\e[1;92m\]\$\[\e[0m\] "' >> /home/${CONTAINER_USERNAME}/.bashrc && \
    echo '[ -f /init-scripts/welcome.sh ] && source /init-scripts/welcome.sh' >> /home/${CONTAINER_USERNAME}/.bashrc && \
    chown -R ${CONTAINER_USERNAME}:${CONTAINER_USERNAME} /home/${CONTAINER_USERNAME}

# Configure bash prompt for root
RUN echo 'export PS1="\[\e[1;31m\]\u\[\e[0m\]@\[\e[1;34m\]\h\[\e[0m\]:\[\e[0;34m\]\w\[\e[1;31m\]\#\[\e[0m\] "' >> /root/.bashrc

# Set working directory
WORKDIR /app

# Switch to non-root user
USER ${CONTAINER_USERNAME}

# Start with bash shell
CMD ["/bin/bash"]
