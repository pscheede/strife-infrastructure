#! /bin/bash
echo "Copy: strifeuser ALL = NOPASSWD: $(which docker)"
echo "Run: sudo visudo -f /etc/sudoers.d/strife"
