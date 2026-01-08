!/bin/bash
# SPDX-FileCopyrightText: 2025 Ren
# SPDX-License-Identifier: MIT
set -eu

WS='$HOME/ros2_ws'
cd '$WS'

colcon build --packages-select mypkg > /dev/null
set +u
# shellcheck disable=SC1091
source install/local_setup.bash
set -u
LOG=/tmp/mypkg.log
rm -f '$LOG'

timeout 8 ros2 launch mypkg wareki.launch.py year:=2004 >'$LOG' 2>&1 || true

grep -q 'year=2004 -> 平成16年' '$LOG'
