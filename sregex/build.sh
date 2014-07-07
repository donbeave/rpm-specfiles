pack="sregex-0.0.1rc1.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "https://github.com/openresty/sregex/archive/v0.0.1rc1.tar.gz" -O ~/rpmbuild/SOURCES/$pack
fi
RELEASE=`date +"%Y%m%d"` rpmbuild -ba sregex.spec
