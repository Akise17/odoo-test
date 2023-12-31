FROM odoo:14.0

WORKDIR /usr/src/app

COPY . .
RUN mkdir config
RUN pip3 install -r requirements.txt

EXPOSE 8069

CMD ["./odoo-bin", "-c", "./config/odoo.conf", "--update=all"]