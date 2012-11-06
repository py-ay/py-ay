#-*- encoding:utf-8-*-

import sys
import datetime
import re

if len(sys.argv) == 3:
	original_file = sys.argv[1]	# 주간보고 텍스트 파일
	pattern_file = sys.argv[2]	# 주간보고 변환 규칙 파일
else:
	original_file = str(datetime.date.today()) + ".txt"	# 없으면 오늘날짜
	pattern_file = "weekly_report_pattern.txt"

# [TODO] 패턴 파일을 읽어와서 변경하는 것으로 바꾸기

original_contents = ''

for line in open(original_file):
	original_contents += line

new_contents = original_contents

# 개행을 <p></p>로 변경용
pattern = re.compile('([^\n]*)\n')
new_contents = pattern.sub(r'<p>\1</p>', new_contents)

# 빈 <p> 처리
pattern = re.compile('<p></p>')
new_contents = pattern.sub(r'<p>&nbsp;</p>', new_contents)

# 내용에 따라 글짜 스타일 적용
pattern = re.compile('(\[이번주 할 일\])')
new_contents = pattern.sub(r'<span style="font-weight:bold;color:#ff6c00;">\1</span>', new_contents)

print new_contents
