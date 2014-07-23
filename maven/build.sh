pack="apache-maven-3.2.2-bin.tar.gz"
if [ ! -f ~/rpmbuild/SOURCES/$pack ];
then
    wget "http://www.eng.lsu.edu/mirrors/apache/maven/maven-3/3.2.2/binaries/$pack" -O ~/rpmbuild/SOURCES/$pack
fi
RELEASE=`date +"%Y%m%d"` rpmbuild -ba maven.spec
