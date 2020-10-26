#sudo snap install ffmpeg

#WIDTH=
#HEIGHT=
#FPS=
#QP=
#INPUT_FILE=
#ENCODED_FILE=
#DECODED_FILE=

ffmpeg -f rawvideo -vcodec rawvideo -s $WIDTH\x$HEIGHT -r $FPS -pix_fmt yuv420p -i $INPUT_FILE -c:v libx264 -qp $QP $ENCODED_FILE

ffmpeg -i $ENCODED_FILE -vcodec rawvideo $DECODED_FILE



