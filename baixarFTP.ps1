$ftpServer = "ftp://10.40.13.9/trans/diversos/produtos/produtos.csv"
$localFile = "C:\TXT\produtos.csv"
$username = "tcg"
$password = "tcg1234"

$webclient = New-Object System.Net.WebClient
$webclient.Credentials = New-Object System.Net.NetworkCredential($username, $password)
$webclient.DownloadFile($ftpServer, $localFile)
