FROM 3scale/base:precise
MAINTAINER Michal Cichra <michal@3scale.net> # 2014-02-24

# all the apt-gets in one command & delete the cache after installing
RUN apt-get -q -y update \
 && apt-get -q -y install software-properties-common python-software-properties \
 && apt-add-repository -y ppa:chris-lea/redis-server \
 && apt-get -q -y update \
 && apt-get -q -y install redis-server cron luarocks supervisor logrotate \
                          make build-essential libpcre3-dev libssl-dev wget \
 && apt-get -q -y clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

ENV OPENRESTY_VERSION 1.5.12.1

RUN wget -nv http://openresty.org/download/ngx_openresty-$OPENRESTY_VERSION.tar.gz \
         -O /root/ngx_openresty-$OPENRESTY_VERSION.tar.gz \
 && tar -xzf /root/ngx_openresty-$OPENRESTY_VERSION.tar.gz -C /root/ \
 && cd /root/ngx_openresty-$OPENRESTY_VERSION/ \
 && ./configure \
    --prefix=/opt/openresty  \
    --with-http_gunzip_module \
    --with-luajit \
    --with-http_stub_status_module \
    --with-http_ssl_module \
 && make \
 && make install \
 && rm -rf /root/ngx_openresty-$OPENRESTY_VERSION*

#RUN echo "daemon off;" >> /opt/openresty/nginx/conf/nginx.conf
ADD nginx.conf /opt/openresty/nginx/conf/nginx.conf

EXPOSE 80

ADD . /var/www

WORKDIR /opt/openresty/nginx
