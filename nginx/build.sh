pack="nginx-1.6.0.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "http://nginx.org/download/$pack" -O ~/rpmbuild/SOURCES/$pack
fi
cp sources/* ~/rpmbuild/SOURCES/
RELEASE=`date +"%Y%m%d"` rpmbuild -ba nginx.spec
