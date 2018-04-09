chcp 65001

call _PTC_Env_.bat 

si viewcps --user=USER_ --password=PASSWORD_ --query=QUERYNAME_ > test_cps.txt

FOR /f "tokens=1,2,3,4,5* delims=	" %%i in (test_cps.txt) DO (
	im viewcp --user=USER_ --password=PASSWORD_ --attributes=id,summary,status --EntryAttributes=member,revision,project %%i  >> test_package.txt 
)