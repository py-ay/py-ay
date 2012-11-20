#-*- encoding:utf-8-*-

import sys
import datetime
import re

if len(sys.argv) == 3:
	original_file = sys.argv[1]	# 주간보고 텍스트 파일
	pattern_file = sys.argv[2]	# 주간보고 변환 규칙 파일
elif len(sys.argv) == 2:
	original_file = sys.argv[1]
	pattern_file = "pattern.txt"
else:
	original_file = str(datetime.date.today()) + ".txt"	# 없으면 오늘날짜
	pattern_file = "pattern.txt"

result_file =  original_file[0:original_file.rfind('.')] + "_output.txt"

# 패턴 파일 형식
# pattern|replacement - 라인단위로 읽어서 튜플로 저장하기

new_contents = ''

for content in open(original_file):
	new_contents += content

for line in open(pattern_file):
	fields = line.split("\t")
	pattern = re.compile(fields[0])
	replacement = fields[1].replace("\r", "").replace("\n", "")
	new_contents = pattern.sub(replacement, new_contents)

# default font family, size 
new_contents = '<div style="font-size: 9pt; font-family: 나눔고딕, NanumGothic, sans-serif;">' + new_contents + '</div>'

fOut = open(result_file, "w")

print >>fOut, new_contents

fOut.close()