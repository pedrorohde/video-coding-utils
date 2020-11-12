#sudo snap install ffmpeg

#

ENCODED_FILE=../data/H264_mp4/BasketballPass_416x240_50_H264_42.mp4
OUTPUT_DIR=../data/H264_raw/BasketballPass_416x240_50_H264_42_IPB

ffmpeg -i $ENCODED_FILE \
	-vf "select='eq(pict_type\,I)'" -vsync 0 $OUTPUT_DIR/I/frame%02d.png \
	-vf "select='eq(pict_type\,P)'" -vsync 0 $OUTPUT_DIR/P/frame%02d.png \
	-vf "select='eq(pict_type\,B)'" -vsync 0 $OUTPUT_DIR/B/frame%02d.png

