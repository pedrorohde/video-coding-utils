# install rclone
curl https://rclone.org/install.sh | sudo bash

# initial setup (https://rclone.org/drive/)
rclone config

# copy files from local to remote
rclone -v copy path/to/files remote:path/to/files
