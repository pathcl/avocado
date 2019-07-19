FROM python:3.7-alpine as base
FROM base as builder
 
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base
COPY --from=builder /install /usr/local
ENV VSPHERE_VCENTER vcenter.domain.tld
ENV VSPHERE_USER username
ENV VSPHERE_PASSWORD password
COPY . /app
COPY templates /app
WORKDIR /app
EXPOSE 8000
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000","app:app"]
