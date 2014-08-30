pack="libmaxminddb-0.5.6.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "https://github.com/maxmind/libmaxminddb/releases/download/0.5.6/$pack" -O ~/rpmbuild/SOURCES/$pack
fi
RELEASE=`date +"%Y%m%d"` rpmbuild -ba libmaxminddb.spec
