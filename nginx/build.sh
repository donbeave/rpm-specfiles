pack="nginx-1.6.0.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "http://nginx.org/download/$pack" -O ~/rpmbuild/SOURCES/$pack
fi
cp sources/* ~/rpmbuild/SOURCES/
pack="ngx_http_geoip2_module-0.1.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "https://github.com/leev/ngx_http_geoip2_module/archive/0.1.tar.gz" -O ~/rpmbuild/SOURCES/$pack
fi
RELEASE=`date +"%Y%m%d"` rpmbuild -ba nginx.spec
