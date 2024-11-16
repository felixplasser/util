# add date stamp to photo using ImageMagick
#TAG="Theo-Schule_" -> set via shell

echo "TAG: $TAG"

for f in $@
do
   [ -f $f ] || exit 1
   XDT=`identify -verbose $f | grep exif:DateTime: | cut -b 20- | sed 's/:/-/g' | sed 's/ /_/'`

   if [ -z "$XDT" ]
   then
      echo "Did not find exif info for $f"
   else
      STAMP=`echo ${XDT//[-_]/} | cut -b -12`
      touch -t $STAMP $f

      PRE=${XDT}_${TAG}
      ff=${f/2019-??-??_??-??-??_/}
      mv -v ${f} ${PRE}$ff
   fi
done
