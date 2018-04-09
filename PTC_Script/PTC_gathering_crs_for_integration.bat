chcp 65001

im issues --user="leemi4" --password="monitor" --query="DAS_RADAR: DAS_HK_4GH-2a_CRs_I049_RC06" --fields=id,summary > test_crs.txt

rename test_crs.txt text.tmp
for /f "delims=" %%i in (text.tmp) do (echo --^> %%i >> test_crs.txt)
del text.tmp