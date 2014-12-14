pack="nginx-1.6.2.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "http://nginx.org/download/$pack" -O ~/rpmbuild/SOURCES/$pack
fi
cp sources/* ~/rpmbuild/SOURCES/
pack="ngx_http_geoip2_module-1.0.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "https://github.com/leev/ngx_http_geoip2_module/archive/1.0.tar.gz" -O ~/rpmbuild/SOURCES/$pack
fi
pack="ngx_replace_filter_module-0.01rc5.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "https://github.com/openresty/replace-filter-nginx-module/archive/v0.01rc5.tar.gz" -O ~/rpmbuild/SOURCES/$pack
fi
pack="ngx_http_substitutions_filter_module-0.6.4.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "https://github.com/yaoweibin/ngx_http_substitutions_filter_module/archive/v0.6.4.tar.gz" -O ~/rpmbuild/SOURCES/$pack
fi
RELEASE=`date +"%Y%m%d"` rpmbuild -ba nginx.spec
