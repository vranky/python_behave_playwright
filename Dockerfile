FROM mcr.microsoft.com/playwright:focal

WORKDIR /workspace

COPY . /workspace

RUN python -m pip install -r requirements.txt
RUN python -m playwright install

CMD ["/bin/bash"]