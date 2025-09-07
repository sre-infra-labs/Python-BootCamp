#cls
$directory = '/stale-storage/Study-Zone/Python/Complete Python Bootcamp'
$srtFiles = Get-ChildItem -Path $directory -Recurse -File -Name *.srt
foreach($file in $srtFiles) {
  $filePath = "$directory/$file"
  $filePath | Remove-Item
  #break
}
