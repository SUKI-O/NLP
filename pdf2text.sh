# Change the target to your own

for file in /Users/itsukiogihara/Documents/SCAN/J9/MEMO_copy/*.pdf
do
    pdftotext -enc UTF-8 $file
done



for file in ./*.txt
do 
mv $file ./texts/$file
done