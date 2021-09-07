FROM mcr.microsoft.com/playwright:focal

WORKDIR /workspace

COPY . /workspace

# Install essential packages
RUN apt-get update -y \
    && apt-get -y install \
        dumb-init gnupg wget ca-certificates apt-transport-https \
        ttf-wqy-zenhei unzip \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install Chrome Headless Browser
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -y \
    && apt-get -y install google-chrome-unstable \
    && rm /etc/apt/sources.list.d/google-chrome.list \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Install test repo libs
RUN python -m pip install -r requirements.txt
RUN python -m playwright install-deps

CMD ["/bin/bash"]