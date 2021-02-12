<?php 
$sure=strtime("now");


if ($sure>=strtime("06") or $sure<strtime("10")) {
	echo "Günaydın";
}

elseif ($sure>=strtime("10") or $sure<strtime("17")) {
	echo "İyi Günler";
}

elseif ($sure>=strtime("17") or $sure<strtime("20")) {
	echo "İyi Akşamlar";
}

elseif ($sure>=strtime("20") or $sure<strtime("00")) {
	echo "İyi Geceler";
}

else {
	echo "Esenlikler Dilerim";
}

?>