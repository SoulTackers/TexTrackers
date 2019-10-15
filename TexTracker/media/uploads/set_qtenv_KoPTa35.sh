#!/bin/bash
# sets the Qt high resolution as a system environment variable
# by modifying /etc/profile 

# check /etc/profile for existance of QT_DEVICE_PIXEL_RATIO
PROFILE="/etc/profile" 

# error exit if file does not exist or unreadable
if [ ! -f $PROFILE ]; then
   echo "$PROFILE does not exists"
   exit 1
elif [ ! -r $PROFILE ]; then
   echo "$PROFILE: can not read"
   exit 2
fi

# read contents
CONTENTS=""
EXPORT_EXISTS=0
QT_EXISTS=0
QT_FOUND=0
exec 3<&0
exec 0<$PROFILE
while read -r line
do
  
  # replace existing entries
  QT_FOUND=`expr match "$line" 'QT_DEVICE_PIXEL_RATIO'`
  if [ $QT_FOUND -gt 0 ]; then
	line="QT_DEVICE_PIXEL_RATIO=auto"
        QT_EXISTS=1
  fi

  # check for export statement
  if [ $EXPORT_EXISTS -eq 0 ]; then
      EXPORT_EXISTS=`expr match "$line" 'export QT_DEVICE_PIXEL_RATIO'`
  fi

  #append the line to the contents
  CONTENTS="$CONTENTS\n$line"
done
exec 0<&3

if [ $QT_EXISTS -eq 0 ]; then
  CONTENTS="$CONTENTS\nQT_DEVICE_PIXEL_RATIO=auto"
fi

if [ $EXPORT_EXISTS -eq 0 ]; then
  CONTENTS="$CONTENTS\nexport QT_DEVICE_PIXEL_RATIO"
fi

echo "Writing QT_DEVICE_PIXEL_RATIO environment variable to /etc/profile"
sudo echo -e $CONTENTS > /etc/profile

exit 0 

