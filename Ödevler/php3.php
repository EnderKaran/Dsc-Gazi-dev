<!DOCTYPE html>
<html>
<head>
	<title>Asal Sayı Bulma</title>
</head>
<body>

	
<form action="" method="post">
	Sayı: <input type="text" name="sayi">   
	<input type="submit" name="Kontrol ET">
</form>
</body>
</html>



<?php
$say=$_POST['sayi'];
$asal=0; $i=2;
do
{ 
	if ($say % $i == 0)
	{
		
		$asal = 1;
	}
	$i++;
}
while($i<$say);
if ($asal != 1)
{
	echo "Girilen Sayı Asaldır..!";
}
else
{
	echo "Girilen Sayı Asal Değildir..!";
}
 
?>

