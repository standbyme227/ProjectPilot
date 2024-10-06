#!/bin/bash

# 기본 변수 설정
SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/manage.py"
LINK_PATH="/usr/local/bin/manage"

# 실행 권한 추가
chmod +x "$SCRIPT_PATH"

# 전역 명령어로 심볼릭 링크 생성
if [ -L "$LINK_PATH" ]; then
    echo "이미 심볼릭 링크가 존재합니다: $LINK_PATH"
else
    sudo ln -s "$SCRIPT_PATH" "$LINK_PATH"
    echo "성공적으로 전역 명령어로 등록되었습니다: manage"
fi
