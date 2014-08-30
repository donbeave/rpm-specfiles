pack="apache-archiva-2.1.0-bin.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "http://www.us.apache.org/dist/archiva/2.1.0/binaries/$pack" -O ~/rpmbuild/SOURCES/$pack
fi
cp sources/* ~/rpmbuild/SOURCES/
RELEASE=`date +"%Y%m%d"` rpmbuild -ba archiva.spec
