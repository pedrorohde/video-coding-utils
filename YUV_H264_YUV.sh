#sudo apt-get install ffmpeg

WIDTH=416
HEIGHT=240
FPS=50
QP=42
INPUT_FILE=../data/YUV/BasketballPass_416x240_50.yuv
ENCODED_FILE=../data/H264_mp4/BasketballPass_416x240_50_H264_42.mp4
DECODED_FILE=../data/H264_raw/BasketballPass_416x240_50_H264_42.yuv

ffmpeg -f rawvideo -vcodec rawvideo -s $WIDTH\x$HEIGHT -r $FPS -pix_fmt yuv420p -i $INPUT_FILE -c:v libx264 -qp $QP $ENCODED_FILE

ffmpeg -i $ENCODED_FILE -vcodec rawvideo $DECODED_FILE


